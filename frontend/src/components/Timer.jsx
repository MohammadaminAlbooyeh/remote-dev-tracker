import React from "react";
import { useTimer } from "../hooks/useTimer";

export default function Timer() {
  const { elapsed, isRunning, clockIn, clockOut } = useTimer();

  return (
    <div>
      <h2>{elapsed}</h2>
      {isRunning ? (
        <button onClick={clockOut}>CLOCK OUT</button>
      ) : (
        <button onClick={clockIn}>CLOCK IN</button>
      )}
    </div>
  );
}
