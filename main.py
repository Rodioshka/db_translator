from config import DataBaseConfig, DocumentConfig

from usecases.types import DataBasesTypesEnum
from usecases.usecases import DataBaseStructureUseCase, CreateDocumentUseCase
from db.db_connector import DataBaseConnection
from db.db_interface import DataBaseInterface


def main() -> None:
    db_config = DataBaseConfig(DB_TYPE=DataBasesTypesEnum.postgresql)
    connection = DataBaseConnection(config=db_config)

    db_interface = DataBaseInterface(engine=connection.engine)

    dbs = DataBaseStructureUseCase(interface=db_interface)
    dbs.execute()

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
