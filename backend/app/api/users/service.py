from sqlalchemy.ext.asyncio import AsyncSession

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
        return UserRead.model_validate(user)

    @staticmethod
    async def add_users(
        random_api: RandomUserAPI, db: AsyncSession, data: UserCreateRequest
    ):
        items = await random_api.fetch_random_users(data.count)
        users = [UserCreate.model_validate(user.model_dump()) for user in items]
        return await add_users(db, users)

    @staticmethod
    async def get_random_user(random_api: RandomUserAPI, db: AsyncSession):
        user = (await random_api.fetch_random_users(1))[0]
        await create_user(db, UserCreate.model_validate(user.model_dump()))
        return UserRead.model_validate(user.model_dump())
