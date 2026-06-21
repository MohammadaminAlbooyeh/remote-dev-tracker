from backend.services.payment_service import calculate_session_payment
from datetime import datetime
import pytz

CET = pytz.timezone("Europe/Rome")


def test_calculate_payment():
    start = CET.localize(datetime(2026, 6, 1, 9, 0, 0))
    end = CET.localize(datetime(2026, 6, 1, 17, 30, 0))
    result = calculate_session_payment(start, end, 25.0)
    assert result["duration_hours"] == 8.5
    assert result["amount"] == 212.5


def test_zero_hours():
    start = CET.localize(datetime(2026, 6, 1, 9, 0, 0))
    end = CET.localize(datetime(2026, 6, 1, 9, 0, 0))
    result = calculate_session_payment(start, end, 25.0)
    assert result["duration_hours"] == 0.0
    assert result["amount"] == 0.0
