import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_item():
    response = client.get("/api/items/123")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 123
    assert "CI/CD demo item" in data["message"]

