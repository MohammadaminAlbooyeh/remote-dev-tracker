import React, { createContext, useState, useEffect } from "react";
import { authApi } from "../services/auth_api";

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      authApi
        .me()
        .then((res) => setUser(res.data))
        .catch(() => localStorage.removeItem("token"))
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (email, password) => {
    setError(null);
    try {
      const res = await authApi.login(email, password);
      localStorage.setItem("token", res.data.access_token);
      const meRes = await authApi.me();
      setUser(meRes.data);
    } catch (err) {
      const msg =
        err.response?.data?.detail || err.response?.data?.message || "Login failed. Please check your credentials.";
      setError(msg);
      throw err;
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, error, login, logout, setError, setUser }}>
      {children}
    </AuthContext.Provider>
  );
}
