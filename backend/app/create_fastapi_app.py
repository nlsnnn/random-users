from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.random_user.random_api import RandomUserAPI
from app.core.config import settings
from app.api import register_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await app.state.random_api.init_session()
    yield
    await app.state.random_api.close_session()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    app.state.random_api = RandomUserAPI(base_url=settings.random_user_api.url)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_routers(app)

    return app
