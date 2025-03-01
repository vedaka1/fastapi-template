from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.postgresql.common.models.base import Base


class UserModel(Base):
    __tablename__ = 'users'

    uuid: Mapped[UUID] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str | None] = mapped_column(nullable=True)
    last_name: Mapped[str | None] = mapped_column(nullable=True)
    middle_name: Mapped[str | None] = mapped_column(nullable=True)


class UserModelTest(Base):
    __tablename__ = 'users_test'

    uuid: Mapped[UUID] = mapped_column(primary_key=True, index=True)
