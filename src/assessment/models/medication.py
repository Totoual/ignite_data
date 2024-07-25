from enum import Enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from assessment.models.model_base import Base


class FormEnum(Enum):
    powder = "powder"
    tablet = "tablet"
    capsule = "capsule"
    syrup = "syrup"


class Medication(Base):
    """
    Medication SQLAlchemy model.
    """
    __tablename__ = 'medications'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(30))
    code_system: Mapped[str] = mapped_column(String(30))
    strength_value: Mapped[float]
    strength_unit: Mapped[str] = mapped_column(String(30))
    form: Mapped[FormEnum]