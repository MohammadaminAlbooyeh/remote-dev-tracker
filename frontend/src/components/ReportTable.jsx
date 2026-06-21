import React from "react";
import { useReport } from "../hooks/useReport";

export default function ReportTable() {
  const { report } = useReport();

  return (
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Hours</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        {report?.sessions?.map((s, i) => (
          <tr key={i}>
            <td>{s.date}</td>
            <td>{s.hours}</td>
            <td>€{s.amount}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
