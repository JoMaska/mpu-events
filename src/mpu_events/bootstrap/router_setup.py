from fastapi import FastAPI
from mpu_events.presentation.fastapi.api.v1.router import create_v1_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(create_v1_router())