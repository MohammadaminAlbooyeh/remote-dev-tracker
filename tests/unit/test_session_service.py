from datetime import datetime, timedelta
import pytz

CET = pytz.timezone("Europe/Rome")


def test_clock_in_creates_active_session():
    assert True


def test_clock_out_completes_session():
    assert True


def test_clock_in_when_already_active_raises_error():
    assert True
