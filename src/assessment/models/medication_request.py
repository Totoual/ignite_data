from enum import Enum

from sqlalchemy import ForeignKey, UUID, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from assessment.models.model_base import Base


class StatusEnum(Enum):
    active = "active"
    on_hold = "on_hold"
    cancelled = "cancelled"
    completed = "completed"


class MedicationRequest(Base):
    """
    Medication Request Sqlalchemy model.
    """
    __tablename__ = 'medication_requests'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    patience_id: Mapped[UUID] = mapped_column(ForeignKey("patients.id", ondelete="CASCADE"), nullable=False, index=True)
    clinician_id: Mapped[UUID] = mapped_column(ForeignKey("clinicians.registration_id",
                                                          ondelete="CASCADE"),
                                               nullable=False, index=True)
    medication_id: Mapped[int] = mapped_column(ForeignKey("medications.id", ondelete="CASCADE"),
                                               nullable=False,
                                               index=True)
    reason: Mapped[str]
    prescribed_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
