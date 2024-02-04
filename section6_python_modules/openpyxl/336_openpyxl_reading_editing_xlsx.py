from pathlib import Path

from openpyxl import Workbook
# TO READ A WORKBOOK IT IS NECESSARY USE load_workbook
from openpyxl import load_workbook
# TYPING CELL
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

ROOT_PATH = Path(__file__).parent
STATIC_PATH = ROOT_PATH / 'static'
DESTINATION_PATH = STATIC_PATH / 'dest'
WORKBOOK_PATH = STATIC_PATH / 'workbook.xlsx'

# LOADING FILE XLSX
loaded_workbook: Workbook = load_workbook(WORKBOOK_PATH)

# DECLARE SHEET NAME
sheet_name = 'My Sheet'

# ACTIVATING SHEET THAT WILL BE USED
worksheet: Worksheet = loaded_workbook[sheet_name]

# TO START AFTER HEADER ROW USE MIN_ROW = 2
row: tuple[Cell]
for row in worksheet.iter_rows(min_row=2):
    # TO GET TYPING OF CLASS CELL IMPORT from openpyxl.cell import Cell
    for cell in row:
        print(cell.value, end='\t')

        # CHANGING MARIA AGE VERIFYING FOR HER NAME
        if cell.value == 'Maria':
            worksheet.cell(cell.row, 2, value='13')
    print()

# PRINT A SPECIFIC CELL
cell_maria_age: Cell = worksheet['B3']
print(cell_maria_age.value)  # output: 13

# CHANGING MARIA AGE
cell_maria_age.value = 14

loaded_workbook.save(WORKBOOK_PATH)
