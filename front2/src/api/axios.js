import axios from "axios";

// Instance Axios centralisée pour communiquer avec l'API Flask
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:5000/api",
  headers: {
    "Content-Type": "application/json",
  },
  // 5 minutes : l'analyse (clone + IA + build MkDocs) peut légitimement
  // dépasser 60s. Valeur précédente (6 000 000 ms = 100 min) était une
  // faute de frappe.
  timeout: 3000000,
});

// Injecte automatiquement le token d'authentification si présent
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Gestion centralisée des erreurs (ex: session expirée)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem("token");
      localStorage.removeItem("user");
      if (window.location.pathname !== "/login") {
        window.location.href = "/login";
      }
    }
    return Promise.reject(error);
  }
);

export default api;

