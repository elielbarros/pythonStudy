"""
# English
The calendar library in Python provides calendar-related functions. It offers several utilities for manipulating and
displaying information related to dates and calendars.

Doc: https://docs.python.org/3/library/calendar.html

# Portuguese
A biblioteca calendar em Python fornece funções relacionadas a calendários. Ela oferece diversas utilidades para
manipulação e exibição de informações relacionadas a datas e calendários.

Doc: https://docs.python.org/3/library/calendar.html
"""
import calendar

print(calendar.calendar(2024))

print(calendar.month(2024, 1))

first_january_day, total_days_january = calendar.monthrange(2024, 1)
print(first_january_day)  # (0, Monday) ~ (6, Sunday) | output: 0 = Monday
print(total_days_january)  # output: 31
# Get first day name
print(calendar.day_name[first_january_day])  # output: Monday
# Get last day name
print(calendar.day_name[calendar.weekday(2024, 1, total_days_january)])  # output: Wednesday

print(list(enumerate(calendar.day_name)))

# Get all week from a month
print(calendar.monthcalendar(2024, 1))

for week_ in calendar.monthcalendar(2024, 1):
    print(list(enumerate(week_)))
    for day_ in week_:
        if day_ == 0:
            continue
        print(day_)
