import { observer } from "mobx-react-lite";
import { userStore } from "../../store/userStore";
import {
  MdOutlineKeyboardArrowLeft,
  MdOutlineKeyboardArrowRight,
  MdFirstPage,
  MdLastPage,
} from "react-icons/md";

export const Pagination = observer(() => {
  const { page, totalPages } = userStore;

  const getPageNumbers = () => {
    if (totalPages <= 3) {
      return Array.from({ length: totalPages }, (_, i) => i + 1);
    }
    if (page === 1) return [1, 2, 3];
    if (page === totalPages)
      return [totalPages - 2, totalPages - 1, totalPages];
    return [page - 1, page, page + 1];
  };

  return (
    <div className="mt-6">
      <div className="flex justify-center items-center">
        <button
          className="text-xl rounded-full cursor-pointer mx-1"
          onClick={() => userStore.getUsers(1)}
          disabled={page === 1}
          title="Первая страница"
        >
          <MdFirstPage className="text-2xl" />
        </button>

        <button
          className="text-xl rounded-full cursor-pointer mx-1"
          onClick={() => userStore.getUsers(page - 1)}
          disabled={page === 1}
          title="Предыдущая страница"
        >
          <MdOutlineKeyboardArrowLeft className="text-2xl" />
        </button>

        {getPageNumbers().map((num) => (
          <button
            key={num}
            className={`mx-1 px-4 py-2 rounded-full ${
              page === num
                ? "bg-[var(--color-muted)] text-white"
                : "bg-gray-200 text-black hover:bg-[var(--color-border)] hover:text-[var(--color-muted)] cursor-pointer"
            } transition duration-300`}
            onClick={() => userStore.getUsers(num)}
            disabled={page === num}
          >
            {num}
          </button>
        ))}

        <button
          className="text-xl rounded-full cursor-pointer mx-1"
          onClick={() => userStore.getUsers(page + 1)}
          disabled={page === totalPages}
          title="Следующая страница"
        >
          <MdOutlineKeyboardArrowRight className="text-2xl" />
        </button>

        <button
          className="text-xl rounded-full cursor-pointer mx-1"
          onClick={() => userStore.getUsers(totalPages)}
          disabled={page === totalPages}
          title="Последняя страница"
        >
          <MdLastPage className="text-2xl" />
        </button>
      </div>
    </div>
  );
});
