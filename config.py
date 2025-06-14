from dataclasses import dataclass

from src.main.environment import get_env_var


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

    @classmethod
    def load_from_env(cls) -> 'PostgresqlConfig':
        return cls(
            get_env_var('POSTGRES_HOST', str, default='postgres'),
            get_env_var('POSTGRES_PORT', int, default=5432),
            get_env_var('POSTGRES_USER', str),
            get_env_var('POSTGRES_PASSWORD', str),
            get_env_var('POSTGRES_DB', str),
        )


@dataclass
class AppConfig:
    db: PostgresqlConfig

    @classmethod
    def load_from_env(cls) -> 'AppConfig':
        return cls(
            PostgresqlConfig.load_from_env(),
        )
