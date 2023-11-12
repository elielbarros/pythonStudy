# input always return string
name = input("What's your name? ")
print(f'Your name: {name}')

# If we want to get numbers from user, we have to convert the result input into an int
number_A_str = input("Choose a number for A: ")
number_B_str = input("Choose a number for B: ")

print(f'A + B = {int(number_A_str) + int(number_B_str)}')
