import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { observer } from "mobx-react-lite";
import { userStore } from "../../store/userStore";
import { Header } from "../UI/Header";

export const User = observer(({ isRandom = false }) => {
  const { userId } = useParams();

  useEffect(() => {
    if (isRandom) {
      document.title = "Случайный пользователь";
      userStore.getRandomUser();
    } else {
      document.title = `Пользователь ${userId}`;
      userStore.getUserById(userId);
    }
  }, [isRandom, userId]);

  if (userStore.isLoading) {
    return (
      <>
        <Header />
        <main className="container mx-auto px-4 py-8">
          <p>Загрузка...</p>
        </main>
      </>
    );
  }

  if (userStore.error) {
    return (
      <>
        <Header />
        <main className="bg-gray-50">
          <div className="container mx-auto px-4 py-8">
            <div className="text-red-600">
              <p>
                Не удалось получить данные:{" "}
                {userStore.error.message || userStore.error}
              </p>
              <button
                className="mt-4 px-4 py-2 bg-blue-500 text-white rounded-full hover:bg-blue-600 transition duration-300 cursor-pointer"
                onClick={() => {
                  if (isRandom) userStore.getRandomUser();
                  else userStore.getUserById(userId);
                }}
              >
                Повторить
              </button>
            </div>
          </div>
        </main>
      </>
    );
  }

  if (!userStore.user) {
    return null;
  }

  const { id, name, lastName, gender, phoneNumber, email, address, photo } =
    userStore.user;

  return (
    <>
      <Header />
      <main className="bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <h1 className="text-3xl font-bold mb-4">
            {isRandom ? "Случайный пользователь" : `Пользователь #${id}`}
          </h1>
          <div className="bg-white shadow rounded-lg p-6 flex flex-col md:flex-row items-center gap-6">
            <img src={photo} alt={name} className="w-32 h-32 rounded-full" />
            <div className="space-y-2 text-sm text-gray-700">
              <p>
                <strong>Имя:</strong> {name}
              </p>
              <p>
                <strong>Фамилия:</strong> {lastName}
              </p>
              <p>
                <strong>Пол:</strong>{" "}
                {gender === "male" ? "Мужской" : "Женский"}
              </p>
              <p>
                <strong>Телефон:</strong> {phoneNumber}
              </p>
              <p>
                <strong>Email:</strong> {email}
              </p>
              <p>
                <strong>Адрес:</strong> {address}
              </p>
            </div>
          </div>
        </div>
      </main>
    </>
  );
});
