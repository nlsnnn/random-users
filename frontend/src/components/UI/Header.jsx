import { Link } from "react-router-dom";

export const Header = () => {
  return (
    <header className="border-[#e7edf4] border-b-2">
      <div className="container mx-auto flex justify-between items-center p-4">
        <div>
          <Link
            to="/"
            className="text-xl text-dark font-bold hover:text-blue-500 transition duration-300"
          >
            Random Users
          </Link>
        </div>
        <div>
          <Link
            to="/random"
            className="ml-4 text-sm text-gray-500 hover:text-blue-500 transition duration-300"
          >
            Случайный пользователь
          </Link>
        </div>
      </div>
    </header>
  );
};
