import { Link } from "react-router-dom";

export const UserTr = ({ user }) => {
  const gender = user.gender === "male" ? "Мужской" : "Женский";

  return (
    <tr class="border-t border-t-[#cfdbe7]">
      <td class="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        <Link
          to={`/${user.id}`}
          className="hover:text-[var(--color-primary)] hover:underline"
        >
          {user.name}
        </Link>
      </td>
      <td class="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.lastName}
      </td>
      <td class="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">{gender}</td>
      <td class="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.phoneNumber}
      </td>
      <td class="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.email}
      </td>
      <td class="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.address}
      </td>
      <td class="h-[72px] px-4 py-2 w-14 text-sm font-normal">
        <img
          src={user.photo}
          alt={user.name}
          className="rounded-full"
        />
      </td>
    </tr>
  );
};
