from pydantic import BaseSettings


class Config(BaseSettings):
    # API
    MIGRATIONS_DIR: str = "migrations"
    TESTING: bool = False

    # DB
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "apidb"
    DB_USER: str = "api"
    DB_PASS: str = "passpass"

    class Config:
        case_sensitive = True
