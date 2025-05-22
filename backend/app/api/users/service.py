from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.crud.users import (
    get_all_users,
    get_user_by_id,
    get_users_paginated,
    create_user,
    add_users,
)
from app.core.schemas.user import UserCreate, UserRead, UserCreateRequest
from app.services.random_user import RandomUserAPI
from app.core.schemas.pagination import Pagination
from app.core.exceptions import UsersException


class UserService:
    @staticmethod
    async def get_all_users(db: AsyncSession):
        return await get_all_users(db)

    @staticmethod
    async def get_users_paginated(db: AsyncSession, page: int = 1, size: int = 50):
        skip = max(page - 1, 0) * size
        limit = size
        items, total = await get_users_paginated(db, skip=skip, limit=limit)

        users = [UserRead.model_validate(user) for user in items]
        return Pagination(page=page, size=size, total=total, items=users)

    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int):
        user = await get_user_by_id(db, user_id)
        if not user:
            raise UsersException(
                message=f"Пользователь с ID {user_id} не найден",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return UserRead.model_validate(user)

    @staticmethod
    async def add_users(
        random_api: RandomUserAPI, db: AsyncSession, data: UserCreateRequest
    ):
        try:
            items = await random_api.fetch_random_users(data.count)
            users = [UserCreate.model_validate(user.model_dump()) for user in items]
            return await add_users(db, users)
        except IntegrityError:
            raise UsersException(
                message="Уменьшите кол-во загружаемых пользователей или попробуйте позже",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    @staticmethod
    async def get_random_user(random_api: RandomUserAPI, db: AsyncSession):
        try:
            user = (await random_api.fetch_random_users(1))[0]
            orm_user = await create_user(
                db, UserCreate.model_validate(user.model_dump())
            )
            return UserRead.model_validate(orm_user)
        except IntegrityError:
            raise UsersException(
                message="Не получилось добавить пользователя. Попробуйте еще раз",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
