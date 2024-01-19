"""
# English
- Ambient Environment -
Each operating system maintains a set of environment variables that contain information about system configuration,
user preferences, and other properties of the environment. Additionally, users can define their own environment
variables to customize the execution of programs and scripts.

- os.environ -
List all system and local environment variables

- os.getenv('ENVIRONMENT_NAME') -
Returns the value of the environment variable

- load_dotenv(.env path) -
pip install python-dotenv
https://pypi.org/project/python-dotenv/
NOTE: ALWAYS REMEMBER TO CREATE A .env-example

# Portuguese
- Variaveis de Ambiente -

Cada sistema operacional mantém um conjunto de variáveis de ambiente que contém informações sobre a configuração do
sistema, preferências do usuário e outras propriedades do ambiente. Além disso, os usuários podem definir suas
próprias variáveis de ambiente para personalizar a execução de programas e scripts.

- os.environ -
Lista todos as variaveis de ambiente do sistema e local

- os.getenv('ENVIRONMENT_NAME') -
Retorna o valor da variavel de ambiente

- load_dotenv(.env path) -
pip install python-dotenv
https://pypi.org/project/python-dotenv/
OBS.: SEMPRE LEMBRE-SE DE CRIAR UM .env-example
"""
import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / 'static' / '.env'

print(dotenv_path)

print(load_dotenv(dotenv_path))

print(os.environ)
print(os.environ['USER_DB'])  # output: user
print(os.environ['PASSWORD_DB'])  # output: password

print(os.getenv('USER_DB'))  # output: user
print(os.getenv('PASSWORD_DB'))  # output: password
