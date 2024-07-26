# test_endpoints.py
import uuid

import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from unittest.mock import patch
from assessment.main import app
from assessment.models.medication import FormEnum
from assessment.models.patient import SexEnum
from assessment.models import Clinician, Patient, MedicationRequest, Medication

client = TestClient(app)

#
# # Test data
test_clinician = Clinician(
    registration_id=str(uuid.uuid4()),
    first_name="John",
    last_name="Doe",
)

test_patient = Patient(
    id=str(uuid.uuid4()),
    first_name="John",
    last_name="Doy",
    date_of_birth="1988-11-26",
    sex=SexEnum.male
)

test_medication = Medication(
    id=1,
    code="3452345",
    code_name="Oxamniquine",
    code_system="SNOMED",
    strength_value=5,
    strength_unit="g/ml",
    form=FormEnum.tablet
)

test_medication_request_json = {
  "patience_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "clinician_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "medication_id": 1,
  "reason": "string",
  "prescribed_date": "2024-07-26T06:15:06.699Z",
  "end_date": "2024-07-26T06:15:06.699Z",
  "frequency": 1,
  "status": "active"
}

test_medication_patch_json = {
  "frequency": 3,
  "end_date": "2024-07-26T07:04:58.586Z",
  "status": "active"
}



@pytest.mark.asyncio
async def test_create_medical_request(mock_db_session):

    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.post("/medication-request", json=test_medication_request_json)
    assert response.status_code == 200
    mock_db_session.add.assert_called()
    mock_db_session.commit.assert_called()


@pytest.mark.asyncio
async def test_get_filtered_medical_request(mock_db_session):

    async def mock_execute_query(self, session, model, options, filters):
        mock_medication_requests = [MedicationRequest(id=1,
                                                      patience_id='123e4567-e89b-12d3-a456-426614174000',
                                                      clinician_id='123e4567-e89b-12d3-a456-426614174001',
                                                      medication_id=1,
                                                      reason='Test Reason',
                                                      prescribed_date='2023-07-25T00:00:00Z',
                                                      end_date='2023-07-30T00:00:00Z',
                                                      status='active',
                                                      frequency=1,
                                                      clinician=test_clinician,
                                                      medication=test_medication)]
        return mock_medication_requests

    with patch("assessment.services.base.base_service.BaseService.select", new=mock_execute_query):
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            response = await ac.get("/medication-request", params={"status": "active"})
        json_data = response.json()
        assert response.status_code == 200
        assert type(response.json()) == list
        assert json_data[0]["frequency"] == 1
        assert "clinician" in json_data[0].keys()


@pytest.mark.asyncio
async def test_get_filtered_medical_request_with_start_date(mock_db_session):

    async def mock_execute_query(self, session, model, options, filters):
        mock_medication_requests = [MedicationRequest(id=1,
                                                      patience_id='123e4567-e89b-12d3-a456-426614174000',
                                                      clinician_id='123e4567-e89b-12d3-a456-426614174001',
                                                      medication_id=1,
                                                      reason='Test Reason',
                                                      prescribed_date='2023-07-25T00:00:00Z',
                                                      end_date='2023-07-30T00:00:00Z',
                                                      status='active',
                                                      frequency=1,
                                                      clinician=test_clinician,
                                                      medication=test_medication)]
        return mock_medication_requests

    with patch("assessment.services.base.base_service.BaseService.select", new=mock_execute_query):
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            response = await ac.get("/medication-request", params={"start_date": "2023-07-25"})
        json_data = response.json()
        assert response.status_code == 200
        assert type(response.json()) == list
        assert json_data[0]["frequency"] == 1
        assert "clinician" in json_data[0].keys()

@pytest.mark.asyncio
async def test_get_filtered_medical_request_with_end_date(mock_db_session):

    async def mock_execute_query(self, session, model, options, filters):
        mock_medication_requests = [MedicationRequest(id=1,
                                                      patience_id='123e4567-e89b-12d3-a456-426614174000',
                                                      clinician_id='123e4567-e89b-12d3-a456-426614174001',
                                                      medication_id=1,
                                                      reason='Test Reason',
                                                      prescribed_date='2023-07-25T00:00:00Z',
                                                      end_date='2023-07-30T00:00:00Z',
                                                      status='active',
                                                      frequency=1,
                                                      clinician=test_clinician,
                                                      medication=test_medication)]
        return mock_medication_requests

    with patch("assessment.services.base.base_service.BaseService.select", new=mock_execute_query):
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            response = await ac.get("/medication-request", params={"end_date": "2023-07-25"})
        json_data = response.json()
        assert response.status_code == 200
        assert type(response.json()) == list
        assert json_data[0]["frequency"] == 1
        assert "clinician" in json_data[0].keys()


@pytest.mark.asyncio
async def test_get_filtered_medical_request_with_both_dates(mock_db_session):

    async def mock_execute_query(self, session, model, options, filters):
        mock_medication_requests = [MedicationRequest(id=1,
                                                      patience_id='123e4567-e89b-12d3-a456-426614174000',
                                                      clinician_id='123e4567-e89b-12d3-a456-426614174001',
                                                      medication_id=1,
                                                      reason='Test Reason',
                                                      prescribed_date='2023-07-25T00:00:00Z',
                                                      end_date='2023-07-30T00:00:00Z',
                                                      status='active',
                                                      frequency=1,
                                                      clinician=test_clinician,
                                                      medication=test_medication)]
        return mock_medication_requests

    with patch("assessment.services.base.base_service.BaseService.select", new=mock_execute_query):
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            response = await ac.get("/medication-request", params={"start_date": "2023-07-25",
                                                                   "end_date": "2023-07-25"})
        json_data = response.json()
        assert response.status_code == 200
        assert type(response.json()) == list
        assert json_data[0]["frequency"] == 1
        assert "clinician" in json_data[0].keys()


@pytest.mark.asyncio
async def test_get_filtered_medical_request_with_no_results(mock_db_session):

    async def mock_execute_query(self, session, model, options, filters):
        mock_medication_requests = None
        return mock_medication_requests

    with patch("assessment.services.base.base_service.BaseService.select", new=mock_execute_query):
        async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
            response = await ac.get("/medication-request", params={"start_date": "2023-07-25",
                                                                   "end_date": "2023-07-25"})
        json_data = response.json()
        assert response.status_code == 200
        assert type(response.json()) == list
        assert len(json_data) == 0


@pytest.mark.asyncio
async def test_patch_medical_request(mock_db_session):

    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.patch("/medication-request/1", json=test_medication_patch_json)
    assert response.status_code == 200
    mock_db_session.commit.assert_called()