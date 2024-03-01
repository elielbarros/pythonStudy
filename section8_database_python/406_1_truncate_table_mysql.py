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
