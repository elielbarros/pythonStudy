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

# It is also possible to delete this file using unlink()
text_file.unlink()
