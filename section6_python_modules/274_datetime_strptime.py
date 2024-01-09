"""
# English
How create date and datetime using the class datetime

Specifying only Date
datetime_ = datetime(year, month, day)

Specifying Date and Time
datetime_ = datetime(year, month, day, hour, minute, second, microsecond)

Documentation - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
Using a date as String and specifying date format
date_converted = datetime.strptime('DATE_AS_STRING', 'DATE_FORMAT')


# Portuguese
Como criar data e data e horario usando a classe datetime

Especificando apenas data
datetime_ = datetime(year, month, day)

Especificando data e horario
datetime_ = datetime(year, month, day, hour, minute, second, microsecond)

Documentacao - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
Usando a data como String e especificando o formato da data
date_converted = datetime.strptime('DATE_AS_STRING', 'DATE_FORMAT')
"""

from datetime import datetime

date_ = datetime(2022, 1, 6)
print(date_)  # output: 2022-04-20 00:00:00

datetime_ = datetime(2022, 1, 6, 23, 59, 59)
print(datetime_)  # output: 2022-04-20 23:59:59

date_converted = datetime.strptime('06/01/2024', '%d/%m/%Y')
print(date_converted, type(date_converted))  # output: 2024-01-06 00:00:00 <class 'datetime.datetime'>

datetime_converted = datetime.strptime('06/01/2024 14:05:00', '%d/%m/%Y %H:%M:%S')
print(datetime_converted, type(datetime_converted))  # output: 2024-01-06 14:05:00 <class 'datetime.datetime'>

