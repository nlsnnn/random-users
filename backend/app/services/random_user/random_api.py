import aiohttp

from app.services.random_user.exceptions import RandomUserException
from app.services.random_user.schemas import RandomUser


class RandomUserAPI:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._session: aiohttp.ClientSession | None = None

    async def init_session(self):
        if self._session is None:
            self._session = aiohttp.ClientSession(base_url=self._base_url)

    async def close_session(self):
        if self._session is not None:
            await self._session.close()

    async def fetch_random_users(self, count: int = 1) -> list[RandomUser]:
        await self.init_session()
        async with self._session.get("", params={"results": count}) as response:
            if response.status != 200:
                raise RandomUserException(f"HTTP {response.status}")
            data = await response.json()
            return [RandomUser.model_validate(u) for u in data["results"]]
