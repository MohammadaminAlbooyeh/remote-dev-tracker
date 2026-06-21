import api from "./api";

export const authApi = {
  login: (email, password) => api.post("/api/v1/auth/login", { email, password }),
  register: (data) => api.post("/api/v1/auth/register", data),
  me: () => api.get("/api/v1/auth/me"),
  logout: () => api.post("/api/v1/auth/logout"),
};
