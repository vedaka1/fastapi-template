from dataclasses import dataclass

from src.application.common.interfaces.commiter import ICommiter
from src.application.user.dto import CreateUserInput
from src.application.user.repository import IUserRepository
from src.domain.user.entity import User
from src.domain.user.exceptions import UserAlreadyExistException


@dataclass(slots=True, eq=False)
class CreateUserInteractor:
    user_repository: IUserRepository
    commiter: ICommiter

    async def execute(self, input: CreateUserInput) -> User:
        is_exists = await self.user_repository.get_by_username(input.username)
        if is_exists:
            raise UserAlreadyExistException

        user = User.create(**input.__dict__)

        await self.user_repository.create(user)
        await self.commiter.commit()
        return user
