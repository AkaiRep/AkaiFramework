import inspect
import sqlite3
import sys
import models

def parse_classes(classes):
    prohibited,allowed = ["Enum","SQLField","SQLFieldTypes","SQLFieldTypes","SQLTable"],[]

    for item in classes: 
        if item[0] not in prohibited: allowed.append(item[1])

    return allowed


def get_migration_expressions():

    models_classes = inspect.getmembers(sys.modules["models"], inspect.isclass)
    list_of_classes = parse_classes(models_classes)
    expressions = []

    for item in list_of_classes: print("[+] found", item.name,"model")

    for item in list_of_classes:

        expression = "CREATE TABLE " + item.name + " ( "
        for field in item.fields:
            expression += str(field) + ", " if item.fields.index(field) != len(item.fields)-1 else str(field)
        expression+=" );";expressions.append(expression)

    return expressions


def make_migration():

    try:
        sqlite_connection = sqlite3.connect('sqlite.db')
        
        expressions = get_migration_expressions()
        cursor = sqlite_connection.cursor()
        print("[*] Connected to DB")

        for expression in expressions:
            try:
                cursor.execute(expression)
                print("[+] Migration maked succesful")
                sqlite_connection.commit()
            except sqlite3.Error as error:
                print("[!] SQL Error:", error)
        
        cursor.close()

    except sqlite3.Error as error:
        print("[!] Cannot connect to DB", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("[!] Connection with DB was closed")
            
make_migration()