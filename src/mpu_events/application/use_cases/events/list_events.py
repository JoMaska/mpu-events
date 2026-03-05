from mpu_events.domain.interfaces.event_repository import EventRepository
from mpu_events.domain.interfaces.registration_repository import RegistrationRepository
from mpu_events.application.dto.event_dto import EventResponseDTO


class ListEventsUseCase:
    def __init__(self, event_repo: EventRepository, registration_repo: RegistrationRepository):
        self.event_repo = event_repo
        self.registration_repo = registration_repo

    async def execute(self, skip: int = 0, limit: int = 20) -> list[EventResponseDTO]:
        events = await self.event_repo.get_all(skip=skip, limit=limit)
        result = []
        for event in events:
            count = await self.registration_repo.count_by_event(event.id)
            result.append(EventResponseDTO.model_validate({
                **event.__dict__,
                "current_participants": count,
            }))
        return result