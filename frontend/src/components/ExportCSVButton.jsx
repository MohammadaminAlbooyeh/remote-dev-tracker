import React from "react";
import { reportApi } from "../services/report_api";

export default function ExportCSVButton() {
  const handleExport = async () => {
    try {
      const res = await reportApi.exportCsv();
      const url = window.URL.createObjectURL(new Blob([res.data]));
      const a = document.createElement("a");
      a.href = url;
      a.download = "report.csv";
      a.click();
      window.URL.revokeObjectURL(url);
    } catch {
      // handled by axios interceptor
    }
  };

  return <button onClick={handleExport}>Export CSV</button>;
}
