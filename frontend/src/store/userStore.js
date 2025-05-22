import { makeAutoObservable, runInAction } from "mobx";
import { UserService } from "../service/userService";

class UserStore {
  users = [];
  user = null;
  page = 1;
  size = 6;
  totalPages = 0;
  error = null;
  isLoading = false;

  constructor() {
    makeAutoObservable(this);
  }

  async getUsers(page = 1) {
    runInAction(() => {
      this.isLoading = true;
      this.error = null;
    });
    try {
      const data = await UserService.getUsers(page, this.size);
      runInAction(() => {
        this.page = page;
        this.totalPages = Math.ceil(data.total / this.size);
        this.users = data.items;
      });
    } catch (e) {
      runInAction(() => {
        if (e.response?.status === 404) {
          this.error = "Пользователи не найдены";
        } else {
          this.error = "Ошибка загрузки пользователей";
        }
      });
    } finally {
      runInAction(() => {
        this.isLoading = false;
      });
    }
  }

  async getUserById(id) {
    runInAction(() => {
      this.isLoading = true;
      this.error = null;
    });
    try {
      const data = await UserService.getUserById(id);
      runInAction(() => {
        this.user = data;
      });
    } catch (e) {
      runInAction(() => {
        if (e.response?.status === 404) {
          this.error = "Пользователь не найден";
        } else {
          this.error = "Ошибка загрузки пользователя";
        }
      });
    } finally {
      runInAction(() => {
        this.isLoading = false;
      });
    }
  }

  async getRandomUser() {
    runInAction(() => {
      this.isLoading = true;
      this.error = null;
      this.user = null;
    });
    try {
      const data = await UserService.getRandomUser();
      runInAction(() => {
        this.user = data;
      });
    } catch (e) {
      runInAction(() => {
        this.error =
          "Ошибка загрузки случайного пользователя. Попробуйте еще раз.";
      });
    } finally {
      runInAction(() => {
        this.isLoading = false;
      });
    }
  }

  async addUsers(count) {
    runInAction(() => {
      this.isLoading = true;
      this.error = null;
    });
    try {
      const data = await UserService.addUsers(count);
      runInAction(() => {
        this.users = [...this.users, ...data];
      });
    } catch (e) {
      runInAction(() => {
        this.error = "Ошибка добавления пользователей";
      });
    } finally {
      runInAction(() => {
        this.isLoading = false;
      });
    }
  }
}

export const userStore = new UserStore();
