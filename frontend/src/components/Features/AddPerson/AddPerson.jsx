export const AddPerson = () => {
  return (
    <div className="flex flex-col container mx-auto py-8 gap-4">
      <input
        type="text"
        placeholder="Введите кол-во"
        className="p-[15px] flex w-full min-w-0 h-14 flex-1 text-muted bg-slate-50 resize-none overflow-hidden rounded-xl focus:outline-0 focus:ring-0 border border-[var(--color-border)] focus:border-[var(--color-border)] placeholder:text-[var(--color-border)]"
      />
      <button className="flex min-w-[84px] max-w-[480px] bg-[var(--color-primary)] h-10 px-4 text-white text-sm font-bold cursor-pointer items-center justify-center overflow-hidden rounded-full hover:bg-[var(--color-muted)] transition duration-300">
        Добавить
      </button>
    </div>
  );
};
