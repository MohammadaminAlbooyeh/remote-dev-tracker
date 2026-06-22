import React from "react";
import DeveloperList from "../components/DeveloperList";
import SummaryCard from "../components/SummaryCard";
import ExportCSVButton from "../components/ExportCSVButton";

export default function AdminDashboard() {
  return (
    <div className="page">
      <h1>Admin Dashboard</h1>
      <div className="admin-grid">
        <div className="card">
          <div className="card-header">
            <h2>Platform Summary</h2>
          </div>
          <SummaryCard />
        </div>
        <div className="card">
          <div className="card-header">
            <h2>Export</h2>
          </div>
          <ExportCSVButton />
        </div>
        <div className="card">
          <div className="card-header">
            <h2>All Developers</h2>
          </div>
          <DeveloperList />
        </div>
      </div>
    </div>
  );
}
