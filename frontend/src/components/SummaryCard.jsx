import React from "react";

export default function SummaryCard({ today = 0, week = 0, month = 0, todayAmount = 0, weekAmount = 0, monthAmount = 0 }) {
  return (
    <div className="summary-grid">
      <div className="summary-item">
        <div className="summary-item-label">Today</div>
        <div className="summary-item-hours">{today.toFixed(1)}h</div>
        <div className="summary-item-amount">&euro;{todayAmount.toFixed(2)}</div>
      </div>
      <div className="summary-item">
        <div className="summary-item-label">This Week</div>
        <div className="summary-item-hours">{week.toFixed(1)}h</div>
        <div className="summary-item-amount">&euro;{weekAmount.toFixed(2)}</div>
      </div>
      <div className="summary-item">
        <div className="summary-item-label">This Month</div>
        <div className="summary-item-hours">{month.toFixed(1)}h</div>
        <div className="summary-item-amount">&euro;{monthAmount.toFixed(2)}</div>
      </div>
    </div>
  );
}
