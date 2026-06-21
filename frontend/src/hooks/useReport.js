import { useState, useEffect } from "react";
import { reportApi } from "../services/report_api";

export function useReport(period = "daily") {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    reportApi
      .get(period)
      .then((res) => setReport(res.data))
      .finally(() => setLoading(false));
  }, [period]);

  return { report, loading };
}
