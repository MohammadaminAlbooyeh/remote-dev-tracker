import React from "react";
import DateRangePicker from "../components/DateRangePicker";
import ReportTable from "../components/ReportTable";
import ExportCSVButton from "../components/ExportCSVButton";

export default function ReportsPage() {
  return (
    <div>
      <h1>Reports</h1>
      <DateRangePicker />
      <ReportTable />
      <ExportCSVButton />
    </div>
  );
}
