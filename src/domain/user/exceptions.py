from dataclasses import dataclass

from src.domain.common.exceptions import ApplicationException


@dataclass
class UserAlreadyExistException(ApplicationException):
    status_code: int = 409
    message: str = 'User already exist'
