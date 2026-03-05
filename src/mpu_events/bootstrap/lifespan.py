from contextlib import asynccontextmanager
from fastapi import FastAPI
from mpu_events.config import settings
from mpu_events.infra.database.manager import DatabaseManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = DatabaseManager(
        database_url=settings.DATABASE_URL,
        echo=settings.DEBUG,
    )
    app.state.db = db

    yield

    await db.close()