import json

from config import DataBaseConfig, DocumentConfig

from usecases.types import DataBasesTypesEnum
from usecases.db_cases import DataBaseStructureUseCase
from usecases.document_cases import CreateDocumentUseCase
from db.db_connector import DataBaseConnection
from db.db_interface import DataBaseInterface


def main() -> None:
    db_config = DataBaseConfig(DB_TYPE=DataBasesTypesEnum.postgresql)
    connection = DataBaseConnection(config=db_config)

    db_interface = DataBaseInterface(engine=connection.engine)

    dbs = DataBaseStructureUseCase(interface=db_interface)
    dbs.execute()
    # Сохранение словаря в файл
    with open('results/data.json', 'w', encoding='utf-8') as f:
        json.dump(dbs.data, f, ensure_ascii=False, indent=4)

    document_wrk = CreateDocumentUseCase()
    document_wrk.execute(
        template_name=DocumentConfig.DOCUMENT_TEMPLATE,
        template_path=DocumentConfig.DOCUMENT_TEMPLATE_PATH,
        file_name=DocumentConfig.DOCUMENT_NAME,
        file_format=DocumentConfig.DOCUMENT_EXT,
        data=dbs.data
    )


if __name__ == '__main__':
    main()
