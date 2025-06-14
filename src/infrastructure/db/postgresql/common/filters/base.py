from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.infrastructure.db.postgresql.common.models.base import Base

TModel = TypeVar('TModel', bound=Base)


class BaseFiltersImpl(Generic[TModel], ABC):
    @abstractmethod
    def __init__(self, model: type[TModel]) -> None: ...
