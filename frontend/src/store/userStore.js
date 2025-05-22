import { makeAutoObservable } from "mobx";
import { UserService } from "../service/userService";

class UserStore {
  users = [];
  user = null;
  page = 1;
  size = 6;
  totalPages = 0;

  constructor() {
    makeAutoObservable(this);
  }

  async getUsers(page = 1) {
    const data = await UserService.getUsers(page, this.size);
    this.page = page;
    this.totalPages = data.total;
    this.users = data.items;
  }

  async getUserById(id) {
    const data = await UserService.getUserById(id);
    this.user = data;
  }

  async getRandomUser() {
    const data = await UserService.getRandomUser();
    this.user = data;
  }

  async addUsers(count) {
    const data = await UserService.addUsers(count);
    this.users = [...this.users, ...data];
  }
}

export const userStore = new UserStore();
