import { useState, useEffect } from "react";
import { reportApi } from "../services/report_api";

export function useReport() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(true);
  const [period, setPeriod] = useState("daily");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const fetchReport = async (p) => {
    const token = localStorage.getItem("token");
    if (!token) {
      setLoading(false);
      return;
    }
    setLoading(true);
    try {
      const res = await reportApi.get(p);
      setReport(res.data);
    } catch {
      // handled
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchReport(period);
  }, [period]);

  const fetchCustom = async () => {
    if (!startDate || !endDate) return;
    setLoading(true);
    try {
      const res = await reportApi.custom(startDate, endDate);
      setReport(res.data);
    } catch {
      // handled
    } finally {
      setLoading(false);
    }
  };

  return { report, loading, period, setPeriod, startDate, endDate, setStartDate, setEndDate, fetchCustom };
}
