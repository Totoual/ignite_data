from datetime import datetime
from typing import Optional, List

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from assessment.models import MedicationRequest
from assessment.models.medication_request import StatusEnum
from assessment.schemas.medication_request_schema import MedicationRequestSchema, MedicationRequestResponseSchema
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
            end_date: Optional[datetime]
    ) -> List[MedicationRequestResponseSchema]:

        filters = []
        if status:
            filters.append(MedicationRequest.status == status)
        if start_date and end_date:
            filters.append(and_(MedicationRequest.prescribed_date >= start_date,
                                MedicationRequest.prescribed_date <= end_date))
        elif start_date:
            filters.append(MedicationRequest.prescribed_date >= start_date)
        elif end_date:
            filters.append(MedicationRequest.prescribed_date <= end_date)

        results = await self.select(session=session,
                                   model=MedicationRequest,
                                   options=[selectinload(MedicationRequest.clinician),
                                            selectinload(MedicationRequest.medication)],
                                   filters=[and_(*filters)])
        if results:
            response = [MedicationRequestResponseSchema.model_validate(result) for result in results]
            return response
        else:
            # Returning empty list, for consistency so we don't raise an exception.
            return list()
