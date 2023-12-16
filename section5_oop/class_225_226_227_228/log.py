"""
# Portuguese
- Abstracao

- Assinatura de Metodo
    Se uma subclasse estah sobrepondo um metodo da classe super, eh necessario manter a sua assinatura identica.
    Isso indica que nao deve-se mudar o tipo e/ou retorno do metodo

- Template Method Pattern
    Essa aula implementa parte do pattern Template Method.
"""
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    # This is an abstraction.
    # When we use a method from superclass to use a protected method using Inheritance.
    def _log(self, message):
        raise NotImplementedError('Implement log method')

    def log_error(self, message):
        self._log(f'Error: {message}')

    def log_success(self, message):
        self._log(f'Success: {message}')


# Inheritance
# LogFileMixin is the class Log too
class LogFileMixin(Log):
    def _log(self, message):
        print(message)
        with open(LOG_FILE, 'a') as file:
            file.write(f'{message}')
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} {self.__class__.__name__}')


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.log_error('Raising Error')
    log_print.log_success('Raising Success')

    log_file = LogFileMixin()
    log_file.log_success('Raising Success')
