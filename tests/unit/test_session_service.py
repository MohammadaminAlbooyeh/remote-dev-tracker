from unittest.mock import MagicMock, patch
from backend.services.session_service import SessionService
from backend.models.session import Session


def test_clock_in_creates_active_session():
    db = MagicMock()
    db.query.return_value.filter.return_value.first.return_value = None
    service = SessionService(db)
    session = service.clock_in("dev-1")
    assert session.developer_id == "dev-1"
    assert session.status == "active"
    db.add.assert_called_once()
    db.commit.assert_called_once()


def test_clock_out_completes_session():
    db = MagicMock()
    active = Session(id="s-1", developer_id="dev-1", status="active")
    active.start_time = MagicMock()
    db.query.return_value.filter.return_value.first.side_effect = [active, MagicMock(hourly_rate=25.0)]
    service = SessionService(db)
    session = service.clock_out("dev-1")
    assert session.status == "completed"
    assert session.duration is not None
    db.commit.assert_called_once()


def test_clock_in_when_already_active_raises_error():
    db = MagicMock()
    active = Session(id="s-1", developer_id="dev-1", status="active")
    active.start_time = MagicMock()
    db.query.return_value.filter.return_value.first.return_value = active
    service = SessionService(db)
    import pytest
    with pytest.raises(ValueError, match="Already clocked in"):
        service.clock_in("dev-1")


def test_clock_out_with_no_active_session_raises_error():
    db = MagicMock()
    db.query.return_value.filter.return_value.first.return_value = None
    service = SessionService(db)
    import pytest
    with pytest.raises(ValueError, match="No active session"):
        service.clock_out("dev-1")


def test_get_active_session_returns_active():
    db = MagicMock()
    active = Session(id="s-1", developer_id="dev-1", status="active")
    db.query.return_value.filter.return_value.first.return_value = active
    service = SessionService(db)
    result = service.get_active_session("dev-1")
    assert result is not None
    assert result.id == "s-1"


def test_get_user_sessions_orders_by_start_time_desc():
    db = MagicMock()
    mock_query = db.query.return_value
    mock_filter = mock_query.filter.return_value
    mock_order = mock_filter.order_by.return_value
    mock_order.offset.return_value.limit.return_value.all.return_value = []
    service = SessionService(db)
    result = service.get_user_sessions("dev-1")
    assert result == []
