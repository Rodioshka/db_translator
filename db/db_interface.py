from sqlalchemy import inspect, engine


class DataBaseInterface:
    def __init__(self, engine: engine):
        self.engine = engine

    def get_schemes(self) -> list:
        return inspect(self.engine).get_schema_names()

    def get_tables(self, schema_name: str = 'public') -> list:
        return inspect(self.engine).get_table_names(schema=schema_name)

    def get_table_description(self, table_name: str, schema_name: str = 'public') -> dict:
        return inspect(self.engine).get_table_comment(schema=schema_name, table_name=table_name)

    def get_columns(self, table_name: str, schema_name: str = 'public') -> list:
        return inspect(self.engine).get_columns(schema=schema_name, table_name=table_name)

    def get_constraints(self, table_name: str, schema_name: str = 'public') -> list:
        return inspect(self.engine).get_check_constraints(schema=schema_name, table_name=table_name)

    def get_fk(self, table_name: str, schema_name: str = 'public'):
        return inspect(self.engine).get_foreign_keys(schema=schema_name, table_name=table_name)

    def get_indexes(self, table_name: str, schema_name: str = 'public'):
        return inspect(self.engine).get_indexes(schema=schema_name, table_name=table_name)

    def get_multi_check_constraints(self, table_name: str, schema_name: str = 'public'):
        return inspect(self.engine).get_multi_check_constraints(schema=schema_name, table_name=table_name)

    def get_pk_constraint(self, table_name: str, schema_name: str = 'public'):
        return inspect(self.engine).get_pk_constraint(schema=schema_name, table_name=table_name)