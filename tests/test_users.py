from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_my_profile_success():
    """Verify GET /api/v2/users/me returns the profile."""
    response = client.get("/api/v2/users/me")
    assert response.status_code == 200
    data = response.json()
    expected_fields = ["id", "nickname", "firstname", "lastname", "email", "dob", "role", "modified_at"]
    for field in expected_fields:
        assert field in data, f"Field '{field}' missing in response"


def test_patch_my_profile_success():
    """Verify PATCH /api/v2/users/me updates fields partially."""
    payload = {
        "firstname": "Billy",
        "nickname": "Corgan",
    }
    response = client.patch("/api/v2/users/me", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["firstname"] == "Billy"
    assert data["nickname"] == "Corgan"
    # Unchanged fields remain intact
    assert data["lastname"] == "Collie"


def test_patch_my_profile_validation_error():
    """Verify invalid patch data triggers 422 Unprocessable Entity."""
    payload = {
        "dob": "2999-01-01",  # Future date
    }
    response = client.patch("/api/v2/users/me", json=payload)
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
