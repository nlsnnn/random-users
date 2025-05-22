import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { observer } from "mobx-react-lite";
import { userStore } from "../../store/userStore";
import { Header } from "../UI/Header";

export const User = observer(({ isRandom = false }) => {
  const { userId } = useParams();

  useEffect(() => {
    userStore.user = null;

    if (isRandom) {
      document.title = "Случайный пользователь";
      userStore.getRandomUser();
    } else {
      document.title = `Пользователь ${userId}`;
      userStore.getUserById(userId);
    }
  }, [isRandom, userId]);

  if (!userStore.user) {
    return (
      <>
        <Header />
        <main className="container mx-auto px-4 py-8">
          <p>Загрузка...</p>
        </main>
      </>
    );
  }

  const { id, name, lastName, gender, phoneNumber, email, address, photo } =
    userStore.user;

  return (
    <>
      <Header />
      <main className="container mx-auto px-4 py-8">
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
              <strong>Пол:</strong> {gender === "male" ? "Мужской" : "Женский"}
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
      </main>
    </>
  );
});
