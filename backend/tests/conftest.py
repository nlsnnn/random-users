import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.create_fastapi_app import create_app
from app.core.dependencies import DependsSession, DependsRandomAPI
from app.core.models.base import Base


@pytest_asyncio.fixture
async def db_session():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with session_maker() as session:
        yield session


@pytest_asyncio.fixture
def dummy_random_api():
    from app.services.random_user.schemas import RandomUser

    class DummyAPI:
        async def fetch_random_users(self, count):
            return [
                RandomUser(
                    name="E",
                    last_name="L",
                    gender="male",
                    phone_number="555",
                    email=f"user{i}@ex.com",
                    address="Addr",
                    photo="pic",
                )
                for i in range(count)
            ]

    return DummyAPI()


@pytest_asyncio.fixture
async def async_client(db_session, dummy_random_api):
    app = create_app()

    async def _get_test_db():
        yield db_session

    app.dependency_overrides[DependsSession] = _get_test_db
    app.dependency_overrides[DependsRandomAPI] = lambda: dummy_random_api

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
