import React from "react";
import { useAPI } from "../hooks/useAPI";
import LoadingSpinner from "./LoadingSpinner";

export default function DeveloperList() {
  const { data: developers, loading } = useAPI("/api/v1/admin/developers", "get", true);

  if (loading) return <LoadingSpinner />;

  if (!developers || developers.length === 0) {
    return <div className="empty-state">No developers found.</div>;
  }

  return (
    <div className="dev-list">
      {developers.map((dev) => (
        <div key={dev.id} className="dev-item">
          <div className="dev-item-left">
            <span className={`online-dot ${dev.is_online ? "online" : "offline"}`} />
            <span className="dev-item-name">{dev.name}</span>
          </div>
          <span className="dev-item-rate">&euro;{dev.hourly_rate}/h</span>
        </div>
      ))}
    </div>
  );
}
