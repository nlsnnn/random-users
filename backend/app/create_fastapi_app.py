from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.random_user.random_api import RandomUserAPI
from app.core.config import settings
from app.api import register_routers
from app.utils.db_start import check_and_fill_db
from app.api.error_handlers import register_error_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await app.state.random_api.init_session()
    await check_and_fill_db(app)
    yield
    await app.state.random_api.close_session()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.state.random_api = RandomUserAPI(base_url=settings.random_user_api.url)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",  # dev
            "http://localhost",  # prod
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_error_handlers(app)
    register_routers(app)

    return app
