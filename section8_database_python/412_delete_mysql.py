# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import os
from pathlib import Path

import dotenv
import pymysql

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
    database=os.environ['MYSQL_DATABASE']
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
        # Insert data using tuple
        query = f"""INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)"""
        data = ('John', 35)
        result = cursor.execute(query, data)
        print(result)

        # Insert data using dict
        query = f"""INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s)"""
        data = {
            'name': 'Mary',
            'age': 50
        }
        result = cursor.execute(query, data)
        print(result)

        # Insert many data using tuple, query cannot have named params
        query = f"""INSERT INTO {TABLE_NAME} (name, age) VALUES (%s, %s)"""
        data = (
            ('Zaqiel', 47),
            ('Harut', 39)
        )
        result = cursor.executemany(query, data)
        print(result)

        # Insert many data using dict, query must have named params
        query = f"""INSERT INTO {TABLE_NAME} (name, age) VALUES (%(name)s, %(age)s)"""
        data = [
            {'name': 'Ariel', 'age': 81},
            {'name': 'Raphael', 'age': 96}
        ]
        result = cursor.executemany(query, data)
        print(result)

        connection.commit()

    # Create a SELECT query to database
    with connection.cursor() as cursor:
        # Select all data from database
        query = f"""SELECT * FROM {TABLE_NAME}"""

        # Execute query to database
        cursor.execute(query)

        query_result = cursor.fetchall()
        print(query_result)

        for row in query_result:
            print(row)

        # Select specific data using where and placeholder
        query = f"""SELECT * FROM {TABLE_NAME} WHERE id = %s"""
        _id = 3

        # Execute query to database
        cursor.execute(query, _id)

        # Print result
        query_result = cursor.fetchall()
        print(f'{query_result=}')

    # Create a DELETE query to database
    with connection.cursor() as cursor:
        # Delete data from database by id
        query = f"""DELETE FROM {TABLE_NAME} WHERE id = %s"""

        _id = 3

        # Execute query to database
        result = cursor.execute(query, _id)

        connection.commit()

        query = f"""SELECT * FROM {TABLE_NAME}"""
        cursor.execute(query)

        query_result = cursor.fetchall()
        print(query_result)

        for row in query_result:
            print(row)
