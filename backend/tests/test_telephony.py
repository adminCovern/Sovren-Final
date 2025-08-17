from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_resolve_not_found():
    r = client.get("/telephony/resolve", params={"did": "19999999999"})
    assert r.status_code == 200
    data = r.json()
    assert data["ok"] is False
    assert "DID not mapped" in data.get("error", "")

