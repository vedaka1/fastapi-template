from dataclasses import dataclass
from uuid import UUID

from src.application.common.filters.base import BaseFilters


@dataclass
class UserFilters(BaseFilters):
    search_string: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    uuid_in: list[UUID] | None = None
