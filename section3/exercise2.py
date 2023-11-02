"""
1. Get your name from input
2. Print the name
3. Print the name reversed
4. Print if name contain (or not) space
5. Print how many characters has the name
6. Print the first character from the name
7. Print the last character from the name
8. If input is empty print 'Sorry! You must input a name'
"""

space = ' '
name = input('Write your name: ')
if not len(name):
    print('Sorry! You must provide a name.')
else:
    print(f'Your name is: {name}')
    name_reversed = name[::-1]
    print(f'Your name reversed is: {name_reversed}')
    if space in name:
        print(f'Your name contain space')
    else:
        print(f'Your name does not contain space')
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is: {name[0]}')
    print(f'The last letter of your name is: {name[len(name)-1]}')

