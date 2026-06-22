def test_register_developer(client):
    res = client.post("/api/v1/auth/register", json={
        "name": "Test Dev",
        "email": "test@example.com",
        "password": "secret123",
        "hourly_rate": 25.0,
    })
    assert res.status_code == 200
    data = res.json()
    assert data["name"] == "Test Dev"
    assert data["email"] == "test@example.com"
    assert data["role"] == "dev"
    assert data["is_online"] is False


def test_login_returns_token(client):
    client.post("/api/v1/auth/register", json={
        "name": "Test Dev",
        "email": "test@example.com",
        "password": "secret123",
        "hourly_rate": 25.0,
    })
    res = client.post("/api/v1/auth/login", json={
        "email": "test@example.com",
        "password": "secret123",
    })
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client):
    res = client.post("/api/v1/auth/login", json={
        "email": "nonexistent@example.com",
        "password": "wrong",
    })
    assert res.status_code == 401
    assert "Invalid credentials" in res.json()["detail"]


def test_register_duplicate_email(client):
    payload = {
        "name": "Test Dev",
        "email": "test@example.com",
        "password": "secret123",
        "hourly_rate": 25.0,
    }
    client.post("/api/v1/auth/register", json=payload)
    res = client.post("/api/v1/auth/register", json=payload)
    assert res.status_code == 400
    assert "already registered" in res.json()["detail"]


def test_me_returns_current_user(client):
    client.post("/api/v1/auth/register", json={
        "name": "Test Dev",
        "email": "test@example.com",
        "password": "secret123",
        "hourly_rate": 25.0,
    })
    login_res = client.post("/api/v1/auth/login", json={
        "email": "test@example.com",
        "password": "secret123",
    })
    token = login_res.json()["access_token"]
    res = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["email"] == "test@example.com"


def test_me_without_token_fails(client):
    res = client.get("/api/v1/auth/me")
    assert res.status_code == 401
