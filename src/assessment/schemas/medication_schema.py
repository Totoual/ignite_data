from pydantic import BaseModel, ConfigDict


class MedicationBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    code_name: str
