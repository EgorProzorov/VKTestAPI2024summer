from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json() == {"username": "testuser"}
