from pydantic import BaseModel


class MedicationBaseSchema(BaseModel):
    code_name: str