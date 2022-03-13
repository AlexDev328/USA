import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "HlGEozzPG4PR27QbpNDK-XT4SPv9PRr9C3kbS4WTx7E"  # secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    PROJECT_NAME: str
    USERS_OPEN_REGISTRATION: bool

    SERVER_HOST: str

    BACKEND_CORS_ORIGINS: list[Union[str, AnyHttpUrl]] = ['http://localhost:8080']

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    EMAILS_ENABLED: bool
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int
    EMAILS_FROM_NAME: str
    EMAILS_FROM_EMAIL: str
    EMAIL_TEMPLATES_DIR: str
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_TLS: bool
    SMTP_USER: str
    SMTP_PASSWORD: str

    class Config:
        env_file = "/run/media/carolus/WD/Projects/Python/USA_AGAIN/.env"
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()
