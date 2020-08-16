from fastapi import FastAPI
from migri import apply_migrations, get_connection

from src.config import Config
from src.db import db
from src.quote import views as quote_views

config = Config()
app = FastAPI()
app.include_router(quote_views.router, prefix="/quotes")


@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.on_event("startup")
async def set_up_db():
    # Run migrations
    conn = get_connection(
        config.DB_NAME,
        config.DB_USER,
        config.DB_PASS,
        config.DB_HOST,
        config.DB_PORT
    )
    await apply_migrations(config.MIGRATIONS_DIR, conn)

    # Connect to db
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
