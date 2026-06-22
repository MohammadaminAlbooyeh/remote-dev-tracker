import React from "react";

const periods = [
  { value: "daily", label: "Daily" },
  { value: "weekly", label: "Weekly" },
  { value: "monthly", label: "Monthly" },
];

export default function DateRangePicker({ period, onPeriodChange, startDate, endDate, onStartDateChange, onEndDateChange, onCustomFetch }) {
  return (
    <div className="date-range">
      <div className="date-range-field">
        <label>Period</label>
        <select className="input" value={period} onChange={(e) => onPeriodChange(e.target.value)}>
          {periods.map((p) => (
            <option key={p.value} value={p.value}>{p.label}</option>
          ))}
        </select>
      </div>
      <div className="date-range-field">
        <label>From</label>
        <input className="input" type="date" value={startDate} onChange={(e) => onStartDateChange(e.target.value)} />
      </div>
      <div className="date-range-field">
        <label>To</label>
        <input className="input" type="date" value={endDate} onChange={(e) => onEndDateChange(e.target.value)} />
      </div>
      <button className="btn btn-outline" onClick={onCustomFetch} disabled={!startDate || !endDate}>
        Apply
      </button>
    </div>
  );
}
