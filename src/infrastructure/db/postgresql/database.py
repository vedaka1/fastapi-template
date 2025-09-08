from functools import lru_cache
from typing import Annotated, AsyncIterable

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import PostgresqlConfig
from src.infrastructure.di.stub import Stub


@lru_cache(1)
def get_async_engine(echo: bool = False) -> AsyncEngine:
    return create_async_engine(url=PostgresqlConfig.load_from_env().DB_URL, echo=echo)


def get_async_sessionmaker(
    engine: Annotated[AsyncEngine, Depends(Stub(AsyncEngine))],
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session(
    session_factory: Annotated[async_sessionmaker[AsyncSession], Depends(Stub(async_sessionmaker[AsyncSession]))],
) -> AsyncIterable[AsyncSession]:
    async with session_factory() as session:
        yield session
        await session.close()
