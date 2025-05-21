from typing import Annotated
from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db.helper import db_helper
from app.services.random_user.random_api import RandomUserAPI


def get_random_api(request: Request) -> RandomUserAPI:
    return request.app.state.random_api


DependsSession = Annotated[AsyncSession, Depends(db_helper.session_getter)]
DependsRandomAPI = Annotated[RandomUserAPI, Depends(get_random_api)]
