from pydantic import BaseModel, constr, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

from assessment.models.medication_request import StatusEnum
from assessment.schemas.clinician_schema import ClinicianBaseSchema
from assessment.schemas.medication_schema import MedicationBaseSchema


class MedicationRequestSchema(BaseModel):
    """Pydantic model for MedicationRequest"""
    model_config = ConfigDict(from_attributes=True)

    patience_id: UUID
    clinician_id: UUID
    medication_id: int
    reason: constr(min_length=1)
    prescribed_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: Optional[datetime] = None
    status: StatusEnum


class MedicationRequestResponseSchema(MedicationRequestSchema):
    ...
    clinician: ClinicianBaseSchema
    medication: MedicationBaseSchema

