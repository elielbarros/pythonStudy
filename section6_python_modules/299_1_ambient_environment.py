"""
# English
- Ambient Environment -
Each operating system maintains a set of environment variables that contain information about system configuration,
user preferences, and other properties of the environment. Additionally, users can define their own environment
variables to customize the execution of programs and scripts.

# Portuguese
- Variaveis de Ambiente -

Cada sistema operacional mantém um conjunto de variáveis de ambiente que contém informações sobre a configuração do
sistema, preferências do usuário e outras propriedades do ambiente. Além disso, os usuários podem definir suas
próprias variáveis de ambiente para personalizar a execução de programas e scripts.


"""
import os

print(os.getenv("test"))
