from pathlib import Path

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
DESTINATION_PATH = STATIC_PATH / 'dest'
WORKBOOK_PATH = STATIC_PATH / 'workbook.xlsx'

# Another way to create sheet
workbook = Workbook()

# Giving a name for the sheet
sheet_name = 'My Sheet'
workbook.create_sheet(sheet_name, index=0)

# Activating worksheet and select for the sheet 'My Sheet'
worksheet: Worksheet = workbook[sheet_name]

# Removing the default sheet
workbook.remove(workbook['Sheet'])

print(workbook.sheetnames)  # output: ['My Sheet']

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

for student in students:
    worksheet.append(student)

workbook.save(WORKBOOK_PATH)
