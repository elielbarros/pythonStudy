a = 'A'
b = 'B'
c = 1.1

# Using the order of arguments
format = 'a={} b={} c={:.2f}'.format(a, b, c)

# Using index independent of order
format_by_index = 'a={0} b={1} c={2:.2f} c={2:.1f}'.format(a, b, c)

# Named parameter
named_parameter = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)

print(format)
print(format_by_index)
print(named_parameter)
