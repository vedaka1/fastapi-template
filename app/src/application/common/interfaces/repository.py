from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.application.common.enums import Sort
from src.application.common.filters.base import BaseFilters

TEntity = TypeVar('TEntity')
TEntityFilters = TypeVar('TEntityFilters', bound=BaseFilters)


class IBaseRepository(Generic[TEntity, TEntityFilters], ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: int) -> TEntity | None:
        """
        Args:
            entity_id: id сущности
        Returns:
            модель сущности или None
        """
        ...

    @abstractmethod
    async def get_by_uuid(self, entity_uuid: str) -> TEntity | None:
        """
        Args:
            entity_uuid: uuid сущности
        Returns:
            модель сущности или None
        """
        ...

    @abstractmethod
    async def create(self, entity: TEntity) -> TEntity:
        """
        Args:
            entity: модель сущности
        Returns:
            модель сущности
        """
        ...

    @abstractmethod
    async def update(self, entity: TEntity) -> TEntity:
        """
        Args:
            entity: модель сущности
        Returns:
            модель сущности
        """
        ...

    @abstractmethod
    async def delete_by_uuid(self, entity_uuid: str) -> None:
        """
        Args:
            entity_uuid: uuid сущности
        Returns:
            None
        """
        ...

    @abstractmethod
    async def get_many(
        self,
        filters: TEntityFilters | None = None,
        order_by: dict[str, Sort] | None = None,
        offset: int | None = None,
        limit: int | None = 100,
    ) -> list[TEntity]:
        """
        Args:
            filters: фильтры модели
            order_by: поля для сортировки
            offset: смещение
            limit: лимит
        Returns:
            список сущностей
        """
        ...

    @abstractmethod
    async def count(self, filters: TEntityFilters | None = None) -> int:
        """
        Args:
            filters: фильтры модели
        Returns:
            общее количество сущностей
        """
        ...
