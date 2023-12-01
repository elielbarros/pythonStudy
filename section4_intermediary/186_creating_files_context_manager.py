"""
# English
It is possible to manipulate file with Python

To manipulate a file it is necessary the directory path and the file name

If the directory path informed, is tha file name, so the file will be created on the same directory that is executed
the python script

If the directory path has the directory path specified and the file name, so the file will be created at this
specified directory path

To manipulate files, we need to know about some modes:
- r (leitura)           || w (escrita) || x (criacao)
- a (escreve ao final)  || b (binario)
- t (modo texto)        || + (leitura e escrita)
- Context Manager - with (abre e fecha arquivo)

# Portuguese

Eh possivel manipular arquivo com o Python

Para manipular um arquivo eh necessario o caminho do arquivo e o nome do arquivo

Se for informado no caminho, apenas o nome do arquivo, entao o arquivo serah criado no mesmo diretorio de onde ocorre
a execucao do script python

Se for informado um caminho + o nome do arquivo, o arquivo sera criado no caminho especificado.

Para manipular arquivos, precisamos ter conhecimento dos modos:
- r (leitura)           || w (escrita) || x (criacao)
- a (escreve ao final)  || b (binario)
- t (modo texto)        || + (leitura e escrita)
- Context Manager - with (abre e fecha arquivo)
"""

file_path = '/home/eliel/Documents/projects/pythonStudy/section4_intermediary/186_class.txt'
print(file_path)

# Not indicated way to manipulate file
# file = open(file_path, 'w')
#
# file.close()

# Indicated way to manipulate file
# Using context manager - WITH
with open(file_path, 'w') as file:
    print('Hello World')
    print('Closing file')

