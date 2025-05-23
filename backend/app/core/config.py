from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    url: str
    pool_size: int = 50
    max_overflow: int = 10


class RandomUserAPIConfig(BaseModel):
    url: str = "https://randomuser.me/api/"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("app/.env.example", "app/.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APPLICATION__",
    )

    db: DatabaseConfig
    random_user_api: RandomUserAPIConfig


settings = Settings()
