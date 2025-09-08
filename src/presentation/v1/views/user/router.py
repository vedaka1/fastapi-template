from typing import Annotated

from fastapi import APIRouter, Depends

from src.application.user.interactors.create_one import CreateUserInteractor
from src.application.user.interactors.get_many import GetUsersInteractor
from src.domain.user.exceptions import UserAlreadyExistException
from src.infrastructure.di.stub import Stub
from src.presentation.order_by import create_order_by_from_query
from src.presentation.pagination import PaginationRequest
from src.presentation.v1.views.user.filters import UserFiltersRequest
from src.presentation.v1.views.user.requests import CreateUserRequest
from src.presentation.v1.views.user.responses import UserResponse, UsersResponse

router = APIRouter(tags=['Users'], prefix='/users')


@router.post(
    '',
    summary='Create user',
    responses={
        200: {'model': None},
        409: {'model': UserAlreadyExistException, 'description': UserAlreadyExistException.message},
    },
)
async def create_user(
    interactor: Annotated[CreateUserInteractor, Depends(Stub(CreateUserInteractor))],
    input: CreateUserRequest = Depends(),
) -> UserResponse:
    user = await interactor.execute(input.to_dto())
    return UserResponse.from_entity(user)


@router.get(
    '',
    summary='Get users',
    responses={
        200: {'model': UsersResponse},
    },
)
async def get_users(
    interactor: Annotated[GetUsersInteractor, Depends(Stub(GetUsersInteractor))],
    user_filters: UserFiltersRequest = Depends(),
    pagination: PaginationRequest = Depends(),
    order_by: str | None = None,
) -> UsersResponse:
    users, total = await interactor.execute(
        user_filters.to_dto(),
        create_order_by_from_query(order_by),
        pagination.offset,
        pagination.limit,
    )
    return UsersResponse(items=[UserResponse.from_entity(user) for user in users], total=total)
