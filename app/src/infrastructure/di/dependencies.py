from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from src.application.common.interfaces.commiter import ICommiter
from src.application.user.repository import IUserRepository
from src.application.user.usecases.create_user import CreateUserUseCase
from src.application.user.usecases.get_users import GetUsersUseCase
from src.infrastructure.db.postgresql.database import get_async_engine, get_async_session, get_async_sessionmaker
from src.infrastructure.di.common import get_commiter
from src.infrastructure.di.repository import get_user_repository
from src.infrastructure.di.usecase import create_user_usecase, get_users_usecase


def init_db(app: FastAPI) -> None:
    app.dependency_overrides[AsyncEngine] = get_async_engine
    app.dependency_overrides[async_sessionmaker[AsyncSession]] = get_async_sessionmaker
    app.dependency_overrides[AsyncSession] = get_async_session
    app.dependency_overrides[ICommiter] = get_commiter


def init_repositories(app: FastAPI) -> None:
    app.dependency_overrides[IUserRepository] = get_user_repository


def init_usecases(app: FastAPI) -> None:
    app.dependency_overrides[CreateUserUseCase] = create_user_usecase
    app.dependency_overrides[GetUsersUseCase] = get_users_usecase


def init_dependencies(app: FastAPI) -> None:
    """Initialize dependencies."""
    init_db(app=app)
    init_repositories(app=app)
    init_usecases(app=app)
