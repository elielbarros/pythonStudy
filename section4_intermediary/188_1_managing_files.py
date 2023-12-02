file_path = '/home/eliel/Documents/projects/pythonStudy/section4_intermediary/186_class.txt'

# WRITING FILE || DOES NOT READ || CREATE FILE IF IT DOES NOT EXIST EITHER
# USING 'w' TO WRITE ON FILE, EVERYTIME YOU OPEN FILE USING 'w' EVERYTHING THAT WAS THERE ALREADY WILL BE REMOVED
with open(file_path, 'w') as file:
    # The class responsible for manage this file is _io.TextIOWrapper
    print(type(file))

    file.write('Hello World\n')
    file.write('How you doing?\n')

# READING FILE || IT IS ONLY POSSIBLE TO READ A FILE THAT EXISTS
with open(file_path, 'r') as file:
    print(file.read())

# WRITING AND READING FILE AT THE SAME TIME
with open(file_path, 'w+') as file:
    file.write('Hello World\n')
    file.write('How you doing?\n')

    file.seek(0, 0)
    print(file.read())

# TO WRITE WITHOUT REMOVE WHAT WAS INSIDE THE FILE, WE HAVE TO USE 'a'
# USING 'a' EVERYTHING WILL BE ADDED AT THE FINAL LINE FROM THE FILE
# 'a' MEANS - APPEND - MODE
with open(file_path, 'a+') as file:
    file.write('Write file at the final line\n')

    file.seek(0, 0)
    print(file.read())

# BINARY MODE IS TO SPECIFIC CASE AND WILL NOT WORK TO WRITE STRING AS WE ARE DOING
