from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_fetch_rates():
    response = client.post("/currencies/fetch")
    assert response.status_code == 200

def test_get_currencies():
    response = client.get("/currencies/")
    assert response.status_code == 200
