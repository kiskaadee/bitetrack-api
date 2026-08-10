from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_register_user_success():
    """
    Happy path check
    """
    payload = {
        "email": "staff@bitetrack.com",
        "nickname": "staff_member",
        "firstname": "Anne",
        "lastname": "Droid",
        "dob": "1999-02-13",
        "role": "staff",
        "password": "supersecurepassword123"
    }

    response = client.post("/api/v2/auth/register", json=payload)

    # Assert status code is 201
    assert response.status_code == 201
    # Parse JSON response body
    data = response.json()
    expected_fields = ["id", "nickname", "firstname", "lastname", "dob", "role", "created_at"]
    for field in expected_fields:
        assert field in data, f"Attribute '{field}' missing from user data."
    assert data["email"] == "staff@bitetrack.com", f"Expected email: staff@bitetrack.com, got: {data['email']}"
    assert "password" not in data, "Password included in response object."

def test_register_user_validation_error():
    """
    Sad Path Check
    """

    payload = {
        "email": "invalid-email",
        "nickname" : "staff_member",
        "firstname": "Anne",
        "lastname": "Droid",
        "dob": "1995-10-25",
        "role": "staff",
        "password": "short"
    }

    response = client.post("/api/v2/auth/register", json=payload)
    # Assert status code is 422 Unprocessable Content
    assert response.status_code == 422, f"Expected Status Code: 422, Got: {response.status_code}"

    data = response.json()
    assert "detail" in data, "Response detail object missing"
