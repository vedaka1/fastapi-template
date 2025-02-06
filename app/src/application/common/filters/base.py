from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class BaseFilters(ABC):
    @staticmethod
    @abstractmethod
    def get_map(model: Any) -> dict[str, Any]: ...
