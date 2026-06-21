import React from "react";
import SessionCard from "./SessionCard";
import { useSessions } from "../hooks/useSessions";

export default function SessionList() {
  const { sessions } = useSessions();

  return (
    <div>
      <h3>Recent Sessions</h3>
      {sessions.map((s) => (
        <SessionCard key={s.id} session={s} />
      ))}
    </div>
  );
}
