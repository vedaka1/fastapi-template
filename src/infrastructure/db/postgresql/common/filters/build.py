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
        filters_impl_dict=filters_impl(model).__dict__,
        exclude_fields=exclude_fields,
        only_fields=only_fields,
    )


def _build_filters_list(
    filters_dict: dict[str, Any],
    filters_impl_dict: dict[str, Callable[[Any], BinaryExpression[Any]]],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
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

    keys = only_fields or _key_gen(filters_dict.keys(), exclude_fields, filters_impl_dict)
    filters_list = [filter for filter in _filter_gen(keys, filters_dict, filters_impl_dict)]

    return filters_list


def _key_gen(
    keys: Iterable[str],
    exclude_fields: set[str],
    filters_impl_dict: dict[str, Callable[[Any], BinaryExpression[Any]]],
) -> Generator[str]:
    for key in keys:
        if key not in exclude_fields and key in filters_impl_dict:
            yield key


def _filter_gen(
    keys: list[str] | Generator[str],
    filters_dict: dict[str, Any],
    filters_impl_dict: dict[str, Callable[[Any], BinaryExpression[Any]]],
) -> Generator[BinaryExpression[Any]]:
    for key in keys:
        value = filters_dict.get(key)
        if type(value) is bool or value:
            yield filters_impl_dict[key](value)
