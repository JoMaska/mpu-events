from uuid import UUID
from mpu_events.domain.interfaces.event_repository import EventRepository
from mpu_events.domain.interfaces.registration_repository import RegistrationRepository
from mpu_events.domain.exceptions.exceptions import (
    EventNotFoundException,
    AlreadyRegisteredException,
    EventFullException,
)
from mpu_events.application.dto.registration_dto import RegistrationResponseDTO


class RegisterForEventUseCase:
    def __init__(self, event_repo: EventRepository, registration_repo: RegistrationRepository):
        self.event_repo = event_repo
        self.registration_repo = registration_repo

    async def execute(self, user_id: UUID, event_id: UUID) -> RegistrationResponseDTO:
        event = await self.event_repo.get_by_id(event_id)
        if not event:
            raise EventNotFoundException(event_id)

        if await self.registration_repo.exists(user_id, event_id):
            raise AlreadyRegisteredException()

        current_count = await self.registration_repo.count_by_event(event_id)
        if not event.can_register(current_count):
            raise EventFullException()

        registration = await self.registration_repo.create(user_id, event_id)
        return RegistrationResponseDTO.model_validate(registration)