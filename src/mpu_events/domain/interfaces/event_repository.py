from abc import ABC, abstractmethod
from uuid import UUID

from mpu_events.domain.entities.event import Event

class EventRepository(ABC):
    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 10) -> list[Event]: ...

    @abstractmethod
    async def get_by_id(self, event_id: UUID) -> Event | None: ...

    @abstractmethod
    async def create(self, event: Event) -> Event: ...

    @abstractmethod
    async def update(self, event: Event) -> Event: ...

    @abstractmethod
    async def delete(self, event_id: UUID) -> None: ...