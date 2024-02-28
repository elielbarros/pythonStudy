import sqlite3
from pathlib import Path

# Documentation: https://www.sqlite.org/doclist.html
# Another Documentation: https://www.techonthenet.com/sqlite/index.php

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)

# The cursor will be created to execute query to database
cursor = connection.cursor()

# Executing select to database
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# Printing information loaded from database
for row in cursor.fetchall():
    print(row)
    # _id = row[0]
    # name = row[1]
    # weight = row[2]
    _id, name, weight = row
    print(_id, name, weight)

print()

# To maintain information about what was loaded convert fetchall to list
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

list_ = list(cursor.fetchall())
for row in list_:
    print(row)

# Always close connection and cursor
cursor.close()
connection.close()
