import React, { useState } from "react";
import { useAuth } from "../hooks/useAuth";
import api from "../services/api";

export default function ProfilePage() {
  const { user, setUser } = useAuth();
  const [name, setName] = useState(user?.name || "");
  const [hourlyRate, setHourlyRate] = useState(user?.hourly_rate || "");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSave = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);
    setSaving(true);
    try {
      const payload = {};
      if (name !== user?.name) payload.name = name;
      if (Number(hourlyRate) !== user?.hourly_rate) payload.hourly_rate = Number(hourlyRate);
      if (Object.keys(payload).length === 0) {
        setSaving(false);
        return;
      }
      const res = await api.put("/api/v1/developers/profile", payload);
      setUser(res.data);
      setSuccess(true);
    } catch {
      setError("Failed to update profile");
    } finally {
      setSaving(false);
    }
  };

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
        </div>
        <form onSubmit={handleSave}>
          <div className="profile-field">
            <label>Name</label>
            <input className="input" value={name} onChange={(e) => setName(e.target.value)} required />
          </div>
          <div className="profile-field">
            <label>Email</label>
            <input className="input" value={user?.email || ""} readOnly />
          </div>
          <div className="profile-field">
            <label>Hourly Rate (&euro;/h)</label>
            <input className="input" type="number" step="0.01" min="0" value={hourlyRate} onChange={(e) => setHourlyRate(e.target.value)} required />
          </div>
          {error && <div className="login-error">{error}</div>}
          {success && <div style={{ color: "var(--green)", marginBottom: 12 }}>Profile updated successfully.</div>}
          <button className="btn btn-primary" type="submit" disabled={saving}>
            {saving ? "Saving..." : "Save Changes"}
          </button>
        </form>
      </div>
    </div>
  );
}
