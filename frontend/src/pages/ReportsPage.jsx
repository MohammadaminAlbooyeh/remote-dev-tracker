import React from "react";
import DateRangePicker from "../components/DateRangePicker";
import ReportTable from "../components/ReportTable";
import ExportCSVButton from "../components/ExportCSVButton";
import { useReport } from "../hooks/useReport";
import LoadingSpinner from "../components/LoadingSpinner";

export default function ReportsPage() {
  const { report, loading, period, setPeriod, startDate, endDate, setStartDate, setEndDate, fetchCustom } = useReport();

  return (
    <div className="page">
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 24 }}>
        <h1 style={{ margin: 0 }}>Reports</h1>
        <ExportCSVButton />
      </div>
      <div className="card">
        <DateRangePicker
          period={period}
          onPeriodChange={setPeriod}
          startDate={startDate}
          endDate={endDate}
          onStartDateChange={setStartDate}
          onEndDateChange={setEndDate}
          onCustomFetch={fetchCustom}
        />
        {loading ? <LoadingSpinner /> : <ReportTable report={report} />}
      </div>
    </div>
  );
}
