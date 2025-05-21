from fastapi import FastAPI
from sqlalchemy import func, select

from app.core.db import db_helper
from app.core.models import User
from app.core.schemas.user import UserCreate


async def check_and_fill_db(app: FastAPI):
    async with db_helper.session_maker() as session:
        stmt = select(func.count()).select_from(User)
        total: int = await session.scalar(stmt)
        if total:
            return

        random_users = await app.state.random_api.fetch_random_users(count=3000)

        unique_by_email: dict = {}
        for user in random_users:
            if user.email not in unique_by_email:
                unique_by_email[user.email] = user
                if len(unique_by_email) >= 1000:
                    break

        users_to_add = []
        for user in unique_by_email.values():
            dto = UserCreate.model_validate(user.model_dump())
            users_to_add.append(User(**dto.model_dump()))

        session.add_all(users_to_add)
        await session.commit()
