from unittest.mock import AsyncMock
import pytest

from assessment.main import app
from assessment.models.sessionmaker import get_db


mock_session = AsyncMock()

async def override_get_db():
    try:
        yield mock_session
    finally:
        pass

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def mock_db_session():
    return mock_session