from backend.models.session import Session
from backend.utils.timezone import now_cet, to_cet
from datetime import timedelta


class ReportService:
    def __init__(self, db):
        self.db = db

    def _query_sessions(self, developer_id, start, end):
        return (
            self.db.query(Session)
            .filter(
                Session.developer_id == developer_id,
                Session.start_time >= start,
                Session.start_time <= end,
                Session.status == "completed",
            )
            .order_by(Session.start_time.desc())
            .all()
        )

    def get_daily_report(self, developer_id):
        now = now_cet()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        sessions = self._query_sessions(developer_id, start, now)
        return self._build_report(sessions)

    def get_weekly_report(self, developer_id):
        now = now_cet()
        start = now - timedelta(days=now.weekday())
        start = start.replace(hour=0, minute=0, second=0, microsecond=0)
        sessions = self._query_sessions(developer_id, start, now)
        return self._build_report(sessions)

    def get_monthly_report(self, developer_id):
        now = now_cet()
        start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        sessions = self._query_sessions(developer_id, start, now)
        return self._build_report(sessions)

    def get_custom_report(self, developer_id, start_date, end_date):
        start = to_cet(start_date)
        end = to_cet(end_date).replace(hour=23, minute=59, second=59)
        sessions = self._query_sessions(developer_id, start, end)
        return self._build_report(sessions)

    def get_all_sessions(self):
        return self.db.query(Session).order_by(Session.start_time.desc()).all()

    def get_global_summary(self):
        sessions = self.db.query(Session).filter(Session.status == "completed").all()
        total_hours = sum(float(s.duration or 0) for s in sessions)
        total_amount = sum(float(s.amount or 0) for s in sessions)
        return {"total_hours": round(total_hours, 2), "total_amount": round(total_amount, 2)}

    def _build_report(self, sessions):
        total_hours = sum(float(s.duration or 0) for s in sessions)
        total_amount = sum(float(s.amount or 0) for s in sessions)
        return {
            "sessions": [
                {
                    "id": s.id,
                    "date": to_cet(s.start_time).strftime("%Y-%m-%d"),
                    "start_time": to_cet(s.start_time).strftime("%H:%M"),
                    "end_time": to_cet(s.end_time).strftime("%H:%M") if s.end_time else None,
                    "hours": float(s.duration or 0),
                    "amount": float(s.amount or 0),
                    "note": s.note,
                }
                for s in sessions
            ],
            "summary": {
                "total_sessions": len(sessions),
                "total_hours": round(total_hours, 2),
                "total_amount": round(total_amount, 2),
            },
        }
