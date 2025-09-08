from dataclasses import dataclass


@dataclass
class CreateUserInput:
    username: str
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
