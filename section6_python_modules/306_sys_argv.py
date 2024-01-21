import sys

args = sys.argv
args_size = len(args)

# The First argument is the own module.
# The Actual argument will be 306_sys.argv.py
if args_size <= 1:
    print('No args sent')
else:
    try:
        # Argument is the same of script parameter.
        # Script Parameter on intellij is separated by space.
        print(f'Args: {args[1]}')  # hello_world
        print(f'Args: {args[2]}')
    except IndexError:
        print('Lack of arguments')
