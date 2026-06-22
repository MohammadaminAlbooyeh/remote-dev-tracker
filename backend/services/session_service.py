from backend.models.session import Session
from backend.models.user import User
from backend.services.payment_service import calculate_session_payment
from backend.utils.timezone import now_cet, to_cet


class SessionService:
    def __init__(self, db):
        self.db = db

    def clock_in(self, developer_id: str):
        active = self.get_active_session(developer_id)
        if active:
            raise ValueError("Already clocked in")
        session = Session(
            developer_id=developer_id,
            start_time=now_cet(),
            status="active",
        )
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def clock_out(self, developer_id: str, note: str = None):
        session = self.get_active_session(developer_id)
        if not session:
            raise ValueError("No active session")
        user = self.db.query(User).filter(User.id == developer_id).first()
        end_time = now_cet()
        start_time = to_cet(session.start_time)
        payment = calculate_session_payment(start_time, end_time, float(user.hourly_rate))
        session.end_time = end_time
        session.duration = payment["duration_hours"]
        session.amount = payment["amount"]
        session.status = "completed"
        session.note = note
        self.db.commit()
        self.db.refresh(session)
        return session

    def get_user_sessions(self, developer_id: str, skip: int = 0, limit: int = 100):
        return (
            self.db.query(Session)
            .filter(Session.developer_id == developer_id)
            .order_by(Session.start_time.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_active_session(self, developer_id: str):
        return (
            self.db.query(Session)
            .filter(
                Session.developer_id == developer_id,
                Session.status == "active",
            )
            .first()
        )

    def get_session(self, session_id: str, developer_id: str):
        return (
            self.db.query(Session)
            .filter(Session.id == session_id, Session.developer_id == developer_id)
            .first()
        )
