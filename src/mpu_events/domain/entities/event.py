from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Event:
    title: str
    description: str
    start_time: datetime
    location: str
    created_by: UUID

    id: UUID | None = None
    max_participants: int | None = None
    created_at: datetime | None = None

    def can_register(self, current_count: int) -> bool:
        if self.max_participants is None:
            return True
        return current_count < self.max_participants