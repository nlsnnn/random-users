import { Link } from "react-router-dom";

export const Header = () => {
  return (
    <header className="flex justify-center items-center p-4 border-[#e7edf4] border-b-2">
      <div>
        <Link
          to="/"
          className="text-xl text-dark font-bold hover:text-blue-500 transition duration-300"
        >
          Random Users
        </Link>
      </div>
    </header>
  );
};
