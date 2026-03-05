import uuid
from mpu_events.domain.entities.user import User, UserRole
from mpu_events.infra.database.models.user_model import UserModel


class UserMapper:
    @staticmethod
    def to_entity(model: UserModel) -> User:
        return User(
            id=model.id,
            email=model.email,
            full_name=model.full_name,
            group_number=model.group_number,
            hashed_password=model.hashed_password,
            role=UserRole(model.role),
            created_at=model.created_at,
        )

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id or uuid.uuid4(),
            email=entity.email,
            full_name=entity.full_name,
            group_number=entity.group_number,
            hashed_password=entity.hashed_password,
            role=entity.role,
        )
