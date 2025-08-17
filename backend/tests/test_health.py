import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"ok": True}

def test_metrics_exposes_prometheus_text():
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "sovren_requests_total" in r.text

