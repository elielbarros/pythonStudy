import sqlite3
from pathlib import Path

# Documentation: https://www.sqlite.org/doclist.html
# Another Documentation: https://www.techonthenet.com/sqlite/index.php

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
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

# Committing last delete sequence requested
connection.commit()

# Asking to create table customers with column id, name and weight
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
)

# Committing last create query requested
connection.commit()

# Ask to insert values to table
# Use .execute to execute one query
# cursor.execute('')
# Use .executemany to execute many queries
# Be Careful with SQL Injection!
# Pay Attention it is not necessary to inform id, so it will be removed from query
# sql = f'INSERT INTO {TABLE_NAME} (id, name, weight) VALUES '
# f'(NULL, "John Doe", 1.1), '
# f'(NULL, "Mary Jane", 23.3), '
# f'(NULL, "Peter Park", 87.3)'
# It will be used to prevent SQL INJECTION "binding" represented by '?'
# sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
# To insert many values use execute many
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'

# Using binding it is necessary to use __parameters and send an array with values that will fill the binding
cursor.executemany(sql, [
    ['John Doe', 64.2],
    ['Mary Jane', 32.8]
])

# Committing last insert query requested
connection.commit()

# Always close connection and cursor
cursor.close()
connection.close()
