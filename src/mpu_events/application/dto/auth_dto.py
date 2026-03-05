from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from mpu_events.domain.entities.user import UserRole


class RegisterUserDTO(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    group_number: str | None = None


class LoginUserDTO(BaseModel):
    email: EmailStr
    password: str


class AuthTokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponseDTO(BaseModel):
    id: UUID
    email: str
    full_name: str
    group_number: str | None
    role: UserRole
    created_at: datetime

    model_config = {"from_attributes": True}