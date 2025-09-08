from typing import Annotated

from fastapi import Depends, FastAPI

from src.application.common.interfaces.commiter import ICommiter
from src.application.user.interactors.create_one import CreateUserInteractor
from src.application.user.interactors.get_many import GetUsersInteractor
from src.application.user.repository import IUserRepository
from src.infrastructure.di.stub import Stub


def init_user_usecases(app: FastAPI) -> None:
    app.dependency_overrides[CreateUserInteractor] = create_user_usecase
    app.dependency_overrides[GetUsersInteractor] = get_users_usecase


def create_user_usecase(
    user_repository: Annotated[IUserRepository, Depends(Stub(IUserRepository))],
    commiter: Annotated[ICommiter, Depends(Stub(ICommiter))],
) -> CreateUserInteractor:
    return CreateUserInteractor(user_repository, commiter)


def get_users_usecase(
    user_repository: Annotated[IUserRepository, Depends(Stub(IUserRepository))],
) -> GetUsersInteractor:
    return GetUsersInteractor(user_repository)
