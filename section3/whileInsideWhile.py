qtt_lines = 5
qtt_columns = 5

line = 1
column = 1
while line < qtt_lines:
    print(f'[{line}]', end=' ')
    while column < qtt_columns:
        print(f'{column}', end=' ')
        column += 1
    qtt_columns = column + 5
    print()
    line += 1
