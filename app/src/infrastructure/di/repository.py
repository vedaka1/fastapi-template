from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.user.repository import IUserRepository
from src.infrastructure.db.postgresql.user.repository import UserRepository
from src.infrastructure.di.stub import Stub


def get_user_repository(session: Annotated[AsyncSession, Depends(Stub(AsyncSession))]) -> IUserRepository:
    return UserRepository(session=session)
