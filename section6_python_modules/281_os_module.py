"""
# English
The `os` module in Python provides an interface for interacting with the underlying operating system. It offers
various functions to perform system-related operations, such as file manipulation, filesystem navigation,
system command execution, and more. Some of the main functions of the `os` module include:

1. Directory and File Manipulation:
   - `os.getcwd()`: Returns the current working directory.
   - `os.chdir(path)`: Changes the working directory to the specified path.
   - `os.listdir(path='.')`: Returns a list of file names in the specified directory.

2. Creation and Removal of Directories:
   - `os.mkdir(path)`: Creates a directory with the specified path.
   - `os.makedirs(path)`: Creates nested directories as specified in the path.
   - `os.rmdir(path)`: Removes the specified directory.
   - `os.removedirs(path)`: Removes nested directories as specified in the path.

3. File Path Manipulation:
   - `os.path.join(path1, path2, ...)`: Concatenates paths appropriately for the operating system.
   - `os.path.abspath(path)`: Returns the absolute path of the file or directory.
   - `os.path.exists(path)`: Checks if the specified path exists.
   - `os.path.isfile(path)`: Checks if the specified path is a file.
   - `os.path.isdir(path)`: Checks if the specified path is a directory.

4. Execution of System Commands:
   - `os.system(command)`: Executes a command in the operating system shell.
   - `os.popen(command)`: Opens a pipe for the execution of a command.
   - `os.spawn*(...)`: Functions for starting a new process.

5. Environment Variables:
   - `os.environ`: Dictionary representing the system's environment variables.
   - `os.getenv(key, default=None)`: Gets the value of an environment variable.

6. Process Handling:
   - `os.fork()`: Creates a new process (on Unix systems).
   - `os.kill(pid, signal)`: Sends a signal to a process (on Unix systems).
   - `os.wait()`, `os.waitpid(pid, options)`: Waits for the termination of a process.

Official documentation: https://docs.python.org/3/library/os.html

# Portuguese
O módulo os em Python fornece uma interface para interagir com o sistema operacional subjacente. Ele oferece várias
funções que permitem realizar operações relacionadas ao sistema, como manipulação de arquivos, navegação no sistema
de arquivos, execução de comandos do sistema, entre outras. Algumas das principais funções do módulo os incluem:

1. Manipulação de Diretórios e Arquivos:
 - os.getcwd(): Retorna o diretório de trabalho atual.
 - os.chdir(path): Muda o diretório de trabalho para o especificado em path.
 - os.listdir(path='.'): Retorna uma lista de nomes de arquivos no diretório especificado.

2. Criação e Remoção de Diretórios:
 - os.mkdir(path): Cria um diretório com o caminho especificado.
 - os.makedirs(path): Cria diretórios aninhados conforme especificado no caminho.
 - os.rmdir(path): Remove o diretório especificado.
 - os.removedirs(path): Remove diretórios aninhados conforme especificado no caminho.

3. Manipulação de Caminhos de Arquivo:
 - os.path.join(path1, path2, ...): Concatena caminhos de maneira apropriada para o sistema operacional.
 - os.path.abspath(path): Retorna o caminho absoluto do arquivo ou diretório.
 - os.path.exists(path): Verifica se o caminho especificado existe.
 - os.path.isfile(path): Verifica se o caminho especificado é um arquivo.
 - os.path.isdir(path): Verifica se o caminho especificado é um diretório.

4. Execução de Comandos do Sistema:
 - os.system(command): Executa um comando no shell do sistema operacional.
 - os.popen(command): Abre um pipe para a execução de um comando.
 - os.spawn*(...): Funções para iniciar um novo processo.

5. Variáveis de Ambiente:
 - os.environ: Dicionário que representa as variáveis de ambiente do sistema.
 - os.getenv(key, default=None): Obtém o valor de uma variável de ambiente.

6. Manipulação de Processos:
 - os.fork(): Cria um novo processo (em sistemas Unix).
 - os.kill(pid, signal): Envia um sinal para um processo (em sistemas Unix).
 - os.wait(), os.waitpid(pid, options): Espera pelo término de um processo.

Documentação oficial: https://docs.python.org/3/library/os.html
"""

import os

print(os.getcwd())  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules

# os.system('clear')

os.system('echo "Hello World"')  # output: Hello World
