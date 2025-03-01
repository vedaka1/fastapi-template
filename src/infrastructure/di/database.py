from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.application.common.interfaces.commiter import ICommiter
from src.infrastructure.db.postgresql.commiter import Commiter
from src.infrastructure.di.stub import Stub


def get_commiter(session: Annotated[AsyncSession, Depends(Stub(AsyncSession))]) -> ICommiter:
    return Commiter(session=session)
