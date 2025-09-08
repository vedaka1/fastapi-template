from uuid import UUID

from pydantic import BaseModel

from src.domain.user.entity import User


class UserResponse(BaseModel):
    uuid: UUID
    username: str
    first_name: str | None
    last_name: str | None
    middle_name: str | None

    @classmethod
    def from_entity(cls, user: User) -> 'UserResponse':
        return cls(
            uuid=user.uuid,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            middle_name=user.middle_name,
        )


class UsersResponse(BaseModel):
    items: list[UserResponse]
    total: int
