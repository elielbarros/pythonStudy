"""
# FUNCTION #
1. Not Named Argument or Positional Argument

2. Named argument

"""


def sum_(a, b):
    print(f'{a=} ; {b=} | a + b = {a + b}')


# This way that we call the function is called Positional Argument
# It means that the param 'a' will receive the value 1 and the param 'b' will receive the value 2.
sum_(1, 2)

# This way that we call the function is called Named Argument
# It means  that the param 'a=1' independent of the order we call 'a' or 'b'... the param 'a' will receive 1
sum_(b=2, a=1)

# Also it is important to understand that, if we pass a Named Argument we can't pass after this Named Argument
# one Not Named Argument. If we pass Positional Argument after Named Argument, python will raise an error
# Error: SyntaxError: positional argument follows keyword argument
# sum_(b=2, 1)


# But it is possible to send a Named Argument after a Positional Argument
sum_(1, b=2)
