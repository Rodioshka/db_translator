import logging

from dotenv import dotenv_values
from dataclasses import dataclass

from usecases.types import DataBasesTypesEnum

config = dotenv_values('.env')
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@dataclass(frozen=True)
class DocumentConfig:
    DOCUMENT_NAME: str = 'Отчет'
    DOCUMENT_TEMPLATE: str = 'markdown_template.md_tmp'
    DOCUMENT_EXT: str = 'md'
    DOCUMENT_TEMPLATE_PATH: str = 'service/templates'


@dataclass(frozen=True)
class DataBaseConfig:
    DB_TYPE: DataBasesTypesEnum

    USERNAME: str = config.get('DB_USERNAME')
    PASSWORD: str = config.get('DB_PASSWORD')
    HOST: str = config.get('DB_HOST')
    PORT: str = config.get('DB_PORT')
    DATABASE: str = config.get('DB_DATABASE')
