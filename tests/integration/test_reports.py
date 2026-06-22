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


def _clock_in_out(client, token):
    client.post("/api/v1/sessions/clock-in", headers={"Authorization": f"Bearer {token}"})
    res = client.post("/api/v1/sessions/clock-out", json={}, headers={"Authorization": f"Bearer {token}"})
    return res.json()


def test_daily_report(client):
    token = _register_and_login(client)
    _clock_in_out(client, token)
    res = client.get("/api/v1/reports/daily", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    data = res.json()
    assert data["summary"]["total_sessions"] == 1
    assert data["summary"]["total_hours"] >= 0
    assert data["summary"]["total_amount"] >= 0


def test_weekly_report(client):
    token = _register_and_login(client)
    _clock_in_out(client, token)
    res = client.get("/api/v1/reports/weekly", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    data = res.json()
    assert data["summary"]["total_sessions"] == 1


def test_monthly_report(client):
    token = _register_and_login(client)
    _clock_in_out(client, token)
    res = client.get("/api/v1/reports/monthly", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    data = res.json()
    assert data["summary"]["total_sessions"] == 1


def test_custom_date_range(client):
    token = _register_and_login(client)
    _clock_in_out(client, token)
    res = client.get("/api/v1/reports/custom", params={
        "start": "2026-01-01",
        "end": "2026-12-31",
    }, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    data = res.json()
    assert data["summary"]["total_sessions"] >= 1


def test_empty_report_for_future_date(client):
    token = _register_and_login(client)
    _clock_in_out(client, token)
    res = client.get("/api/v1/reports/custom", params={
        "start": "2099-01-01",
        "end": "2099-12-31",
    }, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    data = res.json()
    assert data["summary"]["total_sessions"] == 0
