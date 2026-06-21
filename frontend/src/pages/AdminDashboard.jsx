import React from "react";
import DeveloperList from "../components/DeveloperList";
import SummaryCard from "../components/SummaryCard";
import ExportCSVButton from "../components/ExportCSVButton";

export default function AdminDashboard() {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <SummaryCard />
      <DeveloperList />
      <ExportCSVButton />
    </div>
  );
}
