from src.application.user.dto import GetUsersOutput
from src.application.user.filters import UserFilters
from src.application.user.repository import IUserRepository


class GetUsersUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
    ) -> None:
        self.user_repository = user_repository

    async def execute(
        self,
        filters: UserFilters | None = None,
        offset: int | None = None,
        limit: int | None = 100,
    ) -> GetUsersOutput:
        users = await self.user_repository.get_many(filters=filters, offset=offset, limit=limit)
        total = await self.user_repository.count(filters=filters)

        return GetUsersOutput(items=users, total=total)
