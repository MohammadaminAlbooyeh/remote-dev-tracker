def _register_and_login(client):
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
    return res.json()["access_token"]


def test_clock_in_and_out_flow(client):
    token = _register_and_login(client)
    clock_in_res = client.post("/api/v1/sessions/clock-in", headers={"Authorization": f"Bearer {token}"})
    assert clock_in_res.status_code == 200
    data = clock_in_res.json()
    assert data["status"] == "active"
    assert "id" in data
    session_id = data["id"]

    clock_out_res = client.post("/api/v1/sessions/clock-out", json={"note": "Done"}, headers={"Authorization": f"Bearer {token}"})
    assert clock_out_res.status_code == 200
    data = clock_out_res.json()
    assert data["status"] == "completed"
    assert data["id"] == session_id
    assert data["duration"] is not None
    assert data["amount"] is not None
    assert data["note"] == "Done"


def test_clock_in_twice_fails(client):
    token = _register_and_login(client)
    client.post("/api/v1/sessions/clock-in", headers={"Authorization": f"Bearer {token}"})
    res = client.post("/api/v1/sessions/clock-in", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 400
    assert "Already clocked in" in res.json()["detail"]


def test_clock_out_without_clock_in_fails(client):
    token = _register_and_login(client)
    res = client.post("/api/v1/sessions/clock-out", json={}, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 400
    assert "No active session" in res.json()["detail"]


def test_list_sessions_returns_user_sessions(client):
    token = _register_and_login(client)
    client.post("/api/v1/sessions/clock-in", headers={"Authorization": f"Bearer {token}"})
    client.post("/api/v1/sessions/clock-out", json={}, headers={"Authorization": f"Bearer {token}"})
    res = client.get("/api/v1/sessions", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 1
    assert data[0]["status"] == "completed"
