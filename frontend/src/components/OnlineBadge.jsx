import React from "react";

export default function OnlineBadge({ isOnline }) {
  return (
    <span className={`online-dot ${isOnline ? "online" : "offline"}`} />
  );
}
