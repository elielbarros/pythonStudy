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
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, weight REAL)'
)

connection.commit()

# Always close connection and cursor
cursor.close()
connection.close()
