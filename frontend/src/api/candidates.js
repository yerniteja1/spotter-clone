import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api",
});

export const candidateApi = {
  list: (params = {}) => api.get("/candidates/", { params }),

  get: (id) => api.get(`/candidates/${id}/`),

  create: (data) => api.post("/candidates/", data),

  update: (id, data) => api.put(`/candidates/${id}/`, data),

  remove: (id) => api.delete(`/candidates/${id}/`),

  stats: () => api.get("/candidates/stats/"),
};
