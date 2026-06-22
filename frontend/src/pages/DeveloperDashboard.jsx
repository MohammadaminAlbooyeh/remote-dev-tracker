import React, { useState, useEffect } from "react";
import { useAuth } from "../hooks/useAuth";
import Timer from "../components/Timer";
import SummaryCard from "../components/SummaryCard";
import SessionList from "../components/SessionList";
import { reportApi } from "../services/report_api";

export default function DeveloperDashboard() {
  const { user } = useAuth();
  const [summary, setSummary] = useState({ today: 0, week: 0, month: 0, todayAmount: 0, weekAmount: 0, monthAmount: 0 });

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return;
    Promise.all([
      reportApi.get("daily"),
      reportApi.get("weekly"),
      reportApi.get("monthly"),
    ])
      .then(([daily, weekly, monthly]) => {
        setSummary({
          today: daily.data.summary?.total_hours ?? 0,
          week: weekly.data.summary?.total_hours ?? 0,
          month: monthly.data.summary?.total_hours ?? 0,
          todayAmount: daily.data.summary?.total_amount ?? 0,
          weekAmount: weekly.data.summary?.total_amount ?? 0,
          monthAmount: monthly.data.summary?.total_amount ?? 0,
        });
      })
      .catch(() => {});
  }, []);

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
          <SummaryCard
            today={summary.today}
            week={summary.week}
            month={summary.month}
            todayAmount={summary.todayAmount}
            weekAmount={summary.weekAmount}
            monthAmount={summary.monthAmount}
          />
        </div>
        <div className="card">
          <SessionList />
        </div>
      </div>
    </div>
  );
}
