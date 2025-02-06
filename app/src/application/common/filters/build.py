from typing import Any

from src.application.common.filters.base import BaseFilters
from src.infrastructure.db.postgresql.models.base import Base


def build_filters(
    filters: BaseFilters | None,
    model: type[Base],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
) -> list[Any]:
    """
    Args:
        filters: класс фильтров BaseFilters | None
        model: модель для фильтров или ее алиас
        exclude_fields: список полей, которые не должны быть в фильтре
        only_fields: список полей, для получения только определенных фильтров
    Returns:
        список фильтров алхимии
    """

    if not filters:
        return []

    filters_map = filters.get_map(model)

    return build_filters_list(
        filters_dict=filters.__dict__,
        filters_map=filters_map,
        exclude_fields=exclude_fields,
        only_fields=only_fields,
    )


def build_filters_list(
    filters_dict: dict[str, Any],
    filters_map: dict[str, Any],
    exclude_fields: set[str] | None = None,
    only_fields: list[str] | None = None,
    additional_filters: list[Any] | None = None,
) -> list[Any]:
    """
    Args:
        filters_dict: словарь фильтров из класса
        filters_map: словарь с ключами из filters_dict и lambda функциями в качестве значения для получения фильтра алхимии
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
