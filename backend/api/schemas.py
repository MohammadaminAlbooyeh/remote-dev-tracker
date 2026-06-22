from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    hourly_rate: float


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str
    hourly_rate: float
    is_active: bool
    is_online: bool = False

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    hourly_rate: Optional[float] = None


class SessionResponse(BaseModel):
    id: str
    developer_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    duration: Optional[float] = None
    amount: Optional[float] = None
    note: Optional[str] = None
    status: str

    class Config:
        from_attributes = True


class ClockInResponse(BaseModel):
    id: str
    start_time: datetime
    status: str


class ClockOutRequest(BaseModel):
    note: Optional[str] = None


class ReportEntry(BaseModel):
    date: str
    start_time: str
    end_time: str
    hours: float
    rate: float
    amount: float
