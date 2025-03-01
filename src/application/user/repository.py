from abc import ABC, abstractmethod
from uuid import UUID

from src.application.common.enums import Sort
from src.application.user.filters import UserFilters
from src.domain.user.entity import User


class IUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> None: ...

    @abstractmethod
    async def delete(self, entity_uuid: UUID) -> None: ...

    @abstractmethod
    async def get_by_uuid(self, entity_uuid: UUID) -> User | None: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> User | None: ...

    @abstractmethod
    async def get_many(
        self,
        filters: UserFilters | None = None,
        order_by: dict[str, Sort] | None = None,
        offset: int | None = None,
        limit: int | None = 100,
    ) -> list[User]: ...

    @abstractmethod
    async def count(self, filters: UserFilters | None = None) -> int: ...
