import React from "react";
import { useAuth } from "../hooks/useAuth";

export default function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="header">
      <div className="header-brand">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10" />
          <polyline points="12 6 12 12 16 14" />
        </svg>
        Remote Dev Tracker
      </div>
      {user && (
        <div className="header-right">
          <span className="header-user">
            <strong>{user.name}</strong> &middot; €{user.hourly_rate}/h
          </span>
          <button className="btn btn-outline" onClick={logout}>
            Logout
          </button>
        </div>
      )}
    </header>
  );
}
