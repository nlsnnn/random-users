from typing import Sequence
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import User
from app.core.schemas.user import UserCreate


async def get_all_users(db: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_users_paginated(
    db: AsyncSession, *, skip: int = 0, limit: int = 50
) -> tuple[list[User], int]:
    q = select(User).offset(skip).limit(limit)
    result = await db.execute(q)
    items = result.scalars().all()

    total = await db.scalar(select(func.count()).select_from(User))
    return items, total


async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    user = User(**user_data.model_dump())
    db.add(user)
    await db.commit()
    return user
