from dataclasses import dataclass


@dataclass
class PaginationRequest:
    page: int = 0
    limit: int = 100

    @property
    def offset(self):
        return self.page * self.limit
