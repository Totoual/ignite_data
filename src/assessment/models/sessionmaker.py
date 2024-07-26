from contextlib import asynccontextmanager
from typing import AsyncIterator, Union

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from assessment.config import config
from assessment.models.model_base import Base


class DatabaseSessionManager:
    def __init__(self):
        self.engine: Union[AsyncEngine, None] = None
        self._sessionmaker: Union[async_sessionmaker, None] = None

    def init(self, host: str):
        """Initialisation of the db."""
        pool_size = 10  # Adjust the pool size as per your requirements
        max_overflow = 20  # Maximum number of connections that can be created
        self.engine = create_async_engine(
            host,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_recycle=config.db_pool_recycle,
        )
        self._sessionmaker = async_sessionmaker(
            autocommit=False, expire_on_commit=False, bind=self.engine
        )

    async def close(self):
        if self.engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self.engine.dispose()
        self.engine = None
        self._sessionmaker = None

    @asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self.engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self.engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def create_all(self, connection: AsyncConnection):
        import assessment.models  # noqa

        await connection.run_sync(Base.metadata.create_all)

    async def drop_all(self, connection: AsyncConnection):
        await connection.run_sync(Base.metadata.drop_all)


sessionmanager = DatabaseSessionManager()


async def get_db() -> AsyncSession:
    async with sessionmanager.session() as session:
        yield session


@asynccontextmanager
async def get_dedicated_session() -> AsyncSession:
    async with sessionmanager.session() as session:
        yield session
