from config import DataBaseConfig

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
    CreateDocumentUseCase.execute(template_name='markdown_template.md_tmp', data=dbs.data)


if __name__ == '__main__':
    main()
