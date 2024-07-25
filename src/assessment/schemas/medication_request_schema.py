from pydantic import BaseModel, constr
from typing import Optional
from uuid import UUID
from datetime import datetime


class MedicationRequestSchema(BaseModel):
    """Pydantic model for MedicationRequest"""
    patience_id: UUID
    clinician_id: UUID
    medication_id: int
    reason: constr(min_length=1)
    prescribed_date: datetime
    end_date: Optional[datetime] = None

