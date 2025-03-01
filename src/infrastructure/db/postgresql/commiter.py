from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.interfaces.commiter import ICommiter
from src.infrastructure.di.stub import Stub


class Commiter(ICommiter):
    def __init__(
        self,
        session: Annotated[AsyncSession, Depends(Stub(AsyncSession))],
    ) -> None:
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    async def close(self) -> None:
        await self.session.close()
