"""
# English
The subprocess module in Python provides a way to call external processes from Python programs. It replaces older
modules like os.system() and os.spawn*().
The subprocess module provides a more powerful and flexible interface for interacting with external processes,
enabling output capture, input/output redirection, communication with background processes, and more.

Executing Simple Commands:
You can use the subprocess.run() function to run external commands synchronously.

- stdin, stdout, stderr -> Input, Output, Error
- capture_output -> capture output and error for later use
- text -> If true, inputs and outputs will be treated as text and automatically encoded or decoded with the
platform's default character set (usually UTF-8)
- shell -> If true, you will have access to the system shell. When using shell (True), it is recommended to send
command and arguments together.
- executable -> can be used to specify the path of the executable that will start the subprocess.

Return:
stdout, stderr, return code and args

Important: Windows encoding may be different. Try using cp1252, cp852, cp850 or others. For mac and linux, use utf_8

Example command:
Windows -> ping 127.0.0.1
Linux/Mac -> ping 127.0.0.1 -c 4

# Portuguese
O módulo subprocess em Python fornece uma maneira de chamar processos externos a partir de programas Python. Ele
substitui módulos mais antigos como os.system() e os.spawn*().
O módulo subprocess oferece uma interface mais poderosa e flexível para interagir com processos externos, permitindo
a captura da saída, o redirecionamento de entrada/saída, comunicação com processos em segundo plano e muito mais.

Executando Comandos Simples:
Você pode usar a função subprocess.run() para executar comandos externos de maneira síncrona.

- stdin, stdout, stderr -> Entrada, Saida, Erro
- capture_output -> captura saida e erro para uso posterior
- text -> Se verdadeiro (True), entradas e saidas serao tratadas como texto e automaticamente codificadas ouo
decodificadas com o conjunto de caracteres padrao da plataforma (geralmente UTF-8)
- shell -> Se verdadeiro (True), tera acesso ao shell do sistema. Ao usar shell (True), recomendado enviar comando e
argumentos juntos.
- executable -> pode ser usado para especificar o c aminho do executável que iniciara o subprocesso.

Retorno:
stdout, stderr, returncoode e args

Importante: A codificacao do windows pode ser diferente. Tente usar cp1252, cp852, cp850 ou outros. Para mac e linux,
use utf_8

Comando de exemplo:
Windows -> ping 127.0.0.1
Linux/Mac -> ping 127.0.0.1 -c 4
"""
