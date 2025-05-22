import pytest


@pytest.mark.asyncio
async def test_list_empty(async_client):
    res = await async_client.get("/users/")
    assert res.status_code == 200
    data = res.json()
    assert data["total"] == 0
    assert data["items"] == []


@pytest.mark.asyncio
async def test_add_and_get_user(async_client):
    post_res = await async_client.post("/users/", json={"count": 1})
    assert post_res.status_code == 200
    lst = post_res.json()
    assert isinstance(lst, list) and len(lst) == 1

    user = lst[0]

    get_res = await async_client.get("/users/1")
    assert get_res.status_code == 200
    assert get_res.json()["email"] == user["email"]


@pytest.mark.asyncio
async def test_get_not_found(async_client):
    res = await async_client.get("/users/1")
    assert res.status_code == 404
    assert res.json()["message"] == "Пользователь с ID 1 не найден"
