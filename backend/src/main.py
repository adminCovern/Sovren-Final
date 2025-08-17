from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from prometheus_client import CollectorRegistry, Counter, generate_latest, CONTENT_TYPE_LATEST

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

@app.get("/metrics")
def metrics():
    data = generate_latest(registry)
    return PlainTextResponse(data.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)

