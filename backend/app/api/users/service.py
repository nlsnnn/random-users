from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.users import (
    get_all_users,
    get_user_by_id,
    get_users_paginated,
    create_user,
)
from app.core.schemas.user import UserCreate, UserRead
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
        return await get_user_by_id(db, user_id)

    @staticmethod
    async def create_user(db: AsyncSession, user_data: UserCreate):
        return await create_user(db, user_data)

    @staticmethod
    async def get_random_user(random_api: RandomUserAPI, db: AsyncSession):
        user = (await random_api.fetch_random_users(1))[0]
        await create_user(db, UserCreate.model_validate(user.model_dump()))
        return user
