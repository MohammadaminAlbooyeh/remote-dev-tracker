from unittest.mock import MagicMock
from backend.services.csv_service import CSVService
from backend.models.session import Session
from datetime import datetime
import pytz

CET = pytz.timezone("Europe/Rome")


def test_csv_header_format():
    db = MagicMock()
    db.query.return_value.filter.return_value.order_by.return_value.all.return_value = []
    service = CSVService(db)
    csv_data = service.export_user_csv("dev-1")
    assert "Date" in csv_data
    assert "Start Time (CET)" in csv_data
    assert "End Time (CET)" in csv_data
    assert "Hours" in csv_data
    assert "Amount" in csv_data
    lines = csv_data.strip().split("\n")
    assert "Rate" in lines[0]


def test_csv_row_format():
    db = MagicMock()
    session = Session(
        id="s-1",
        developer_id="dev-1",
        start_time=CET.localize(datetime(2026, 6, 1, 9, 0, 0)),
        end_time=CET.localize(datetime(2026, 6, 1, 17, 30, 0)),
        duration=8.5,
        amount=212.5,
        status="completed",
    )
    db.query.return_value.filter.return_value.order_by.return_value.all.return_value = [session]
    service = CSVService(db)
    csv_data = service.export_user_csv("dev-1")
    lines = [l for l in csv_data.strip().split("\n") if l.strip()]
    assert len(lines) == 3
    assert "2026-06-01" in lines[1]
    assert "8.50" in lines[1]
    assert "212.50" in lines[1]


def test_csv_all_export_includes_developer_names():
    db = MagicMock()
    user = MagicMock()
    user.name = "John Doe"
    user.id = "dev-1"
    session = Session(
        id="s-1",
        developer_id="dev-1",
        start_time=CET.localize(datetime(2026, 6, 1, 9, 0, 0)),
        end_time=CET.localize(datetime(2026, 6, 1, 17, 30, 0)),
        duration=8.5,
        amount=212.5,
        status="completed",
    )
    db.query.return_value.filter.return_value.order_by.return_value.all.return_value = [session]
    db.query.return_value.filter.return_value.first.return_value = user
    service = CSVService(db)
    csv_data = service.export_all_csv()
    assert "Developer Name" in csv_data
    assert "John Doe" in csv_data


def test_csv_empty_returns_only_headers_and_total():
    db = MagicMock()
    db.query.return_value.filter.return_value.order_by.return_value.all.return_value = []
    service = CSVService(db)
    csv_data = service.export_user_csv("dev-1")
    lines = [l for l in csv_data.strip().split("\n") if l.strip()]
    assert len(lines) == 2
