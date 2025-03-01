from collections.abc import Callable, Generator, Iterable
from typing import Any, TypeVar

from sqlalchemy import BinaryExpression

from src.application.common.filters.base import BaseFilters
from src.infrastructure.db.postgresql.common.filters.base import BaseFiltersImpl
from src.infrastructure.db.postgresql.common.models.base import Base

TModel = TypeVar('TModel', bound=Base)


def build_filters(
    filters: BaseFilters | None,
    filters_impl: type[BaseFiltersImpl[TModel]],
    model: type[TModel],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
) -> list[BinaryExpression[Any]]:
    """
    Args:
        filters: класс фильтров BaseFilters | None
        filters_impl: тип фильтра, имплиментирующего фильтры из BaseFilters
        model: модель для фильтров или ее алиас
        exclude_fields: ключи для исключения из списка фильтров
        only_fields: список ключей для получения только определенных фильтров
    Returns:
        список фильтров алхимии
    """

    if not filters:
        return []

    return _build_filters_list(
        filters_dict=filters.__dict__,
        filters_map=filters_impl(model).__dict__,
        exclude_fields=exclude_fields,
        only_fields=only_fields,
        additional_filters=filters_impl.get_additional_filters(),
    )


def _build_filters_list(
    filters_dict: dict[str, Any],
    filters_map: dict[str, Callable[[Any], BinaryExpression[Any]]],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
    additional_filters: list[BinaryExpression[Any]] | None = None,
) -> list[BinaryExpression[Any]]:
    """
    Args:
        filters_dict: словарь фильтров из класса BaseFilters
        filters_map: словарь фильтров из класса BaseFiltersImpl
        exclude_fields: ключи для исключения из списка фильтров
        only_fields: список ключей для получения только определенных фильтров
        additional_filters: список дополнительных фильтров
    Returns:
        список фильтров
    """
    exclude_fields = exclude_fields or set()
    keys = only_fields or filters_dict.keys()

    def filter_gen(keys: Iterable[str]) -> Generator[BinaryExpression[Any]]:
        for key in keys:
            value = filters_dict.get(key)
            if key not in exclude_fields and key in filters_map and (isinstance(value, bool) or value):
                yield filters_map[key](value)

    filters_list = [filter for filter in filter_gen(keys)]
    if additional_filters:
        filters_list.extend(additional_filters)

    return filters_list
