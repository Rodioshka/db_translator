from typing import List
import datetime
from usecases.types import Column, Table
from db.db_interface import DataBaseInterface


class DataBaseStructureUseCase:
    def __init__(self, interface: DataBaseInterface):
        self.interface = interface
        self.data = dict()
        self.data['meta'] = {
            'created_dt': datetime.datetime.now()
        }

    def execute(self) -> None:
        schemes = self.interface.get_schemes()
        data = list()
        for schema in schemes:
            if schema != 'information_schema':
                tables = self.interface.get_tables(schema_name=schema)

                for table in tables:
                    columns = self.interface.get_columns(table_name=table, schema_name=schema)
                    table_references = self.interface.get_fk(table_name=table, schema_name=schema)
                    table_description = self.interface.get_table_description(table_name=table, schema_name=schema)

                    tb_columns = self.get_table_columns(
                        columns=columns,
                        relationships=table_references
                    )

                    data.append(
                        Table(
                            schema_name=schema,
                            table_name=table,
                            table_description=table_description.get('text'),
                            columns=tb_columns

                        )
                    )
        self.data['data'] = data

    @staticmethod
    def get_column_relationship(column_name: str, relationships: List[dict]) -> tuple:
        for value in relationships:
            if column_name in value.get('constrained_columns'):
                return (
                    value.get('referred_table'),
                    value.get('referred_columns')
                )

    @staticmethod
    def get_table_columns(columns: List[dict], relationships: List[dict]) -> list:
        data_columns = list()
        for column in columns:

            ref_table = None
            ref_columns = None

            for value in relationships:
                if column.get('name') in value.get('constrained_columns'):
                    ref_table, ref_columns = (
                        value.get('referred_table'),
                        value.get('referred_columns')
                    )

            # print(ref_table, ref_columns)

            data_columns.append(
                Column(
                    column_name=column.get('name'),
                    column_type=column.get('type'),
                    column_description=column.get('comment'),
                    nullable=column.get('nullable'),
                    ref_table=ref_table,
                    ref_columns=ref_columns,
                )
            )
        return data_columns


class DataBaseDataExampleUseCase:
    """
    Получение примеров данных, содержащихся в таблице
    """
    pass
