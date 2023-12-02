"""
# English
Mutable param problem on Python function

We have to check every time we define a new method if the param is a mutable param

If the param is a mutable param, we have to initialize before or as None and give it a new value as seen with list param

# Portuguese
Problema dos parametros mutaveis em funcoes Python

Nos temos que checar, todas as vezes que formos criar um novo metodo, se o parametro eh mutavel

Se o parametro eh mutavel, nos temos que inicializar esse parametro antes ou como None e dar um novo valor para ele
como visto na lita
"""


def add_client(name, client_list=[]):
    client_list.append(name)
    return client_list


# First of all, we will create our first client and add a new one and print the result
first_list_client = add_client('John')
add_client('Joana', first_list_client)
print(first_list_client)  # output: ['John', 'Joana']

# After create our first client and add another one (Joana) to this list
# I want to create another list client: second_list_client
# But in Python, this second_list will not be created. Python will use the first list again, append the new clients
# to it.
# See for yourself
second_list_client = add_client('Lucille')
add_client('Edie', second_list_client)
print(second_list_client)  # output: ['John', 'Joana', 'Lucille', 'Edie']


# To resolve this problem, we cant create the list inside method definition
# Look how we cand do it
def add_client_without_problem(name, client_list=None):
    if client_list is None:
        client_list = []

    client_list.append(name)
    return client_list


# Now we can create our different client list
client_list_without_problem_1 = add_client_without_problem('John')
add_client_without_problem('Joana', client_list_without_problem_1)
print(client_list_without_problem_1)  # output: ['John', 'Joana']

client_list_without_problem_2 = add_client_without_problem('Lucille')
add_client_without_problem('Edie', client_list_without_problem_2)
print(client_list_without_problem_2)  # output: ['Lucille', 'Edie']
