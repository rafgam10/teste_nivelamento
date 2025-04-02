import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000", // Mude a porta conforme necessário
});

export default api;
