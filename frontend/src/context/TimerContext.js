import React, { createContext, useState, useEffect } from "react";
import { sessionApi } from "../services/session_api";

export const TimerContext = createContext(null);

export function TimerProvider({ children }) {
  const [isRunning, setIsRunning] = useState(false);
  const [startTime, setStartTime] = useState(null);
  const [activeSession, setActiveSession] = useState(null);

  useEffect(() => {
    sessionApi
      .active()
      .then((res) => {
        if (res.data) {
          setActiveSession(res.data);
          setStartTime(res.data.start_time);
          setIsRunning(true);
        }
      })
      .catch(() => {});
  }, []);

  const clockIn = async () => {
    const res = await sessionApi.clockIn();
    setActiveSession(res.data);
    setStartTime(res.data.start_time);
    setIsRunning(true);
  };

  const clockOut = async () => {
    const res = await sessionApi.clockOut();
    setActiveSession(null);
    setStartTime(null);
    setIsRunning(false);
    return res.data;
  };

  return (
    <TimerContext.Provider value={{ isRunning, startTime, activeSession, clockIn, clockOut }}>
      {children}
    </TimerContext.Provider>
  );
}
