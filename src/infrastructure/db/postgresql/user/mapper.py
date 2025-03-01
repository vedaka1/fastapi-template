from src.domain.user.entity import User
from src.infrastructure.db.postgresql.user.model import UserModel


def map_model_to_user(model: UserModel) -> User:
    return User(
        uuid=model.uuid,
        username=model.username,
        first_name=model.first_name,
        last_name=model.last_name,
        middle_name=model.middle_name,
    )
