from datetime import datetime
import pytz

CET = pytz.timezone("Europe/Rome")


def now_cet() -> datetime:
    return datetime.now(CET)


def to_cet(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return CET.localize(dt)
    return dt.astimezone(CET)


def format_cet(dt: datetime) -> str:
    return to_cet(dt).strftime("%Y-%m-%d %H:%M:%S CET")
