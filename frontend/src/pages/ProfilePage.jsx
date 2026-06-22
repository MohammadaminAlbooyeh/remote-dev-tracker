import React, { useState } from "react";
import { useAuth } from "../hooks/useAuth";

export default function ProfilePage() {
  const { user } = useAuth();

  return (
    <div className="page">
      <h1>Profile</h1>
      <div className="card profile-card">
        <div className="profile-row">
          <div className="profile-stat">
            <div className="profile-stat-label">Role</div>
            <div className="profile-stat-value">
              <span className={`badge ${user?.role === "admin" ? "badge-admin" : "badge-dev"}`}>
                {user?.role}
              </span>
            </div>
          </div>
          <div className="profile-stat">
            <div className="profile-stat-label">Hourly Rate</div>
            <div className="profile-stat-value">&euro;{user?.hourly_rate}/h</div>
          </div>
        </div>
        <div className="profile-field">
          <label>Name</label>
          <input className="input" value={user?.name || ""} readOnly />
        </div>
        <div className="profile-field">
          <label>Email</label>
          <input className="input" value={user?.email || ""} readOnly />
        </div>
      </div>
    </div>
  );
}
