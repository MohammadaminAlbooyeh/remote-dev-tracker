import React, { useState } from "react";

export default function DateRangePicker({ onFilter }) {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");

  const handleApply = () => {
    if (onFilter) onFilter(start, end);
  };

  return (
    <div>
      <input type="date" value={start} onChange={(e) => setStart(e.target.value)} />
      <input type="date" value={end} onChange={(e) => setEnd(e.target.value)} />
      <button onClick={handleApply}>Apply</button>
    </div>
  );
}
