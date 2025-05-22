import pytest
from sqlalchemy.exc import IntegrityError

from app.crud.users import (
    get_user_by_id,
    get_users_paginated,
    create_user,
    add_users,
)
from app.core.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_and_get_user(db_session):
    dto = UserCreate(
        name="John",
        last_name="Doe",
        gender="male",
        phone_number="123",
        email="john@mail.com",
        address="Mir St",
        photo="http://",
    )
    user = await create_user(db_session, dto)
    assert user.id is not None
    fetched = await get_user_by_id(db_session, user.id)
    assert fetched.email == dto.email


@pytest.mark.asyncio
async def test_get_user_not_found(db_session):
    assert await get_user_by_id(db_session, 999) is None


@pytest.mark.asyncio
async def test_pagination(db_session):
    for i in range(5):
        await create_user(
            db_session,
            UserCreate(
                name="E",
                last_name="L",
                gender="x",
                phone_number="0",
                email=f"{i}@x.com",
                address="a",
                photo="p",
            ),
        )
    items, total = await get_users_paginated(db_session, skip=0, limit=2)
    assert len(items) == 2
    assert total == 5


@pytest.mark.asyncio
async def test_add_users_and_integrity(db_session):
    users = [
        UserCreate(
            name="A",
            last_name="B",
            gender="X",
            phone_number="0",
            email=f"{i}@x.com",
            address="st",
            photo="pic",
        )
        for i in range(2)
    ]
    result = await add_users(db_session, users)
    assert result == users

    with pytest.raises(IntegrityError):
        await add_users(db_session, users)
