"""
Link: https://www.youtube.com/watch?v=T17BTNKBeJY&ab_channel=Ot%C3%A1vioMiranda
"""

from pathlib import Path

# Path() return actual directory that this file is inside
project_path = Path()

print(project_path)  # output: .

print(project_path.absolute())  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules


# Return this file path
this_file_path = Path(__file__)

print(this_file_path.absolute())  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules/291_manipulating_directories_files.py

# Return file Parent path
print(this_file_path.parent)  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules

# Return Parent path from another Parent path
print(this_file_path.parent.parent)  # output: /home/eliel/Documents/projects/pythonStudy

# How concatenate directory to a path using __truediv__ from Python
idea = this_file_path.parent / 'idea'
print(idea)  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules/idea
print(idea / 'file_idea.txt')  # output: /home/eliel/Documents/projects/pythonStudy/section6_python_modules/idea/file_idea.txt

# It is possible to get System Home Path using Path.home()
print(Path.home())  # output: /home/eliel

# It is possible to create a text file using touch
text_file = Path.home() / 'Desktop' / 'text_file.txt'
text_file.touch()
print(text_file)  # output : /home/eliel/Desktop/text_file.txt

# It is possible to write something inside a file created before
# write_text will always delete what was inside the file before and write new changes
text_file.write_text('Hello World')

# It is also possible to delete this file using unlink()
text_file.unlink()

another_text_file_path = Path.home() / 'Desktop' / 'another_text_file.txt'

another_text_file_path.touch()
another_text_file_path.write_text('')

# Writing more than one line inside file
with another_text_file_path.open('a+') as file:
    file.write('One line\n')
    file.write('Another line\n')
    file.write('Last line\n')

print(another_text_file_path.read_text())
# output:
# One line
# Another line
# Last line

another_text_file_path.unlink()

# mkdir
# Creating directory using mkdir Path.mkdir()
# exist_ok=True indicate that if the directory is already there, it is okay.
mkdir_path = Path.home() / 'Desktop' / 'mkdir_directory'
mkdir_path.mkdir(exist_ok=True)

sub_directory_mkdir = mkdir_path / 'sub_directory'
sub_directory_mkdir.mkdir(exist_ok=True)

text_file_sub_directory = sub_directory_mkdir / 'file_.txt'
text_file_sub_directory.touch()
text_file_sub_directory.write_text('Hello World from subdirectory')

text_file_mkdir_directory = mkdir_path / 'file_mkdir.txt'
text_file_mkdir_directory.touch()
text_file_mkdir_directory.write_text('Hello world from mkdir directory')




