import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)

# It will be created the cursor to execute query to database
cursor = connection.cursor()

# SQL execution



# Always close connection and cursor
cursor.close()
connection.close()