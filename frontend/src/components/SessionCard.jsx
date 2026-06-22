import React from "react";

export default function SessionCard({ session }) {
  const startDate = session.start_time
    ? new Date(session.start_time).toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "short" })
    : "";
  const startTime = session.start_time
    ? new Date(session.start_time).toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" })
    : "";
  const endTime = session.end_time
    ? new Date(session.end_time).toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" })
    : "";

  return (
    <div className="session-item">
      <div className="session-item-left">
        <span className="session-item-date">{startDate}</span>
        <span className="session-item-time">
          {startTime} &mdash; {endTime || "ongoing"}
          {session.note && <span> &middot; {session.note}</span>}
        </span>
      </div>
      <div className="session-item-right">
        <div className="session-item-hours">
          {session.duration ? `${Number(session.duration).toFixed(1)}h` : "—"}
        </div>
        <div className="session-item-amount">
          {session.amount ? `€${Number(session.amount).toFixed(2)}` : "—"}
        </div>
      </div>
    </div>
  );
}
