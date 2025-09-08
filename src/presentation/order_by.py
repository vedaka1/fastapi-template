from fastapi import HTTPException

from src.application.common.enums import Sort


def create_order_by_from_query(order_by: str | None) -> dict[str, Sort] | None:
    if not order_by:
        return None
    parts = order_by.split(',')
    _order_by: dict[str, Sort] = {}
    for part in parts:
        field_part = part.split(':')
        if len(field_part) != 2:
            return None
        try:
            _order_by[field_part[0]] = Sort(field_part[1])
        except ValueError:
            raise HTTPException(
                400,
                f'Incorrect order_by parameter `{field_part[0]}:{field_part[1]}`, order_by should be like `<field_name>:<asc,desc>',
            )
    return _order_by
