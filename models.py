from sql_utility import SQLField
from sql_utility import SQLFieldTypes
from sql_utility import SQLTable


class ExampleTable(SQLTable):

    name = "example"
    fields = [
        SQLField("id", SQLFieldTypes.INTEGER,True,True,False),
        SQLField("integer_field", SQLFieldTypes.INTEGER),
        SQLField("text_field", SQLFieldTypes.TEXT),
    ]

    