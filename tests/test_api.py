from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_student():
    res = client.post("/students", json={"name": "Asha", "email": "asha@example.com"})
    assert res.status_code in (201, 409)
    res = client.get("/students")
    assert res.status_code == 200
    assert any(s["email"] == "asha@example.com" for s in res.json())


def test_missing_student_returns_404():
    res = client.get("/students/999999")
    assert res.status_code == 404