import { UserTr } from "./UserTr";

export const PeopleTable = ({ users }) => {
  return (
    <table className="w-full border-collapse border border-gray-200 ">
      <thead>
        <tr class="bg-slate-50">
          <th class="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Имя
          </th>
          <th class="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Фамилия
          </th>
          <th class="px-4 py-3 text-left  text-dark w-[400px] text-sm font-medium">
            Пол
          </th>
          <th class="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Номер телефона
          </th>
          <th class="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Email
          </th>
          <th class="px-4 py-3 text-left text-dark w-[400px] text-sm font-medium">
            Адрес
          </th>
          <th class="px-4 py-3 text-left text-dark w-14 text-sm font-medium leading-normal">
            Фото
          </th>
        </tr>
      </thead>
      <tbody>
        <UserTr
          user={{
            name: "test",
            lastName: "test",
            gender: "male",
            phoneNumber: "555-1234",
            email: "test@example.com",
            address: "123 Main St",
            photo: "https://via.placeholder.com/150",
          }}
        />
      </tbody>
    </table>
  );
};
