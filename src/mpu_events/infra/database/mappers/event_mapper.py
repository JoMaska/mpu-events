import uuid
from mpu_events.domain.entities.event import Event
from mpu_events.infra.database.models.event_model import EventModel


class EventMapper:
    @staticmethod
    def to_entity(model: EventModel) -> Event:
        return Event(
            id=model.id,
            title=model.title,
            description=model.description,
            start_time=model.start_time,
            location=model.location,
            max_participants=model.max_participants,
            created_by=model.created_by,
            created_at=model.created_at,
        )

    @staticmethod
    def to_model(entity: Event) -> EventModel:
        return EventModel(
            title=entity.title,
            description=entity.description,
            start_time=entity.start_time,
            location=entity.location,
            max_participants=entity.max_participants,
            created_by=entity.created_by,
        )