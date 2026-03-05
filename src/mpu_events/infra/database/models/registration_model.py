from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from datetime import datetime
import uuid

from mpu_events.infra.database.base import Base, TimestampMixin


class RegistrationModel(Base, TimestampMixin):
    __tablename__ = "registrations"

    id: Mapped[uuid.UUID] = mapped_column(
        PgUUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(PgUUID(as_uuid=True), nullable=False)
    event_id: Mapped[uuid.UUID] = mapped_column(PgUUID(as_uuid=True), nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "event_id", name="uq_user_event"),
    )