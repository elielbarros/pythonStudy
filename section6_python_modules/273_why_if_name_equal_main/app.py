"""
# English
The expression if __name__ == '__main__': in Python is used to determine whether the Python script is running as a
standalone program or whether it is being imported as a module in another script. This is a common practice in Python
to allow a script to have different behaviors depending on how it is executed.

__name__ is a special variable in Python that is automatically defined by the interpreter. When a Python script is
executed, Python sets the __name__ variable to the value '__main__' if the script is running as the main program.

If the script is being imported as a module in another script, __name__ will be set to the actual name of the module,
not '__main__'.

The if __name__ == '__main__': structure is commonly used to include a block of code that should be executed only
when the script is executed directly and not when it is imported as a module.

# Portuguese
A expressão if __name__ == '__main__': em Python é usada para determinar se o script Python está sendo executado como
um programa independente ou se está sendo importado como um módulo em outro script.

__name__ é uma variável especial em Python que é automaticamente definida pelo interpretador. Quando um script Python
é executado, o Python define a variável __name__ com o valor '__main__' se o script está sendo executado como o
programa principal.

Se o script estiver sendo importado como um módulo em outro script, __name__ será definido como o nome real do
módulo, não como '__main__'.

A estrutura if __name__ == '__main__': é comumente usada para incluir um bloco de código que deve ser executado
apenas quando o script é executado diretamente e não quando é importado como um módulo.
"""

from module import sum_

if __name__ == '__main__':
    print(f'{__name__=}')  # output: __name__='__main__'
    print(sum_(10, 30))  # output: 40
