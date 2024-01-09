"""
# English
How check a date is greater than another date
     - end_date > start_date

How calc the difference between two different dates
    - delta = date_a - date_b
    - delta will be 'datetime.timedelta'

datetime.timedelta
    - https://docs.python.org/3/library/datetime.html#timedelta-objects
    - days=
    - hours=
    - minutes=
    - secods=
    - miliseconds=
    - microseconds=

dateutil.relativedelta
    - https://dateutil.readthedocs.io/en/stable/relativedelta.html
    - pip install python-dateutil types-python-dateutil
    - day, days, hour, hours, leapdays, microsecond, microseconds, minutes, months
    - Sum: end_date + relativedelta(seconds=50)
    - Difference between dates: relativedelta(end_date, start_date)

# Portuguese
Como checar se uma data estah posterior a outra data
    - end_date > start_date

Como calcular a diferenca entre duas datas
    - delta = date_a - date_b
    - delta will be 'datetime.timedelta'

datetime.timedelta
    - https://docs.python.org/3/library/datetime.html#timedelta-objects
    - days=
    - hours=
    - minutes=
    - secods=
    - miliseconds=
    - microseconds=

dateutil.relativedelta
    - https://dateutil.readthedocs.io/en/stable/relativedelta.html
    - pip install python-dateutil types-python-dateutil
    - day, days, hour, hours, leapdays, microsecond, microseconds, minutes, months
    - Sum: end_date + relativedelta(seconds=50)
    - Difference between dates: relativedelta(end_date, start_date)
"""
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

format_ = '%d/%m/%Y %H:%M:%S'
start_date = datetime.strptime('12/04/1975 20:34:00', format_)
end_date = datetime.strptime('07/01/2024 22:14:00', format_)

print(end_date > start_date)  # output: True
print(end_date < start_date)  # output: False
print(end_date == start_date)  # output: False

delta = end_date - start_date
print(delta)  # output: 17802 days, 1:40:00
print(delta.days, delta.seconds, delta.microseconds, delta.total_seconds())  # output: 17802 6000 0 1538098800.0
print(type(delta))  # output: <class 'datetime.timedelta'>

# Sum 10 days and 1 hour into end_date
delta = timedelta(days=10, hours=1)
new_end_date = end_date + delta
print(end_date, new_end_date, sep=' || ')  # 2024-01-07 22:14:00 || 2024-01-17 23:14:00

# Sum 50 seconds into end_date
end_date_relative_timedelta = end_date + relativedelta(seconds=50)
print(end_date, end_date_relative_timedelta, sep=' || ')  # output: 2024-01-07 22:14:00 || 2024-01-07 22:14:50

# The difference between days
relativedelta_date = relativedelta(end_date, start_date)
print(relativedelta_date)  # output: relativedelta(years=+48, months=+8, days=+26, hours=+1, minutes=+40)
