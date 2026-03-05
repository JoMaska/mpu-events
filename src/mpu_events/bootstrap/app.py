from fastapi import FastAPI
from mpu_events.bootstrap.lifespan import lifespan
from mpu_events.bootstrap.router_setup import setup_routers
from mpu_events.bootstrap.exception_setup import setup_exceptions
from mpu_events.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        lifespan=lifespan,
    )
    setup_routers(app)
    setup_exceptions(app)
    return app