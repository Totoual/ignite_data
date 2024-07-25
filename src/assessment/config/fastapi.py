from .config import config


class FastApiConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+asyncpg://{config.db_user}:{config.db_password}"
        + f"@{config.db_host}:{config.db_port}/{config.db_name}"
    )
