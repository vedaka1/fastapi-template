from typing import Annotated

from fastapi import Depends, FastAPI

from src.application.common.interfaces.commiter import ICommiter
from src.application.user.repository import IUserRepository
from src.application.user.usecases.create import CreateUserUseCase
from src.application.user.usecases.get import GetUsersUseCase
from src.infrastructure.di.stub import Stub


def init_user_usecases(app: FastAPI) -> None:
    app.dependency_overrides[CreateUserUseCase] = create_user_usecase
    app.dependency_overrides[GetUsersUseCase] = get_users_usecase


def create_user_usecase(
    user_repository: Annotated[IUserRepository, Depends(Stub(IUserRepository))],
    commiter: Annotated[ICommiter, Depends(Stub(ICommiter))],
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository, commiter)


def get_users_usecase(
    user_repository: Annotated[IUserRepository, Depends(Stub(IUserRepository))],
) -> GetUsersUseCase:
    return GetUsersUseCase(user_repository)
