import { apiClient } from "../api/client";

export class UserService {
  static async getUsers(page = 1, size = 10) {
    const response = await apiClient.get("/users", {
      params: { page: page, size: size },
    });
    return response.data;
  }

  static async getUserById(id) {
    const response = await apiClient.get(`/users/${id}`);
    return response.data;
  }

  static async getRandomUser() {
    const response = await apiClient.get("/users/random");
    return response.data;
  }

  static async addUsers(count) {
    const response = await apiClient.post("/users", { count: count });
    return response.data;
  }
}
