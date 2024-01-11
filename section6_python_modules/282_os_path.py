import os

path = os.path.join('/home', 'eliel', 'Documents', 'projects', 'pythonStudy', 'file.txt')
print(path)  # output: home/eliel/Documents/projects/pythonStudy/file.txt

directory, file = os.path.split(path)
print(directory, file)  # output: home/eliel/Documents/projects/pythonStudy file.txt

file_name, file_extension = os.path.splitext(file)
print(file_name, file_extension)  # output: file .txt

git_ignore_path = os.path.join('/home', 'eliel', 'Documents', 'projects', 'pythonStudy', '.gitignore')
print(os.path.exists(git_ignore_path))  # output: True

print(os.path.abspath('.'))  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules

print(os.path.basename(path))  # output: file.txt
print(os.path.basename(git_ignore_path))  # output: .gitignore


