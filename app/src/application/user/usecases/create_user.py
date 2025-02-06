from src.application.common.interfaces.commiter import ICommiter
from src.application.user.dto import CreateUserInput
from src.application.user.repository import IUserRepository
from src.domain.user.entity import User
from src.domain.user.exceptions import UserAlrearedyExistException


class CreateUserUseCase:
    def __init__(
        self,
        user_repository: IUserRepository,
        commiter: ICommiter,
    ) -> None:
        self.user_repository = user_repository
        self.commiter = commiter

    async def execute(self, input: CreateUserInput) -> None:
        is_exists = await self.user_repository.get_by_username(input.username)
        if is_exists:
            raise UserAlrearedyExistException

        user = User.create(**input.__dict__)

        await self.user_repository.create(user)
        await self.commiter.commit()
