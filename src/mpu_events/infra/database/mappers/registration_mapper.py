from mpu_events.domain.entities.registration import Registration
from mpu_events.infra.database.models.registration_model import RegistrationModel


class RegistrationMapper:
    @staticmethod
    def to_entity(model: RegistrationModel) -> Registration:
        return Registration(
            id=model.id,
            user_id=model.user_id,
            event_id=model.event_id,
            created_at=model.created_at,
        )