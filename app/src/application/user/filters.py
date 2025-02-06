from dataclasses import dataclass
from typing import Any

from sqlalchemy import func
from src.application.common.filters.base import BaseFilters
from src.application.common.filters.utils import create_search_string
from src.infrastructure.db.postgresql.models.user import UserModel


@dataclass
class UserFilters(BaseFilters):
    search_string: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None

    @staticmethod
    def get_map(model: UserModel) -> dict[str, Any]:
        return {
            'search_string': lambda v: func.concat(
                model.username,
                model.first_name,
                model.last_name,
                model.middle_name,
            ).ilike(create_search_string(v)),
            'username': lambda v: model.username == v,
            'first_name': lambda v: model.first_name == v,
            'last_name': lambda v: model.last_name == v,
            'middle_name': lambda v: model.middle_name == v,
        }
