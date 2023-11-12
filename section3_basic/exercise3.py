name = 'John Doe'
name_len = len(name)
index = 0
new_name = ''
while index < name_len:
    new_name += f'{name[index]}*'
    index += 1

print(new_name)
