import sqlite3
from pathlib import Path

# Documentation: https://www.sqlite.org/doclist.html
# Another Documentation: https://www.techonthenet.com/sqlite/index.php

# CRUD  - CREATE    READ    UPDATE  DELETE
# SQL   - INSERT    SELECT  UPDATE  DELETE

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)

# It will be created the cursor to execute query to database
cursor = connection.cursor()

# SQL execution
# Asking to delete everything on table
# Be careful with delete without WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Committing last delete query requested
connection.commit()

# Asking to delete the sequence that maintain the sequence id from table
# This will reset id count
# DELETE MUST HAVE WHERE TO DETERMINE WHAT WILL BE DELETED
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

# Committing last delete sequence requested
connection.commit()

# Asking to create table customers with column id, name and weight
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
)

# Committing last create query requested
connection.commit()

# SQL to insert values to table using binding
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)'

dict_list = [
    {"name": "John Doe", "weight": 64.2},
    {"name": "Mary Jane", "weight": 32.8}
]

# Executing query to insert a dictionary list
cursor.executemany(sql, dict_list)

# Committing last insert query requested
connection.commit()

# Executing DELETE to database
cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 2')

# Committing delete query requested
connection.commit()

# Executing UPDATE to database
cursor.execute(f'UPDATE {TABLE_NAME} SET name="UPDATED", weight=61.2 WHERE id = 1')

# Committing UPDATE query requested
connection.commit()

# Always close connection and cursor
cursor.close()
connection.close()
