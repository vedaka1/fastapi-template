from typing import Any, TypeVar

from sqlalchemy import desc

from src.application.common.enums import Sort
from src.application.common.types import OrderBy

T = TypeVar('T', bound=Any)


def build_order_by(order_by: OrderBy, model: Any) -> list[Any]:
    order_by_list = []
    for field, order in order_by.items():
        if model_field := getattr(model, field, None):
            order_by_list.append(desc(model_field) if order == Sort.desc else model_field)
    return order_by_list


def apply_offset_and_limit(query: T, offset: int | None, limit: int | None = 100) -> T:
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query
