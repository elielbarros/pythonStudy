from pathlib import Path

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
DESTINATION_PATH = STATIC_PATH / 'dest'
WORKBOOK_PATH = STATIC_PATH / 'workbook.xlsx'
WORKBOOK_FOR_PATH = STATIC_PATH / 'workbook_FOR.xlsx'

workbook = Workbook()

# It is important to import Worksheet to see the list of methods available for a Worksheet instance.
# Worksheet will be the table that starts with an Excel.
worksheet: Worksheet = workbook.active

# Now that worksheet was activated it is possible to create a header for table
# To do that it is necessary to use the method cell()
# Creating header
worksheet.cell(row=1, column=1, value='Name')
worksheet.cell(row=1, column=2, value='Age')
worksheet.cell(row=1, column=3, value='Score')

students = [
    ['Joao', 14, 5.5],
    ['Maria', 13, 9.7],
    ['Luiz', 15, 8.8],
    ['Alberto', 16, 10],
]

for i, student in enumerate(students, start=2):
    for j, student_column in enumerate(student, start=1):
        # Creating row values
        worksheet.cell(row=i, column=j, value=student_column)

workbook.save(WORKBOOK_FOR_PATH)

# Another way to create sheet using the method append()
workbook = Workbook()
worksheet: Worksheet = workbook.active

worksheet.cell(row=1, column=1, value='Name')
worksheet.cell(row=1, column=2, value='Age')
worksheet.cell(row=1, column=3, value='Score')

for student in students:
    worksheet.append(student)

workbook.save(WORKBOOK_PATH)
