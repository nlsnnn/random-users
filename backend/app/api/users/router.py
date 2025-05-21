from fastapi import APIRouter, Query

from app.core.dependencies import DependsSession, DependsRandomAPI
from app.api.users.service import UserService
from app.core.schemas.user import UserCreate


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def list_users(
    db: DependsSession, page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200)
):
    return await UserService.get_users_paginated(db, page, size)


@router.get("/random")
async def get_random_user(random_api: DependsRandomAPI, db: DependsSession):
    return await UserService.get_random_user(random_api, db)


@router.get("/{user_id}")
async def get_user(user_id: int, db: DependsSession):
    return await UserService.get_user_by_id(db, user_id)


@router.post("/")
async def create_user(user_data: UserCreate, db: DependsSession):
    return await UserService.create_user(db, user_data)
