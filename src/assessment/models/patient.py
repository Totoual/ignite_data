from enum import Enum

from sqlalchemy import UUID, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from assessment.models.model_base import Base


class SexEnum(Enum):
    male = "male"
    female = "female"


class Patient(Base):
    """
    Patient SQLAlchemy model.
    """
    __tablename__ = "patients"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    date_of_birth: Mapped[Date] = mapped_column(Date)
    sex: Mapped[SexEnum]
