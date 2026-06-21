import React from "react";

export default function SessionCard({ session }) {
  return (
    <div>
      <p>{session.date}</p>
      <p>{session.start_time} - {session.end_time}</p>
      <p>{session.hours}h — €{session.amount}</p>
    </div>
  );
}
