"""
# Portuguese
- Abstracao

- Assinatura de Metodo
    Se uma subclasse estah sobrepondo um metodo da classe super, eh necessario manter a sua assinatura identica.
    Isso indica que nao deve-se mudar o tipo e/ou retorno do metodo
"""


class Log:
    def log(self, message):
        raise NotImplementedError('Implement log method')


class LogFileMixin(Log):
    def log(self, message):
        print(message)


if __name__ == '__main__':
    log_ = LogFileMixin()
    log_.log('Hello World')
