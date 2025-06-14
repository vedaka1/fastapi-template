from dataclasses import dataclass

from src.application.common.types import OrderBy
from src.application.user.dto import GetUsersOutput
from src.application.user.filters import UserFilters
from src.application.user.repository import IUserRepository


@dataclass(slots=True, eq=False)
class GetUsersUseCase:
    user_repository: IUserRepository

    async def execute(
        self,
        filters: UserFilters | None = None,
        order_by: OrderBy | None = None,
        offset: int | None = None,
        limit: int | None = 100,
    ) -> GetUsersOutput:
        users = await self.user_repository.get_many(filters, order_by, offset, limit)
        total = await self.user_repository.count(filters)

        return GetUsersOutput(items=users, total=total)
