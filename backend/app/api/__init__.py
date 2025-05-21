from fastapi import APIRouter, FastAPI
from app.api.users.router import router as users_router


def register_routers(app: FastAPI):
    root_router = APIRouter()

    @root_router.get("/ping")
    async def ping():
        return {"message": "Pong!"}

    app.include_router(root_router)
    app.include_router(users_router)
