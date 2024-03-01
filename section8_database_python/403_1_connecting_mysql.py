# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql

# Opening connection with MySQL database
connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='base_de_dados'
)

# Creating cursor to execute queries
cursor = connection.cursor()

# Execute queries here

# Closing cursor
cursor.close()

# Closing connection with MySQL
connection.close()
