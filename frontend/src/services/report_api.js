import api from "./api";

export const reportApi = {
  get: (period) => api.get(`/api/v1/reports/${period}`),
  custom: (start, end) => api.get("/api/v1/reports/custom", { params: { start, end } }),
  exportCsv: () => api.get("/api/v1/reports/export/csv", { responseType: "blob" }),
};
