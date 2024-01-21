from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-b', '--basic',
                    help='Show hello world on screen',
                    # type=str,
                    metavar='STRING',
                    # default='Hello World!', # The Default value will be Hello World!
                    required=False,  # Argument is not required
                    # /home/eliel/Documents/projects/pythonStudy/venv/bin/python /home/eliel/Documents/projects/pythonStudy/section6_python_modules/307_argparse_argumentparser.py -b 1 2 3 4
                    # nargs='+' # Will concatenate all script parameters passed for the argument basic
                    # /home/eliel/Documents/projects/pythonStudy/venv/bin/python /home/eliel/Documents/projects/pythonStudy/section6_python_modules/307_2_argparse_argumentparser.py -b hello -b world
                    action='append',  # Will receive the argument more than once but the type must change from str for list
                    )

# /home/eliel/Documents/projects/pythonStudy/venv/bin/python /home/eliel/Documents/projects/pythonStudy/section6_python_modules/307_argparse_argumentparser.py --help
# -b STRING [STRING ...], --basic STRING [STRING ...]
# Show hello world on screen

parser.add_argument('-v',
                    '--verbose',
                    help='Show log',
                    action='store_true'
                    )

args = parser.parse_args()

if args.basic is None:
    print('You must provide b argument value')
else:
    print(args.basic)

# If you do not know how use the script it is possible to use --help before execute script
# venv/bin/python /home/eliel/Documents/projects/pythonStudy/section6_python_modules/307_argparse_argumentparser.py --help


# /home/eliel/Documents/projects/pythonStudy/venv/bin/python /home/eliel/Documents/projects/pythonStudy/section6_python_modules/307_3_argparse_argumentparser.py -b Hello -b World
print(args.verbose)  # output: False

# /home/eliel/Documents/projects/pythonStudy/venv/bin/python /home/eliel/Documents/projects/pythonStudy/section6_python_modules/307_3_argparse_argumentparser.py -b Hello -b World -v
print(args.verbose)  # output: True
