import api from "./api";

export const adminApi = {
  developers: {
    list: () => api.get("/api/v1/admin/developers"),
    create: (data) => api.post("/api/v1/admin/developers", data),
    update: (id, data) => api.put(`/api/v1/admin/developers/${id}`, data),
    deactivate: (id) => api.delete(`/api/v1/admin/developers/${id}`),
  },
  sessions: {
    list: () => api.get("/api/v1/admin/sessions"),
  },
  summary: () => api.get("/api/v1/admin/summary"),
  exportCsv: () => api.get("/api/v1/admin/export/csv", { responseType: "blob" }),
};
