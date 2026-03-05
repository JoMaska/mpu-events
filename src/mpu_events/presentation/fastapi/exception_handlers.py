from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mpu_events.domain.exceptions.exceptions import (
    EventNotFoundException,
    AlreadyRegisteredException,
    EventFullException,
    UnauthorizedException,
    EmailAlreadyExistsException,
    UserNotFoundException,
)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(EventNotFoundException)
    async def event_not_found(request, exc):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(UserNotFoundException)
    async def user_not_found(request, exc):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(EmailAlreadyExistsException)
    async def email_exists(request, exc):
        return JSONResponse(status_code=409, content={"detail": str(exc)})

    @app.exception_handler(AlreadyRegisteredException)
    async def already_registered(request, exc):
        return JSONResponse(status_code=409, content={"detail": "Вы уже записаны на это событие"})

    @app.exception_handler(EventFullException)
    async def event_full(request, exc):
        return JSONResponse(status_code=409, content={"detail": "Мест больше нет"})

    @app.exception_handler(UnauthorizedException)
    async def unauthorized(request, exc):
        return JSONResponse(status_code=401, content={"detail": str(exc)})