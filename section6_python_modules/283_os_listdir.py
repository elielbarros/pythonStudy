import os

# /home/eliel/Documents/projects/pythonStudy


path = os.path.join('/home', 'eliel', 'Documents', 'projects', 'pythonStudy')

for directory_ in os.listdir(path):
    complete_path = os.path.join(path, directory_)
    if not os.path.isdir(complete_path):
        continue
    for sub_directory in os.listdir(complete_path):
        print(sub_directory)
