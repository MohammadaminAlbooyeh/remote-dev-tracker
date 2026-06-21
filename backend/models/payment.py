from pydantic import BaseModel
from datetime import datetime


class PaymentCalculation(BaseModel):
    duration_hours: float
    hourly_rate: float
    amount: float
