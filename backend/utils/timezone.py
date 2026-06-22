from datetime import datetime, date
import pytz

CET = pytz.timezone("Europe/Rome")


def now_cet() -> datetime:
    return datetime.now(CET)


def to_cet(dt: datetime | date) -> datetime:
    if isinstance(dt, date) and not isinstance(dt, datetime):
        dt = datetime.combine(dt, datetime.min.time())
    if dt.tzinfo is None:
        return CET.localize(dt)
    return dt.astimezone(CET)


def format_cet(dt: datetime) -> str:
    return to_cet(dt).strftime("%Y-%m-%d %H:%M:%S CET")
