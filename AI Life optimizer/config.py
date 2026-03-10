import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = "development"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    DATABASE_URL: str = "sqlite:///./data/aio_life_optimizer.db"

    # External connectors (placeholders)
    GOOGLE_CALENDAR_API_KEY: str | None = None
    GOOGLE_OAUTH_CLIENT_ID: str | None = None
    GOOGLE_OAUTH_CLIENT_SECRET: str | None = None

    FITBIT_CLIENT_ID: str | None = None
    FITBIT_CLIENT_SECRET: str | None = None

    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
