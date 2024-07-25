import fastapi
import logging
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.models.sessionmaker import get_db
from assessment.schemas.medication_request_schema import MedicationRequestSchema
from assessment.services.medication_request_service import MedicationRequestService

logger = logging.getLogger(__name__)

router = fastapi.APIRouter()


@router.post("/medications-request", response_model_exclude_none=True)
async def create_project(
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