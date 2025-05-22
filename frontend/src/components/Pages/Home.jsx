import { AddPerson } from "../Features/AddPerson/AddPerson";
import { PeopleTable } from "../Features/Table/PeopleTable";
import { Header } from "../UI/Header";

export const Home = () => {
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
          <PeopleTable />
        </div>
      </main>
    </>
  );
};
