import { useState, useEffect } from "react";
import { sessionApi } from "../services/session_api";

export function useSessions() {
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    sessionApi
      .list()
      .then((res) => setSessions(res.data))
      .finally(() => setLoading(false));
  }, []);

  return { sessions, loading };
}
