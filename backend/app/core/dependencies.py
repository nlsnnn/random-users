from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db.helper import db_helper


DependsSession = Annotated[AsyncSession, Depends(db_helper.session_getter)]
