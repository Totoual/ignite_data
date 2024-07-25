from pydantic import BaseModel


class ClinicianBaseSchema(BaseModel):
    first_name: str
    last_name: str