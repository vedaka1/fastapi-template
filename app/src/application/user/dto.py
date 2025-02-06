from dataclasses import dataclass

from src.domain.user.entity import User


@dataclass
class CreateUserInput:
    username: str
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None


@dataclass
class GetUsersOutput:
    items: list[User]
    total: int
