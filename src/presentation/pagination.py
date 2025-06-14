from dataclasses import dataclass

from src.application.common.enums import Sort


@dataclass
class PaginationQuery:
    page: int = 0
    limit: int = 100

    @property
    def offset(self):
        return self.page * self.limit


@dataclass
class OrderByQuery:
    order_by: dict[str, Sort]
