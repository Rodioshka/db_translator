from sqlalchemy import create_engine

from config import DataBaseConfig


class DataBaseConnection:
    def __init__(self, config: DataBaseConfig):
        db = config.DB_TYPE
        self.engine = create_engine(
            f'{db.name}+{db.value}://{config.USERNAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DATABASE}'
        )
