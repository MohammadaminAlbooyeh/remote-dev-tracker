import React from "react";
import OnlineBadge from "./OnlineBadge";

export default function DeveloperCard({ developer }) {
  return (
    <div>
      <OnlineBadge isOnline={developer.is_online} />
      <span>{developer.name}</span>
      <span>€{developer.hourly_rate}/h</span>
    </div>
  );
}
