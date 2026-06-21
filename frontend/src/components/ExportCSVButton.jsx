import React from "react";

export default function ExportCSVButton() {
  const handleExport = () => {
    window.location.href = "/api/v1/reports/export/csv";
  };

  return <button onClick={handleExport}>Export CSV</button>;
}
