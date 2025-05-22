import { Link } from "react-router-dom";

export const UserTr = ({ user }) => {
  const gender = user.gender === "male" ? "Мужской" : "Женский";

  return (
    <tr className="border-t border-t-[#cfdbe7]">
      <td className="h-[72px] px-4 py-2 w-[400px] text-dark text-sm">
        <Link
          to={`/${user.id}`}
          className="hover:text-[var(--color-primary)] hover:underline"
        >
          {user.name}
        </Link>
      </td>
      <td className="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.lastName}
      </td>
      <td className="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">{gender}</td>
      <td className="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.phoneNumber}
      </td>
      <td className="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.email}
      </td>
      <td className="h-[72px] px-4 py-2 w-[400px] text-muted text-sm">
        {user.address}
      </td>
      <td className="h-[72px] px-4 py-2 w-14 text-sm font-normal">
        <img
          src={user.photo}
          alt={user.name}
          className="rounded-full"
        />
      </td>
    </tr>
  );
};
