import { useEffect } from "react";
import { AddPerson } from "../Features/AddPerson/AddPerson";
import { PeopleTable } from "../Features/Table/PeopleTable";
import { Header } from "../UI/Header";
import { userStore } from "../../store/userStore";
import { observer } from "mobx-react-lite";
import { Pagination } from "../Features/Pagination";

export const Home = observer(() => {
  useEffect(() => {
    document.title = "Главная страница";
    userStore.getUsers(userStore.page);
  }, []);

  return (
    <>
      <Header />
      <main className="bg-gray-50 h-screen">
        <div className="flex flex-col container mx-auto px-4 py-8">
          <h1 className="text-4xl font-bold text-gray-800">
            Список пользователей
          </h1>
          <div>
            <AddPerson />
          </div>
          <div className="flex flex-col gap-4">
            <PeopleTable />
            <Pagination />
          </div>
        </div>
      </main>
    </>
  );
});
