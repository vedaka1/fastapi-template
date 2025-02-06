from typing import Any

from src.application.common.filters.base import BaseFilters
from src.infrastructure.db.postgresql.common.filters.base import BaseFiltersImpl
from src.infrastructure.db.postgresql.common.models.base import Base


def build_filters(
    filters: BaseFilters | None,
    filters_impl: type[BaseFiltersImpl],
    model: type[Base],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
) -> list[Any]:
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
    filters_map: dict[str, Any],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
    additional_filters: list[Any] | None = None,
) -> list[Any]:
    """
    Args:
        filters_dict: словарь фильтров из класса BaseFilters
        filters_map: словарь фильтров из класса BaseFiltersImpl
        exclude_fields: ключи для исключения из списка фильтров
        only_fields: список ключей для получения только определенных фильтров
        additional_filters: список дополнительных фильтров
    Returns:
        список фильтров list[Any]
    """
    exclude_fields = exclude_fields or set()
    filters_list = []
    keys = only_fields or filters_dict.keys()

    for key in keys:
        value = filters_dict.get(key)
        if key not in exclude_fields and key in filters_map and (isinstance(value, bool) or value):
            filters_list.append(filters_map[key](value))

    if additional_filters:
        filters_list.extend(additional_filters)

    return filters_list
