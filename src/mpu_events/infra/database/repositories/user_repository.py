from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from mpu_events.domain.entities.user import User
from mpu_events.domain.interfaces.user_repository import UserRepository
from mpu_events.infra.database.models.user_model import UserModel
from mpu_events.infra.database.mappers.user_mapper import UserMapper


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: UUID) -> User | None:
        result = await self.session.execute(
            select(UserModel).where(UserModel.id == user_id)
        )
        model = result.scalar_one_or_none()
        return UserMapper.to_entity(model) if model else None

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(UserModel).where(UserModel.email == email)
        )
        model = result.scalar_one_or_none()
        return UserMapper.to_entity(model) if model else None

    async def create(self, user: User) -> User:
        model = UserMapper.to_model(user)
        self.session.add(model)
        await self.session.flush()  # получить id не делая commit
        return UserMapper.to_entity(model)