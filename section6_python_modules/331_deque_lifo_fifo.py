"""
# English
What is LIFO (Last In First Out)?
     - The last item to enter the queue will be the first to leave the queue.
     - Stack concept
     - To remove an item from the end of the stack: O(1) CONSTANT TIME
     - To remove items from the beginning of the stack: O(n) LINEAR TIME
     - Using a list is good
What is FIFO (First In First Out)?
     = The first item to enter the queue will be the first to leave the queue.
     - Queue concept
     - Using deck is good

# Portugues
O que e LIFO (Last In First Out)?
    - O ultimo item a entrar na fila sera o primeiro a sair da fila.
    - Conceito de pilha (stack)
    - Para retirar um item do final da pilha: O(1) TEMPO CONSTANTE
    - Para retirar itens do inicio da pilha: O(n) TEMPO LINEAR
    - Usar lista e bom
O que e FIFO (First In First Out)?
    = O primeiro item a entrar na fila sera o primeiro a sair da fila.
    - Conceito de fila (queue)
    - Usar deque e bom
"""
from collections import deque

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# LIFO with list is good
# Will append 10 at the end of the stack
list_.append(10)

# Will pop last item from the stack
removed_item = list_.pop()
print(removed_item)  # output: 10
print()

# FIFO with list is bad
# To append an item into list, it is necessary to move all items one index ahead
list_.insert(0, 10)

# To remove an item from list, it is necessary to move all items one index behind
remove_item = list_.pop(0)
print(remove_item)  # output: 10

# FIFO is good to use with deque
# It is good to use deque when the list will suffer many changes
# deque works as a list, but these necessary item movements will be more improved like O(1)
queue_fifo: deque[int] = deque()
queue_fifo.append(3)
queue_fifo.append(4)
queue_fifo.append(5)
queue_fifo.appendleft(2)
queue_fifo.appendleft(1)
queue_fifo.appendleft(0)
print(queue_fifo)  # output: deque([0, 1, 2, 3, 4, 5])
popped_item = queue_fifo.pop()
print(popped_item)  # output: 5
popped_item = queue_fifo.popleft()
print(popped_item)  # output: 0
print(queue_fifo)  # output: deque([1, 2, 3, 4])
