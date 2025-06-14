from src.infrastructure.db.postgresql.common.filters.base import BaseFiltersImpl
from src.infrastructure.db.postgresql.common.filters.utils import create_search_string
from src.infrastructure.db.postgresql.user.model import UserModel


class UserFiltersImpl(BaseFiltersImpl[UserModel]):
    def __init__(self, model: type[UserModel]) -> None:
        self.search_string = lambda v: create_search_string(
            [model.username, model.first_name, model.last_name, model.middle_name],
            v,
        )
        self.username = lambda v: model.username == v
        self.first_name = lambda v: model.first_name == v
        self.last_name = lambda v: model.last_name == v
        self.middle_name = lambda v: model.middle_name == v
        self.uuid_in = lambda v: model.uuid.in_(v)
