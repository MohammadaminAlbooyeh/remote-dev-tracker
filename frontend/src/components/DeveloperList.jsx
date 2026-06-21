import React from "react";
import DeveloperCard from "./DeveloperCard";

export default function DeveloperList() {
  const developers = [];

  return (
    <div>
      <h3>All Developers</h3>
      {developers.map((dev) => (
        <DeveloperCard key={dev.id} developer={dev} />
      ))}
    </div>
  );
}
