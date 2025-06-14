from uuid import UUID

from sqlalchemy import delete, func, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.types import OrderBy
from src.application.user.filters import UserFilters
from src.application.user.repository import IUserRepository
from src.domain.user.entity import User
from src.infrastructure.db.postgresql.common.filters.build import build_filters
from src.infrastructure.db.postgresql.common.utils import apply_offset_and_limit, build_order_by
from src.infrastructure.db.postgresql.user.filters import UserFiltersImpl
from src.infrastructure.db.postgresql.user.mapper import map_model_to_user
from src.infrastructure.db.postgresql.user.model import UserModel


class UserRepository(IUserRepository):
    __slots__ = ('session',)

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user: User) -> None:
        query = insert(UserModel).values(**user.__dict__)
        await self.session.execute(query)

    async def delete(self, entity_uuid: UUID) -> None:
        query = delete(UserModel).where(UserModel.uuid == entity_uuid)
        await self.session.execute(query)

    async def get_by_uuid(self, entity_uuid: UUID) -> User | None:
        query = select(UserModel).where(UserModel.uuid == entity_uuid)
        cursor = await self.session.execute(query)
        entity = cursor.scalar_one_or_none()
        return map_model_to_user(entity) if entity else None

    async def get_by_username(self, username: str) -> User | None:
        query = select(UserModel).where(UserModel.username == username)
        cursor = await self.session.execute(query)
        entity = cursor.scalar_one_or_none()
        return map_model_to_user(entity) if entity else None

    async def get_many(
        self,
        filters: UserFilters | None = None,
        order_by: OrderBy | None = None,
        offset: int | None = None,
        limit: int | None = 100,
    ) -> list[User]:
        filters_list = build_filters(filters, filters_impl=UserFiltersImpl, model=UserModel)
        query = select(UserModel).where(*filters_list)

        if order_by:
            query = query.order_by(*build_order_by(order_by, UserModel))

        query = apply_offset_and_limit(query=query, offset=offset, limit=limit)
        cursor = await self.session.execute(query)
        entities = cursor.scalars().all()
        return [map_model_to_user(entity) for entity in entities]

    async def count(self, filters: UserFilters | None = None) -> int:
        filters_list = build_filters(filters=filters, filters_impl=UserFiltersImpl, model=UserModel)
        query = select(func.count()).select_from(UserModel).where(*filters_list)
        cursor = await self.session.execute(query)
        count = cursor.scalar_one()
        return count
