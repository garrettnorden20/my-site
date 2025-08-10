from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "my-site"
    debug: bool = False
    database_url: str = Field(default="sqlite:///./data.db")
    secret_key: str = Field(default="change-me")

    model_config = SettingsConfigDict(env_file=".env")


def get_settings() -> Settings:
    return Settings()


settings = get_settings()
