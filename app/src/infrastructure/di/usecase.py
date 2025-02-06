from typing import Annotated

from fastapi import Depends
from src.application.common.interfaces.commiter import ICommiter
from src.application.user.repository import IUserRepository
from src.application.user.usecases.create_user import CreateUserUseCase
from src.application.user.usecases.get_users import GetUsersUseCase
from src.infrastructure.di.stub import Stub


def create_user_usecase(
    user_repository: Annotated[IUserRepository, Depends(Stub(IUserRepository))],
    commiter: Annotated[ICommiter, Depends(Stub(ICommiter))],
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository, commiter)


def get_users_usecase(
    user_repository: Annotated[IUserRepository, Depends(Stub(IUserRepository))],
) -> GetUsersUseCase:
    return GetUsersUseCase(user_repository)
