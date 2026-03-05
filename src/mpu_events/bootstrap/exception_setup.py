from fastapi import FastAPI
from mpu_events.presentation.fastapi.exception_handlers import register_exception_handlers


def setup_exceptions(app: FastAPI) -> None:
    register_exception_handlers(app)