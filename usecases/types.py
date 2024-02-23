from dataclasses import dataclass, field
from enum import Enum
from typing import List


class DataBasesTypesEnum(Enum):
    """
    Get database name and driver in value
    """
    postgresql = 'psycopg2'


@dataclass
class Column:
    column_name: str
    column_type: str
    column_description: str
    nullable: bool

    ref_table: str = ''
    ref_columns: list = field(default_factory=list)


@dataclass
class Table:
    schema_name: str
    table_name: str
    table_description: str = None
    columns: List[Column] = field(default_factory=list)
