import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    STUDENT = "student"
    ADMIN = "admin"


@dataclass
class User:
    email: str
    full_name: str
    hashed_password: str

    group_number: str | None = None
    role: UserRole = UserRole.STUDENT
    id: uuid.UUID | None = None
    created_at: datetime | None = None

    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN