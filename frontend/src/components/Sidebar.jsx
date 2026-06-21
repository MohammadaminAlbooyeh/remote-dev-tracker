import React from "react";
import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <nav>
      <Link to="/dashboard">Dashboard</Link>
      <Link to="/reports">Reports</Link>
      <Link to="/admin">Admin</Link>
      <Link to="/profile">Profile</Link>
    </nav>
  );
}
