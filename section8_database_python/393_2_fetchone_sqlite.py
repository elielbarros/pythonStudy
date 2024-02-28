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
cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = 2')

# Printing one information loaded from database
# After read cursor, the information will be lost and it will not be possible to make another
row = cursor.fetchone()
print(row)

# Always close connection and cursor
cursor.close()
connection.close()
