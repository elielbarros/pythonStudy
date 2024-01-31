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

# Portuguese
 - Threads -
Como usar Thread com metodo?
    Envie o metodo como argumento e os argumentos do metodo que serao usados no construtor de Thread
    Exemplo: Thread(target=method_name_here, args=('argument', 'here')

Como juntar a Thread criada com a Thread principal?
    Usando Thread.join()

Como checar se a Thread esta viva ainda
    Usando Thread.is_alive()
"""
from threading import Thread
from time import sleep


def will_take_while(text, time):
    sleep(time)
    print(text)


t = Thread(target=will_take_while, args=('Hello World', 5))
t.start()

# Join Main Thread with Created Thread
t.join()
print('Hello World after Thread execution')

# Check Thread is Alive
# while t.is_alive():
#     print('Waiting for thread.')
#     sleep(.5)
