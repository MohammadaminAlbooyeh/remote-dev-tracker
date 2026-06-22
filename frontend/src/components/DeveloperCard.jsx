import React from "react";
import OnlineBadge from "./OnlineBadge";

export default function DeveloperCard({ developer }) {
  return (
    <div className="dev-item">
      <div className="dev-item-left">
        <OnlineBadge isOnline={developer.is_online} />
        <span className="dev-item-name">{developer.name}</span>
      </div>
      <span className="dev-item-rate">&euro;{developer.hourly_rate}/h</span>
    </div>
  );
}
