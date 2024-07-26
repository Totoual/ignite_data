from abc import ABC
from typing import Any, Dict, List, Optional, Union

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.models.model_base import Base


class BaseService(ABC):
    def __init__(self):
        """
        Abstract base class for data managers.
        """
        pass

    async def select(
        self, session: AsyncSession, model: Base, options: Optional[List] = None, filters: Optional[List] = None
    ):
        """
        Selects the data from the database.
        :param session: AsyncSession
        :param model: Base
        :param options: List
        :param filters: List
        :return: List
        """
        if filters is None:
            filters = []
        if options is None:
            options = []
        query = select(model).options(*options).where(*filters)
        result = await session.execute(query)
        return result.scalars()

    async def create_item(self, session: AsyncSession, model: Base) -> Base:
        """Create a new item in the db."""
        session.add(model)
        await session.commit()
        return model

    async def update(
        self, session: AsyncSession, model: Base, data: Union[List, Dict[str, Any]], filters: Optional[List] = None
    ) -> None:
        """Update the data in the database."""
        if filters is None:
            filters = []

        if isinstance(data, dict):
            query = update(model).where(*filters).values(data).execution_options(synchronize_session="fetch")
        else:
            query = update(model).where(*filters).values(*data).execution_options(synchronize_session="fetch")
        await session.execute(query)
        await session.commit()
