"""
Generator Expression: A function that knows when stop

Generator is an iterator but an iterator is not a generator

Generator is used when you are working with UNCOUNTABLE data

Why use Generator and not an Iterable when working with UNCOUNTABLE data?
For example, if you are using a list, you will load in memory ALL data... but if you are using
generator, it will load by necessity

But the generator does not have a length or index like list
"""
import sys

list_ = [number for number in range(1000000)]
print(f'{sys.getsizeof(list_)=}', sep='\n\n')  # output: 8448728

generator_ = (number for number in range(1000000))
print(sys.getsizeof(generator_))  # output: 200
