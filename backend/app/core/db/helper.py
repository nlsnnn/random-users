from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, pool_size: int = 5, max_overflow: int = 10):
        self.engine = create_async_engine(
            url=url,
            echo=False,
            echo_pool=False,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_maker = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_maker() as session:
            try:
                yield session
            except Exception as e:
                await session.rollback()
                raise e


db_helper = DatabaseHelper(
    url=settings.db.url,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
