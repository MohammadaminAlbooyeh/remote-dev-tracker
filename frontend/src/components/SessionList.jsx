import React from "react";
import SessionCard from "./SessionCard";
import { useSessions } from "../hooks/useSessions";
import LoadingSpinner from "./LoadingSpinner";

export default function SessionList() {
  const { sessions, loading } = useSessions();

  return (
    <>
      <div className="card-header">
        <h3>Recent Sessions</h3>
        {sessions.length > 0 && <span className="badge badge-completed">{sessions.length} sessions</span>}
      </div>
      {loading ? (
        <LoadingSpinner />
      ) : sessions.length === 0 ? (
        <div className="empty-state">No sessions yet. Clock in to start tracking.</div>
      ) : (
        <div className="session-list">
          {sessions.map((s) => (
            <SessionCard key={s.id} session={s} />
          ))}
        </div>
      )}
    </>
  );
}
