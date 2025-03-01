import os
from dataclasses import dataclass


@dataclass
class PostgresqlConfig:
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DB_URL(self) -> str:
        return 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}'.format(
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            db=self.POSTGRES_DB,
        )

    @staticmethod
    def load_from_env() -> 'PostgresqlConfig':
        return PostgresqlConfig(
            str(os.getenv('POSTGRES_HOST', 'postgres')),
            int(os.getenv('POSTGRES_PORT', 5432)),
            str(os.getenv('POSTGRES_USER')),
            str(os.getenv('POSTGRES_PASSWORD')),
            str(os.getenv('POSTGRES_DB')),
        )


@dataclass
class AppConfig:
    db: PostgresqlConfig

    def load_from_env(self) -> 'AppConfig':
        return AppConfig(
            PostgresqlConfig.load_from_env(),
        )
