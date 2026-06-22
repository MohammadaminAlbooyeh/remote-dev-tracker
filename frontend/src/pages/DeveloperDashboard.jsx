import React from "react";
import { useAuth } from "../hooks/useAuth";
import Timer from "../components/Timer";
import SummaryCard from "../components/SummaryCard";
import SessionList from "../components/SessionList";

export default function DeveloperDashboard() {
  const { user } = useAuth();

  return (
    <div className="page">
      <h1>Developer Dashboard</h1>
      <div className="dashboard-grid">
        <div className="card">
          <div className="card-header">
            <h2>Time Tracker</h2>
            <span className="badge badge-active">Active</span>
          </div>
          <Timer />
        </div>
        <div className="card">
          <div className="card-header">
            <h2>Summary</h2>
            <span className="badge badge-dev">&euro;{user?.hourly_rate}/h</span>
          </div>
          <SummaryCard />
        </div>
        <div className="card">
          <SessionList />
        </div>
      </div>
    </div>
  );
}
