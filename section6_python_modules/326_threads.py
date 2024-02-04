"""
# English
 - Threads -
How use Thread with method?
    Send method as argument and the method args that will be used on Thread constructor
    Example: Thread(target=method_name_here, args=('argument', 'here')

How join Thread created with principal Thread?
    Using Thread.join()

How check Thread is alive yet
    Using Thread.is_alive()

How to 'LOCK' a method to avoid 'DEADLOCK'?
     Using Lock() and in the method that needs to prevent deadlock use lock.acquire()

# Portuguese
 - Threads -
Como usar Thread com metodo?
    Envie o metodo como argumento e os argumentos do metodo que serao usados no construtor de Thread
    Exemplo: Thread(target=method_name_here, args=('argument', 'here')

Como juntar a Thread criada com a Thread principal?
    Usando Thread.join()

Como checar se a Thread esta viva ainda
    Usando Thread.is_alive()

Como fazer o 'LOCK' de um metodo para evitar 'DEADLOCK'?
    Usando Lock() e no metodo que precisar previnir deadlock usar lock.acquire()
"""
from threading import Lock
from threading import Thread
from time import sleep


class Ticket:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def buy(self, quantity):
        self.lock.acquire()
        if self.stock < quantity:
            print('Does not have enough ticket.')
            self.lock.release()
            return

        sleep(1)

        print(f'You bought {quantity} tickets. We have {self.stock} yet.')
        self.stock -= quantity
        self.lock.release()


if __name__ == '__main__':
    tickets = Ticket(10)
    for i in range(1, 20):
        t = Thread(target=tickets.buy, args=(i,))
        t.start()

    print(tickets.stock)
