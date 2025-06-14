from typing import Annotated

from fastapi import APIRouter, Depends

from src.application.user.dto import CreateUserInput, GetUsersOutput
from src.application.user.filters import UserFilters
from src.application.user.usecases.create import CreateUserUseCase
from src.application.user.usecases.get import GetUsersUseCase
from src.domain.user.exceptions import UserAlrearedyExistException
from src.infrastructure.di.stub import Stub
from src.presentation.order_by import create_order_by_from_query
from src.presentation.pagination import PaginationQuery

router = APIRouter(tags=['Users'], prefix='/users')


@router.post('', summary='Create user', responses={200: {'model': None}, 409: {'model': UserAlrearedyExistException}})
async def create_user(
    interactor: Annotated[CreateUserUseCase, Depends(Stub(CreateUserUseCase))],
    input: CreateUserInput = Depends(),
) -> None:
    data = await interactor.execute(input)
    return data


@router.get('', summary='Get users', responses={200: {'model': GetUsersOutput}})
async def get_users(
    interactor: Annotated[GetUsersUseCase, Depends(Stub(GetUsersUseCase))],
    user_filters: UserFilters = Depends(),
    pagination: PaginationQuery = Depends(),
    order_by: str | None = None,
) -> GetUsersOutput:
    data = await interactor.execute(
        user_filters,
        create_order_by_from_query(order_by),
        pagination.offset,
        pagination.limit,
    )
    return data
