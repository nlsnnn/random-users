import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.create_fastapi_app import create_app
from app.core.db.helper import db_helper
from app.core.dependencies import get_random_api
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
    class DummyAPI:
        async def fetch_random_users(self, count):
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

            return [DummyUser(i) for i in range(count)]

    return DummyAPI()


@pytest_asyncio.fixture
async def async_client(monkeypatch, db_session, dummy_random_api):
    async def noop_check_and_fill_db(app):
        return

    monkeypatch.setattr("app.utils.db_start.check_and_fill_db", noop_check_and_fill_db)

    app = create_app()

    async def _get_test_db():
        yield db_session

    app.dependency_overrides[db_helper.session_getter] = _get_test_db
    app.dependency_overrides[get_random_api] = lambda: dummy_random_api

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
