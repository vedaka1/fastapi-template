from pydantic import BaseModel

from src.application.user.filters import UserFilters


class UserFiltersRequest(BaseModel):
    search_string: str | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None

    def to_dto(self) -> UserFilters:
        return UserFilters(
            search_string=self.search_string,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
        )
