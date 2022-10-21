from enum import Enum


class SQLTable:
    fields = []

    def __init__(self, name):
        self.name = name

    def add_field(self, field):
        self.fields.append(field)

    def __str__(self):
        fields = [str(field) for field in self.fields]
        return f'CREATE TABLE {self.name} ({", ".join(fields)});'


class SQLFieldTypes(Enum):
    INTEGER = "INTEGER"
    TEXT = "TEXT"


class SQLField:
    def __init__(self, name: str, type: SQLFieldTypes, primary_key: bool = False, auto_increment: bool = False, nullable: bool = False):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.nullable = nullable

    def __str__(self):
        primary_key_str = " PRIMARY KEY" if self.primary_key else ""
        auto_increment_str = " AUTOINCREMENT" if self.auto_increment else ""
        nullable_str = " NULL" if self.nullable else " NOT NULL"

        parameters = primary_key_str + auto_increment_str + nullable_str

        return f'{self.name} {self.type.value}{parameters}'