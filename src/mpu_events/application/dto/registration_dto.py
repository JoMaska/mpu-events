from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class RegistrationResponseDTO(BaseModel):
    id: UUID
    user_id: UUID
    event_id: UUID
    created_at: datetime

    model_config = {"from_attributes": True}