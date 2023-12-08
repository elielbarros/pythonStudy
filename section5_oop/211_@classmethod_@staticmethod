"""
# English

If we want to define properties using 'self' define method without annotation

If we want to define properties using 'cls' define method with @classmethod

If we want just the method, use @staticmethod

# Portuguese

Se quisermos definir propriedades usando o método 'self' define sem anotação

Se quisermos definir propriedades usando o método 'cls' defina com @classmethod

Se quisermos apenas o metodo, use @staticmethod
"""

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        con = cls()
        con.user = user
        con.password = password
        return con

    @staticmethod
    def log(message):
        print('Log:', message)


connection = Connection.create_with_auth('john', 'password')
print(connection.__dict__)  # output: {'host': 'localhost', 'user': 'john', 'password': 'password'}

Connection.log('Hello World')  # output: Log: Hello World
