from databases import Database

from src.config import Config

config = Config()

connection_string = (
    f"postgresql://{config.DB_USER}:{config.DB_PASS}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
)
db = Database(connection_string, force_rollback=config.TESTING)
