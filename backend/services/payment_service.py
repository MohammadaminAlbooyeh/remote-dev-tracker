from datetime import datetime


def calculate_session_payment(
    start_time: datetime,
    end_time: datetime,
    hourly_rate: float,
) -> dict:
    duration_seconds = (end_time - start_time).total_seconds()
    duration_hours = round(duration_seconds / 3600, 2)
    amount = round(duration_hours * hourly_rate, 2)

    return {
        "duration_hours": duration_hours,
        "hourly_rate": hourly_rate,
        "amount": amount,
    }
