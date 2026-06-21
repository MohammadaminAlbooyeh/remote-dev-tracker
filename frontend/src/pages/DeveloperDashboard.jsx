import React from "react";
import Timer from "../components/Timer";
import SummaryCard from "../components/SummaryCard";
import SessionList from "../components/SessionList";

export default function DeveloperDashboard() {
  return (
    <div>
      <h1>Developer Dashboard</h1>
      <Timer />
      <SummaryCard />
      <SessionList />
    </div>
  );
}
