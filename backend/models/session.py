import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Numeric, DateTime, ForeignKey
from backend.models.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    developer_id = Column(String, ForeignKey("users.id"), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=True)
    duration = Column(Numeric(10, 2), nullable=True)
    amount = Column(Numeric(10, 2), nullable=True)
    note = Column(Text, nullable=True)
    status = Column(String(10), default="active")
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
