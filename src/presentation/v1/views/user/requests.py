from pydantic import BaseModel

from src.application.user.dto import CreateUserInput


class CreateUserRequest(BaseModel):
    username: str
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None

    def to_dto(self) -> CreateUserInput:
        return CreateUserInput(
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
        )
