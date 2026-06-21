import { useState, useEffect, useContext } from "react";
import { TimerContext } from "../context/TimerContext";

export function useTimer() {
  const ctx = useContext(TimerContext);
  if (!ctx) {
    throw new Error("useTimer must be used within TimerProvider");
  }

  const [elapsed, setElapsed] = useState("00:00:00");
  const { isRunning, startTime, clockIn, clockOut, activeSession } = ctx;

  useEffect(() => {
    if (!isRunning || !startTime) {
      setElapsed("00:00:00");
      return;
    }
    const interval = setInterval(() => {
      const diff = Math.floor((Date.now() - new Date(startTime).getTime()) / 1000);
      const h = String(Math.floor(diff / 3600)).padStart(2, "0");
      const m = String(Math.floor((diff % 3600) / 60)).padStart(2, "0");
      const s = String(diff % 60).padStart(2, "0");
      setElapsed(`${h}:${m}:${s}`);
    }, 1000);
    return () => clearInterval(interval);
  }, [isRunning, startTime]);

  return { elapsed, isRunning, clockIn, clockOut, activeSession };
}
