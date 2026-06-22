import React, { useState, useEffect } from "react";
import SummaryCard from "../components/SummaryCard";
import DeveloperList from "../components/DeveloperList";
import ExportCSVButton from "../components/ExportCSVButton";
import { adminApi } from "../services/admin_api";

export default function AdminDashboard() {
  const [globalSummary, setGlobalSummary] = useState(null);

  useEffect(() => {
    adminApi
      .summary()
      .then((res) => setGlobalSummary(res.data))
      .catch(() => {});
  }, []);

  return (
    <div className="page">
      <h1>Admin Dashboard</h1>
      <div className="admin-grid">
        <div className="card">
          <div className="card-header">
            <h2>Platform Summary</h2>
          </div>
          {globalSummary ? (
            <SummaryCard
              today={globalSummary.total_hours || 0}
              week={globalSummary.total_hours || 0}
              month={globalSummary.total_hours || 0}
              todayAmount={globalSummary.total_amount || 0}
              weekAmount={globalSummary.total_amount || 0}
              monthAmount={globalSummary.total_amount || 0}
            />
          ) : (
            <SummaryCard />
          )}
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
