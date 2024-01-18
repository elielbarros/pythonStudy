"""
# English
- string.Template -

string.Template is a class in the string module in Python that offers a simple and safe approach to performing string
substitutions. It is designed to be a safe and easy-to-use alternative to string formatting, especially when
replacement values come from untrusted sources such as user input.

The main feature of string.Template is replacement based on placeholders called "replaceables". These markers are
delimited by curly braces {} and can contain names or indices, depending on the approach chosen.

doc: https://docs.python.org/3/library/string.html#template-strings

# Portuguese
- string.Template -

string.Template é uma classe no módulo string em Python que oferece uma abordagem simples e segura para realizar
substituições em strings. Ela foi projetada para ser uma alternativa segura e fácil de usar para a formatação de
strings, especialmente quando os valores de substituição vêm de fontes não confiáveis, como entradas do usuário.

A principal característica de string.Template é a substituição baseada em marcadores de lugar chamados de
"substituíveis". Esses marcadores são delimitados por chaves {} e podem conter nomes ou índices, dependendo da
abordagem escolhida.

doc: https://docs.python.org/3/library/string.html#template-strings
"""
import json
import locale
import os
import string
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


def convert_to_brl(number: float) -> str:
    # locale.currency
    # format monetary values according to the system's regional and cultural settings (locale)
    brl = locale.currency(val=number, symbol=True, grouping=True)
    return brl


print(convert_to_brl(100))

date_ = datetime(2022, 12, 28)
data_ = dict(
        name='Joao',
        value=convert_to_brl(1_234_456),
        date=date_.strftime('%d/%m/%Y'),
        company='O. M.',
        phone='+123 (12) 3456-7890'
)

result = json.dumps(data_, indent=2)
print(result)

FILE_ABSOLUT_PATH = os.path.abspath(
        os.path.join(
                os.path.dirname(__file__),
                'static',
                'class_298.txt'
        )
)

with open(FILE_ABSOLUT_PATH, 'r') as file_:
    template_ = string.Template(file_.read())
    # Will generate errors if there is
    message = template_.substitute(data_)
    print(message)

    # Will not generate errors
    another_message = template_.safe_substitute(data_)
    print(f'anonther message = {another_message}')


# It is also possible to override Template
class MyTemplate(string.Template):
    delimiter = '%'


DELIMITER_ABSOLUT_PATH = os.path.abspath(
        os.path.join(
                os.path.dirname(__file__),
                'static',
                'class_298_delimiter_%.txt'
        )
)

with open(DELIMITER_ABSOLUT_PATH, 'r') as file_:
    template_ = MyTemplate(file_.read())
    # Will generate errors if there is
    message = template_.substitute(data_)
    print(message)

    # Will not generate errors
    another_message = template_.safe_substitute(data_)
    print(f'anonther message = {another_message}')