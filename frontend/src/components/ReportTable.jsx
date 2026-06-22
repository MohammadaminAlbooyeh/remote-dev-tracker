import React from "react";

export default function ReportTable({ report }) {
  if (!report || !report.sessions || report.sessions.length === 0) {
    return <div className="empty-state">No data for the selected period.</div>;
  }

  return (
    <table className="reports-table">
      <thead>
        <tr>
          <th>Date</th>
          <th>Hours</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        {report.sessions.map((s, i) => (
          <tr key={i}>
            <td>{s.date || s.start_time ? new Date(s.start_time || s.date).toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short", year: "numeric" }) : "—"}</td>
            <td>{s.hours ?? s.duration ? `${Number(s.hours ?? s.duration).toFixed(1)}h` : "—"}</td>
            <td>{s.amount ? `€${Number(s.amount).toFixed(2)}` : "—"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
