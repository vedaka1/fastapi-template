from dataclasses import dataclass

from src.domain.common.exceptions import ApplicationException


@dataclass
class UserAlrearedyExistException(ApplicationException):
    message = 'User already exist'
    status_code = 409
