"""
# English
How formats an existent date to a format specified
    - datetime_value.strftime(format_expected)

# Portuguese
Como formatar uma data existente para um formato especificado
    - datetime_value.strftime(formato_especificado)
"""
from datetime import datetime

format_ = '%Y/%m/%d'

datetime_ = datetime.strptime('06/01/2024 14:05:00', '%d/%m/%Y %H:%M:%S')

print(datetime_.strftime(format_))  # output: 2024/01/06

format_ = '%Y'
print(datetime_.strftime(format_))  # output: 2024

format_ = '%m'
print(datetime_.strftime(format_))  # output: 01

format_ = '%d'
print(datetime_.strftime(format_))  # output: 06
