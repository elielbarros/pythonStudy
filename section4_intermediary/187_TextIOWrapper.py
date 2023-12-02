file_path = '/home/eliel/Documents/projects/pythonStudy/section4_intermediary/186_class.txt'

# WRITING FILE
with open(file_path, 'w') as file:
    # To write something on the File we have tu use the method write and inside, put what we want to write
    # To jump from one line to another we have to use \r\n for CRLF files or \n for LF files
    # My system work with LF so we will use \n
    file.write('Hello World\n')
    file.write('How you doing?\n')

    # We could also write lines using the method writelines() passing to this method something iterable, like a list
    # or a tuple
    file.writelines(['John Doe\n', 'Joana Dark\n'])

    # It is not possible to read file on this case ('w'), so it will raise an exception: io.UnsupportedOperation: not
    # readable
    # file.read()

# READING FILE
with open(file_path, 'r') as file:
    # It is not possible to write file on this case ('r'), so it will raise an exception: io.UnsupportedOperation:
    # not writable
    # file.write('Hello World\n')

    # read() will return everything that is available inside the file
    print(file.read())

    file.seek(0, 0)
    # We could also read line by line from file
    print(file.readline())

    file.seek(0, 0)
    # We could use readlines() that will return iterable from each line available
    for line in file.readlines():
        print(line.strip())

    print()

# READING AND WRITING FILE AT THE SAME TIME
with open(file_path, 'w+') as file:
    file.write('Hello World\n')
    file.write('How you doing?')
    # To read file after write it, we have to move the cursor to first line and first column.
    # To do that we use seek, with position 0, 0 then the method read() will work fine.
    file.seek(0, 0)
    print(file.read())




