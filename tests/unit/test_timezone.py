from backend.utils.timezone import now_cet, to_cet, format_cet
from datetime import datetime
import pytz

CET = pytz.timezone("Europe/Rome")


def test_now_cet_returns_aware_datetime():
    t = now_cet()
    assert t.tzinfo is not None
    assert str(t.tzinfo) == "Europe/Rome"


def test_to_cet_converts_naive():
    naive = datetime(2026, 6, 1, 12, 0, 0)
    result = to_cet(naive)
    assert result.tzinfo is not None


def test_format_cet():
    naive = datetime(2026, 6, 1, 12, 30, 0)
    formatted = format_cet(naive)
    assert "CET" in formatted
    assert "12:30" in formatted
