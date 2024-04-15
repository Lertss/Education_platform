from typing import Generator

import settings
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


# create async engine for interaction with database
engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)

# create session for the interaction with database
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
