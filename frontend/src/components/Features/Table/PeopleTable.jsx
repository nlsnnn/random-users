import { observer } from "mobx-react-lite";
import { UserTr } from "./UserTr";
import { userStore } from "../../../store/userStore";

export const PeopleTable = observer(() => {
  if (!userStore.users.length) return "Загрузка...";

  return (
    <table className="w-full border-collapse border border-gray-200 ">
      <thead>
        <tr className="bg-slate-50">
          <th className="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Имя
          </th>
          <th className="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Фамилия
          </th>
          <th className="px-4 py-3 text-left  text-dark w-[400px] text-sm font-medium">
            Пол
          </th>
          <th className="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Номер телефона
          </th>
          <th className="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Email
          </th>
          <th className="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Адрес
          </th>
          <th className="px-4 py-3 text-left text-dark w-14 text-sm font-medium leading-normal">
            Фото
          </th>
        </tr>
      </thead>
      <tbody>
        {userStore.users.map((user) => (
          <UserTr key={user.id} user={user} />
        ))}
      </tbody>
    </table>
  );
});
