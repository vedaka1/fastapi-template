from abc import ABC, abstractmethod
from typing import Any

from src.infrastructure.db.postgresql.models.base import Base


class BaseFiltersImpl(ABC):
    @abstractmethod
    def __init__(self, model: type[Base]) -> None: ...

    @staticmethod
    def get_additional_filters() -> list[Any] | None:
        return []
