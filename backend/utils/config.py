from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/remote_dev_tracker"
    secret_key: str = "change-me-to-a-random-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 480
    app_name: str = "Remote Dev Tracker"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    timezone: str = "Europe/Rome"
    cors_origins: List[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()
