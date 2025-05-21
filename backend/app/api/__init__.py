from fastapi import APIRouter, FastAPI


def register_routers(app: FastAPI):
    root_router = APIRouter()

    @root_router.get("/ping")
    async def ping():
        return {"message": "Pong!"}

    app.include_router(root_router)
