import jwt
from datetime import datetime, timedelta, UTC
from uuid import UUID
from mpu_events.config import settings
from mpu_events.domain.entities.user import UserRole
from mpu_events.domain.exceptions.exceptions import UnauthorizedException


class TokenService:
    def create_access_token(self, user_id: UUID, role: UserRole) -> str:
        payload = {
            "sub": str(user_id),
            "role": role.value,
            "exp": datetime.now(UTC) + timedelta(hours=settings.jwt_expires_hours),
        }
        return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")

    def decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise UnauthorizedException("Token expired")
        except jwt.InvalidTokenError:
            raise UnauthorizedException("Invalid token")