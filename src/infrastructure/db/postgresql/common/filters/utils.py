from typing import Any, TypeVar

from sqlalchemy import and_, func
from sqlalchemy.orm import InstrumentedAttribute

T = TypeVar('T')


def create_search_string(fields: list[InstrumentedAttribute], v: str) -> Any:
    filters = (func.concat(*fields).ilike(f'%{word}%') for word in v.split())
    return and_(f for f in filters)  # type: ignore
