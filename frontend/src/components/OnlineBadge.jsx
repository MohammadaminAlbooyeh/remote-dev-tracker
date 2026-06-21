import React from "react";

export default function OnlineBadge({ isOnline }) {
  return (
    <span style={{ color: isOnline ? "green" : "red" }}>
      {isOnline ? "ONLINE" : "OFFLINE"}
    </span>
  );
}
