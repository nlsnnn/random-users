import pytest
from sqlalchemy.exc import IntegrityError

from app.api.users.service import UserService
from app.core.schemas.user import UserCreateRequest
from app.core.exceptions import UsersException


class DummyAPI:
    class DummyUser:
        def __init__(self, idx: int):
            self.name = "E"
            self.last_name = "L"
            self.gender = "male"
            self.phone_number = "555"
            self.email = f"user{idx}@ex.com"
            self.address = "Addr"
            self.photo = "pic"

        def model_dump(self) -> dict:
            return {
                "name": self.name,
                "last_name": self.last_name,
                "gender": self.gender,
                "phone_number": self.phone_number,
                "email": self.email,
                "address": self.address,
                "photo": self.photo,
            }

    async def fetch_random_users(self, count):
        return [DummyAPI.DummyUser(i) for i in range(count)]


@pytest.mark.asyncio
async def test_get_random_user_success(db_session):
    user_read = await UserService.get_random_user(DummyAPI(), db_session)
    assert user_read.email.endswith("@ex.com")
    assert hasattr(user_read, "id")


@pytest.mark.asyncio
async def test_get_random_user_integrity(monkeypatch, db_session):
    async def fake_create(*args, **kwargs):
        raise IntegrityError("msg", "params", "orig")

    monkeypatch.setattr("app.api.users.service.create_user", fake_create)
    with pytest.raises(UsersException) as ei:
        await UserService.get_random_user(DummyAPI(), db_session)
    assert "Не получилось добавить пользователя" in ei.value.message
    assert 400 == ei.value.status_code


@pytest.mark.asyncio
async def test_add_users_success(db_session):
    req = UserCreateRequest(count=3)
    lst = await UserService.add_users(DummyAPI(), db_session, req)
    assert isinstance(lst, list) and len(lst) == 3


@pytest.mark.asyncio
async def test_add_users_integrity(monkeypatch, db_session):
    async def fake_add(db, users):
        raise IntegrityError("msg", "params", "orig")

    monkeypatch.setattr("app.api.users.service.add_users", fake_add)
    with pytest.raises(UsersException) as ei:
        await UserService.add_users(DummyAPI(), db_session, UserCreateRequest(count=1))
    assert "Уменьшите кол-во загружаемых пользователей" in ei.value.message
    assert 400 == ei.value.status_code
