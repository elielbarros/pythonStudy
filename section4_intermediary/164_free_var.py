"""
English:
About Free Var

Free Variable: In a closure, a variable that is referenced by the internal function, but not defined within it,
is called a free variable. This variable is "free" in the sense that it is not tied directly to the inner function
and is found in the scope of the outer function.

Portuguese:
Sobre Variavel Livre
Variável Livre (Free Variable): Em um closure, uma variável que é referenciada pela função interna, mas não definida
dentro dela, é chamada de variável livre. Essa variável é "livre" no sentido de que não está vinculada diretamente à
função interna e é encontrada no escopo da função externa.
"""


# English:
# On this example, our Free Var is X
# We can see it printing our Free Var using co_freevars
# Portuguese:
# Nesse exemplo, nossa Variavel Livre é X
# Nós podemos ver isto fazendo a impressão das variaveis livres usando co_freevars
def outer_function(x):
    def inner_function(y):
        print(
            locals())  # output: {'y': 5, 'inner_function': <function outer_function.<locals>.inner_function at
        # 0x7f3012686700>, 'x': 10}
        print(inner_function.__code__.co_freevars)  # output: ('inner_function', 'x')
        return x + y

    return inner_function


closure_instance = outer_function(10)
result = closure_instance(5)
print(result)  # output: 15


# English:
# We can see on the example below a specific case that will raise the error 'UnboundLocalError'
# The attempt to change Free Var is the cause that is not possible.
# See the example below.
# Portuguese:
# Podemos ver no exemplo a seguir um caso onde ocorre o erro 'UnboundLocalError'
# Esse erro ocorre devido a tentativa de alterar uma Variavel Livre, o que não é possível.
# Veja no exemplo abaixo.
# def concatenate(initial_string):
#     final_value = initial_string
#     def inner_function(value_to_concatenate):
#         # output: UnboundLocalError: cannot access local variable 'final_value' where it is not associated with a
#         value
#         final_value += value_to_concatenate
#         return final_value
#     return inner_function
#
# concatenate_ = concatenate('a')
# print(concatenate_('b'))
# print(concatenate_('c'))
# print(concatenate_('d'))

# English:
# To solve this problem related to 'UnboundLocalError' we can put Free Var as 'nonlocal'
# For example: 'nonlocal final_value'
# Portuguese:
# Para resolver esse problema, relativo ao erro 'UnboundLocalError', podemos dizer que a Variavel Livre é
# 'nonlocal'.
# Por exemplo: 'nonlocal final_value'

def concatenate(initial_string):
    final_value = initial_string

    def inner_function(value_to_concatenate):
        nonlocal final_value
        final_value += value_to_concatenate
        return final_value

    return inner_function


concatenate_ = concatenate('a')
print(concatenate_('b'))
print(concatenate_('c'))
print(concatenate_('d'))
