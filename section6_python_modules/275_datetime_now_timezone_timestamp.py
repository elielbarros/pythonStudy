"""
# English
How get current date and time
    - datetime.now() will return actual date and time

How get current date and time with time zone
    - It is necessary the library 'pytz'
    - pip install pytz types-pytz
    - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

How get Unix Timestamp
    - https://pt.wikipedia.org/wiki/Era_Unix
    - Will return number in seconds from 1970 to today

# Portuguese
Como pegar a data e o tempo atual
    - datetime.now() vai retornar a data e o tempo atual

Como capturar a data e o tempo atual com timezone
    - Eh necessario a biblioteca 'pytz'
    - pip install pytz types-pytz
    - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    - datetime.now(timezone('TZ_Identifier'))
"""
from datetime import datetime

from pytz import timezone

date = datetime.now()
print(date)  # output: 2024-01-07 20:10:56.429987

date_with_tz = datetime.now(timezone('America/Bahia'))
print(date_with_tz)  # output: 2024-01-07 20:20:24.118879-03:00

date_japan = datetime.now(timezone('Asia/Tokyo'))
print(date_japan)  # output: 2024-01-08 08:22:16.736607+09:00

custom_date_canadian = datetime(day=7, month=1, year=2024, tzinfo=timezone('Canada/Atlantic'))
print(custom_date_canadian)  # output: 2024-01-07 00:00:00-04:14

actual_timestamp = date.timestamp()
print(actual_timestamp)  # output: 1704670089.082985

date_from_timestamp = datetime.fromtimestamp(actual_timestamp)
print(date_from_timestamp)  # output: 2024-01-07 20:28:47.768634