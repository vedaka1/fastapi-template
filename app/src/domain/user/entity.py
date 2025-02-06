from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
    uuid: UUID
    username: str
    first_name: str | None
    last_name: str | None
    middle_name: str | None

    @staticmethod
    def create(
        username: str,
        first_name: str | None = None,
        last_name: str | None = None,
        middle_name: str | None = None,
    ) -> 'User':
        return User(
            uuid=uuid4(),
            username=username,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
        )
