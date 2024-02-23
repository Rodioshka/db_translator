import logging

from dotenv import dotenv_values
from dataclasses import dataclass

from usecases.types import DataBasesTypesEnum

config = dotenv_values('.env')
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@dataclass(frozen=True)
class DataBaseConfig:
    DB_TYPE: DataBasesTypesEnum

    USERNAME: str = config.get('DB_USERNAME')
    PASSWORD: str = config.get('DB_PASSWORD')
    HOST: str = config.get('DB_HOST')
    PORT: str = config.get('DB_PORT')
    DATABASE: str = config.get('DB_DATABASE')
