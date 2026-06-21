import { useState, useCallback } from "react";
import api from "../services/api";

export function useAPI(url, method = "get") {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const execute = useCallback(
    async (body = null) => {
      setLoading(true);
      setError(null);
      try {
        const res = await api[method](url, body);
        setData(res.data);
        return res.data;
      } catch (err) {
        setError(err);
        throw err;
      } finally {
        setLoading(false);
      }
    },
    [url, method]
  );

  return { data, loading, error, execute };
}
