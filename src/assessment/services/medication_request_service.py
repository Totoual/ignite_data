from sqlalchemy.ext.asyncio import AsyncSession

from assessment.models import MedicationRequest
from assessment.schemas.medication_request_schema import MedicationRequestSchema
from assessment.services.base.base_service import BaseService


class MedicationRequestService(BaseService):
    """
    Service to create and retrieve medication_requests.
    """

    async def create_medication_request(self, session: AsyncSession, medication_request: MedicationRequestSchema) -> None:
        """
        Create a new medication request.
        :param session:
        :return:
        """
        mr_db = MedicationRequest(**medication_request.model_dump())
        await self.create_item(session, model=mr_db)

