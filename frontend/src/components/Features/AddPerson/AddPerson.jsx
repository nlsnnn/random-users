import { useState } from "react";
import { userStore } from "../../../store/userStore";

export const AddPerson = () => {
  const [count, setCount] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const value = e.target.value;

    if (/^\d*$/.test(value) && Number(value) <= 500) {
      setCount(value);
      setError("");
    } else {
      setError("Введите только положительное число (меньше 500)");
    }
  };

  const handleAdd = async () => {
    const num = Number(count);
    if (!num || num < 1) {
      setError("Введите число больше 0");
      return;
    }
    setError("");
    await userStore.addUsers(num);
    setCount("");
  };

  return (
    <div className="flex flex-col container mx-auto py-8 gap-4">
      <input
        type="number"
        min="1"
        max="500"
        placeholder="Введите кол-во"
        className="p-[15px] flex w-full min-w-0 h-14 flex-1 text-muted bg-slate-50 resize-none overflow-hidden rounded-xl focus:outline-0 focus:ring-0 border border-[var(--color-border)] focus:border-[var(--color-border)] placeholder:text-[var(--color-border)]"
        value={count}
        onChange={handleChange}
      />
      {error && <div className="text-red-500">{error}</div>}
      <button
        onClick={handleAdd}
        className="flex min-w-[84px] max-w-[480px] bg-[var(--color-primary)] h-10 px-4 text-white text-sm font-bold cursor-pointer items-center justify-center overflow-hidden rounded-full hover:bg-[var(--color-muted)] transition duration-300"
        disabled={!count || !!error}
      >
        Добавить
      </button>
    </div>
  );
};
