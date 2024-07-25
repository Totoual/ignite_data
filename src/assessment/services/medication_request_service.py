from datetime import datetime
from typing import Optional

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.models import MedicationRequest
from assessment.models.medication_request import StatusEnum
from assessment.schemas.medication_request_schema import MedicationRequestSchema, MedicationRequestFilteredSchema
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

    async def get_medication_request(
            self,
            session: AsyncSession,
            status: Optional[StatusEnum],
            start_date: Optional[datetime],
            end_date: Optional[datetime]):

        filters = []
        if status:
            filters.append(MedicationRequest.status == status)
        if start_date:
            filters.append(MedicationRequest.prescribed_date >= start_date)
        if end_date:
            filters.append(MedicationRequest.end_date <= end_date)

        query = await self.select(session=session, model=MedicationRequest, filters=[and_(*filters)])