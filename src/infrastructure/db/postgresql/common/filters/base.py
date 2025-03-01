from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from src.infrastructure.db.postgresql.common.models.base import Base

TModel = TypeVar('TModel', bound=Base)


class BaseFiltersImpl(Generic[TModel], ABC):
    @abstractmethod
    def __init__(self, model: type[TModel]) -> None: ...

    @staticmethod
    def get_additional_filters() -> list[Any] | None:
        return []
