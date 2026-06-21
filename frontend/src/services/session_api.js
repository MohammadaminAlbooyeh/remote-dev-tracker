import api from "./api";

export const sessionApi = {
  clockIn: () => api.post("/api/v1/sessions/clock-in"),
  clockOut: (note) => api.post("/api/v1/sessions/clock-out", { note }),
  list: () => api.get("/api/v1/sessions"),
  active: () => api.get("/api/v1/sessions/active"),
  get: (id) => api.get(`/api/v1/sessions/${id}`),
};
