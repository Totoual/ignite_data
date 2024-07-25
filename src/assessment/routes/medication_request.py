from datetime import datetime
from typing import Optional, List

import fastapi
import logging
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.models.medication_request import StatusEnum
from assessment.models.sessionmaker import get_db
from assessment.schemas.medication_request_schema import MedicationRequestSchema, MedicationRequestResponseSchema
from assessment.services.medication_request_service import MedicationRequestService

logger = logging.getLogger(__name__)

router = fastapi.APIRouter()


@router.post("/medications-request", response_model_exclude_none=True)
async def create_medication_request(
    medication_request: MedicationRequestSchema, session: AsyncSession = fastapi.Depends(get_db)
):
    """
    Create a new project.
    :param medication_request:
    :param session:
    :return:
    """
    service = MedicationRequestService()
    await service.create_medication_request(session=session, medication_request=medication_request)


@router.get("/medications-request",
            response_model_exclude_none=True,
            response_model=List[MedicationRequestResponseSchema])
async def get_filtered_medication(
        status: Optional[StatusEnum] = fastapi.Query(None),
        start_date: Optional[datetime] = fastapi.Query(None),
        end_date: Optional[datetime] = fastapi.Query(None),
        session: AsyncSession = fastapi.Depends(get_db)
):
    """
    Create a new project.
    :param status:
    :param start_date:
    :param end_date:
    :param session:
    :return:
    """
    service = MedicationRequestService()
    response = await service.get_medication_request(session=session, status=status, start_date=start_date, end_date=end_date)
    return response