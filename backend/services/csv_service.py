import csv
import io
from backend.models.session import Session
from backend.models.user import User
from backend.utils.timezone import to_cet


class CSVService:
    def __init__(self, db):
        self.db = db

    def export_user_csv(self, developer_id, start=None, end=None):
        query = self.db.query(Session).filter(
            Session.developer_id == developer_id,
            Session.status == "completed",
        )
        if start:
            query = query.filter(Session.start_time >= start)
        if end:
            query = query.filter(Session.start_time <= end)
        sessions = query.order_by(Session.start_time).all()
        return self._generate_csv(sessions)

    def export_all_csv(self):
        sessions = (
            self.db.query(Session)
            .filter(Session.status == "completed")
            .order_by(Session.start_time)
            .all()
        )
        return self._generate_csv(sessions, include_developer=True)

    def _generate_csv(self, sessions, include_developer=False):
        output = io.StringIO()
        writer = csv.writer(output)

        if include_developer:
            writer.writerow(
                ["Developer Name", "Date", "Start Time (CET)", "End Time (CET)", "Hours", "Rate (€/h)", "Amount (€)"]
            )
        else:
            writer.writerow(["Date", "Start Time (CET)", "End Time (CET)", "Hours", "Rate (€/h)", "Amount (€)"])

        total_hours = 0.0
        total_amount = 0.0
        dev_cache = {}

        for s in sessions:
            developer_name = ""
            if include_developer:
                if s.developer_id not in dev_cache:
                    user = self.db.query(User).filter(User.id == s.developer_id).first()
                    dev_cache[s.developer_id] = user.name if user else "Unknown"
                developer_name = dev_cache[s.developer_id]

            row = [
                to_cet(s.start_time).strftime("%Y-%m-%d"),
                to_cet(s.start_time).strftime("%H:%M"),
                to_cet(s.end_time).strftime("%H:%M") if s.end_time else "",
                f"{float(s.duration or 0):.2f}",
                f"{float(s.amount or 0) / float(s.duration or 1):.2f}" if s.duration else "0.00",
                f"{float(s.amount or 0):.2f}",
            ]
            if include_developer:
                row.insert(0, developer_name)
            writer.writerow(row)

            total_hours += float(s.duration or 0)
            total_amount += float(s.amount or 0)

        writer.writerow([])
        writer.writerow(["TOTAL", "", "", "", f"{total_hours:.2f}", "", f"{total_amount:.2f}"])

        return output.getvalue()
