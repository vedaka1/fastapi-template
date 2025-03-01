from typing import Annotated

from fastapi import APIRouter, Depends
from src.application.user.dto import CreateUserInput, GetUsersOutput
from src.application.user.filters import UserFilters
from src.application.user.usecases.create_user import CreateUserUseCase
from src.application.user.usecases.get_users import GetUsersUseCase
from src.domain.user.exceptions import UserAlrearedyExistException
from src.infrastructure.di.stub import Stub
from src.presentation.pagination import PaginationQuery

router = APIRouter(tags=['Users'], prefix='/users')


@router.post('', summary='Create user', responses={200: {'model': None}, 409: {'model': UserAlrearedyExistException}})
async def create_user(
    create_user_usecase: Annotated[CreateUserUseCase, Depends(Stub(CreateUserUseCase))],
    input: CreateUserInput = Depends(),
) -> None:
    data = await create_user_usecase.execute(input)
    return data


@router.get('', summary='Get users', responses={200: {'model': GetUsersOutput}})
async def get_users(
    get_users_usecase: Annotated[GetUsersUseCase, Depends(Stub(GetUsersUseCase))],
    user_filters: UserFilters = Depends(),
    pagination: PaginationQuery = Depends(),
) -> GetUsersOutput:
    data = await get_users_usecase.execute(user_filters, pagination.offset, pagination.limit)
    return data
