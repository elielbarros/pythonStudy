# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
from pathlib import Path

import dotenv
# import pymysql
import pymysql.cursors  # use pymysql.cursors and include to pymysql.connect DictCursor and receive a dict as response

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
ENV_PATH = STATIC_PATH / '.env'
TABLE_NAME = 'customers'

# Using python-dotenv to load environment file .env
dotenv.load_dotenv(ENV_PATH)

# Opening connection with MySQL database using os.environ to load information from environment file .env
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)

# Using context manager to automatically close connection and cursor
# The query to create a table cannot be reversed, because of that, it is not necessary to commit
with connection:
    with connection.cursor() as cursor:
        query = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        PRIMARY KEY (id)
        )"""
        cursor.execute(query)

        # Cleaning table using TRUNCATE
        query = f'TRUNCATE TABLE {TABLE_NAME}'
        cursor.execute(query)
        connection.commit()

    # Using cursor to insert into customers a customer with a placeholder to prevent SQL Injection
    with connection.cursor() as cursor:
        # Insert many data using dict, query must have named params
        query = f"""INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s)"""
        data = [
            {'name': 'John', 'age': 35},
            {'name': 'Mary', 'age': 50},
            {'name': 'Zaqiel', 'age': 47},
            {'name': 'Harut', 'age': 39},
            {'name': 'Ariel', 'age': 81},
            {'name': 'Raphael', 'age': 96}
        ]
        result = cursor.executemany(query, data)

        connection.commit()

        # How print Cursor Last Row Id created
        # In execute many last row id will return first created id
        # But when inserting one using execute, will return last row id
        print(f'last row id created: {cursor.lastrowid}')

    # Create a SELECT query to database
    with connection.cursor() as cursor:
        # Select all data from database
        query = f"""SELECT * FROM {TABLE_NAME}"""

        # Execute query to database
        cursor_result = cursor.execute(query)

        # Cursor Result Size
        print(f'cursor result size: {cursor_result}')  # output: cursor result size: 6

        # Data Result Size = Cursor Result Size
        print(f'Data result size: {len(cursor.fetchall())}')  # output: cursor result size: 6

        # Cursor Row Count
        print(f'Cursor row count: {cursor.rowcount}')  # output: Cursor row count: 6

        # Last row id brute force
        query = f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        cursor.execute(query)

        last_id_from_select = cursor.fetchone()
        print(f'Last row id brute force: {last_id_from_select}')  # output: Last row id brute force: {'id': 6}
