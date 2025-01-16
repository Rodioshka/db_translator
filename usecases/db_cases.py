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
    # TODO: Надо еще добавить в сами данные индексы и pk
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
                    table_pkey_constrains = self.interface.get_pk_constraint(table_name=table, schema_name=schema)
                    table_pkey_index, table_pkey_columns = table_pkey_constrains.get('name'), table_pkey_constrains.get(
                        'constrained_columns')
                    table_indexes = self.interface.get_indexes(table_name=table, schema_name=schema)

                    tb_columns = self.get_table_columns(
                        columns=columns,
                        relationships=table_references,
                        table_indexes=table_indexes,
                        table_pkey_index=table_pkey_index,
                        table_pkey_columns=table_pkey_columns
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
    def get_table_columns(columns: List[dict], relationships: List[dict], table_pkey_index: str = None,
                          table_pkey_columns: list = None, table_indexes: list = None) -> list:
        data_columns = list()
        for column in columns:

            ref_table = None
            ref_columns = None
            is_index = False
            is_pk = False
            index_name = None
            is_unique_index = None

            for value in relationships:
                if column.get('name') in value.get('constrained_columns'):
                    ref_table, ref_columns = (
                        value.get('referred_table'),
                        value.get('referred_columns')
                    )

            if table_pkey_columns:
                if column.get('name') in table_pkey_columns:
                    is_pk = True

            if table_indexes:
                for index in table_indexes:
                    if column.get('name') in index.get('column_names', None):
                        is_index = True
                        index_name = index.get('name', None)
                        is_unique_index = index.get('unique', None)


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

