"""
PEP 570 - Python Positional-Only Parameters
https://peps.python.org/pep-0570/

Will define that the method will accept ONLY POSITIONAL PARAMETERS

How does that?

Using '/' as parameter

Look example below
"""


def sum_(a, b, /):
    print(a + b)

# it is possible to send positional parameters ONLY
sum_(1, 2)  # output: 3

# But if we try to pass named argument, it will raise exception:
# sum_(a=1, b=2)  # output: TypeError: sum_() got some positional-only arguments passed as keyword arguments: 'a, b'
