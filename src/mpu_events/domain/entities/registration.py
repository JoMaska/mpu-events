from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Registration:
    user_id: UUID
    event_id: UUID

    id: UUID | None = None
    created_at: datetime | None = None