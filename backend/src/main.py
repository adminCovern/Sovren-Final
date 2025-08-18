from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from prometheus_client import CollectorRegistry, Counter, generate_latest, CONTENT_TYPE_LATEST
import os
import time
from sqlalchemy import text
from src.db import engine  # reuse configured SQLAlchemy engine
import redis as redis_lib
from pymongo import MongoClient
from src.telephony.service import resolve_did

app = FastAPI(title="Sovren AI Backend")

# Prometheus metrics registry and example counter
registry = CollectorRegistry()
request_count = Counter(
    "sovren_requests_total",
    "Total number of requests to Sovren backend",
    registry=registry,
)

@app.get("/health")
def health():
    request_count.inc()
    return JSONResponse({"ok": True})

@app.get("/status")
def status():
    """Deep status check across core dependencies."""
    results = {}

    # Postgres
    t0 = time.perf_counter()
    try:
        with engine.connect() as conn:
            conn.execute(text("select 1"))
        results["postgres"] = {"ok": True, "latency_ms": round((time.perf_counter()-t0)*1000, 2)}
    except Exception as e:
        results["postgres"] = {"ok": False, "error": str(e)}

    # Redis
    t0 = time.perf_counter()
    try:
        redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
        r = redis_lib.from_url(redis_url)
        r.ping()
        results["redis"] = {"ok": True, "latency_ms": round((time.perf_counter()-t0)*1000, 2)}
    except Exception as e:
        results["redis"] = {"ok": False, "error": str(e)}

    # Mongo
    t0 = time.perf_counter()
    try:
        mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")
        mc = MongoClient(mongo_uri, serverSelectionTimeoutMS=1500)
        mc.admin.command("ping")
        results["mongo"] = {"ok": True, "latency_ms": round((time.perf_counter()-t0)*1000, 2)}
    except Exception as e:
        results["mongo"] = {"ok": False, "error": str(e)}

    overall_ok = all(part.get("ok") for part in results.values())
    return JSONResponse({"ok": overall_ok, "services": results})

@app.get("/metrics")
def metrics():
    data = generate_latest(registry)
    return PlainTextResponse(data.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)

@app.get("/telephony/resolve")
def telephony_resolve(did: str):
    return JSONResponse(resolve_did(did))

from fastapi import Header

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

@app.post("/telephony/admin/map")
def admin_upsert_mapping(did: str, persona: str, cnam: str, authorization: str | None = Header(default=None)):
    if not ADMIN_TOKEN:
        return JSONResponse({"ok": False, "error": "admin disabled"}, status_code=403)
    if not authorization or authorization != f"Bearer {ADMIN_TOKEN}":
        return JSONResponse({"ok": False, "error": "unauthorized"}, status_code=401)
    from src.telephony.service import upsert_mapping
    with SessionLocal() as session:
        m = upsert_mapping(session, did, persona, cnam)
        return JSONResponse({"ok": True, "did": m.did, "persona": m.persona, "cnam": m.cnam})

@app.delete("/telephony/admin/map")
def admin_delete_mapping(did: str, authorization: str | None = Header(default=None)):
    if not ADMIN_TOKEN:
        return JSONResponse({"ok": False, "error": "admin disabled"}, status_code=403)
    if not authorization or authorization != f"Bearer {ADMIN_TOKEN}":
        return JSONResponse({"ok": False, "error": "unauthorized"}, status_code=401)
    from src.telephony.service import delete_mapping
    with SessionLocal() as session:
        ok = delete_mapping(session, did)
        return JSONResponse({"ok": ok})



