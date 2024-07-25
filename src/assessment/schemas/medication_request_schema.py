from pydantic import BaseModel, constr
from typing import Optional
from uuid import UUID
from datetime import datetime

from assessment.models.medication_request import StatusEnum
from assessment.schemas.clinician_schema import ClinicianBaseSchema
from assessment.schemas.medication_schema import MedicationBaseSchema


class MedicationRequestSchema(BaseModel):
    """Pydantic model for MedicationRequest"""
    patience_id: UUID
    clinician_id: UUID
    medication_id: int
    reason: constr(min_length=1)
    prescribed_date: datetime
    end_date: Optional[datetime] = None


class MedicationRequestResponseSchema(MedicationRequestSchema):
    status: str
    clinician: ClinicianBaseSchema
    code_name: MedicationBaseSchema

