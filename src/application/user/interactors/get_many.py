from dataclasses import dataclass

from src.application.common.types import OrderBy
from src.application.user.filters import UserFilters
from src.application.user.repository import IUserRepository
from src.domain.user.entity import User


@dataclass(slots=True, eq=False)
class GetUsersInteractor:
    user_repository: IUserRepository

    async def execute(
        self,
        filters: UserFilters | None = None,
        order_by: OrderBy | None = None,
        offset: int | None = None,
        limit: int | None = 100,
    ) -> tuple[list[User], int]:
        users = await self.user_repository.get_many(filters, order_by, offset, limit)
        total = await self.user_repository.count(filters)

        return users, total
