import React from "react";
import { useTimer } from "../hooks/useTimer";

export default function Timer() {
  const { elapsed, isRunning, clockIn, clockOut } = useTimer();

  return (
    <div className="timer-display">
      <div className="timer-time">{elapsed}</div>
      <div className="timer-controls">
        {isRunning ? (
          <button className="timer-button timer-button-clockout" onClick={clockOut} title="Clock out">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="6" y="6" width="12" height="12" rx="2" />
            </svg>
          </button>
        ) : (
          <button className="timer-button timer-button-clockin" onClick={clockIn} title="Clock in">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <polygon points="5 3 19 12 5 21 5 3" />
            </svg>
          </button>
        )}
      </div>
    </div>
  );
}
