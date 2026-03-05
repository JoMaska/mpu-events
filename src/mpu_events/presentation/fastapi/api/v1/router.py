from fastapi import APIRouter
from .routes import auth, events, registrations


def create_v1_router() -> APIRouter:
    router = APIRouter(prefix="/api/v1")
    router.include_router(auth.router)
    router.include_router(events.router)
    router.include_router(registrations.router)
    return router