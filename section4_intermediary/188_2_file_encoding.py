"""
# English
Every file has an encoding type

For default the 'encoding' from Linux and Mac system are 'UTF-8', for windows is 'Windows 1252'

To set the 'encoding' we want, it is just add at the final of open() method the 'encoding' type.

Example: open(file_path, 'w', encoding='utf8'

# Portuguese
Todo arquivo tem um tipo de encoding

Por padrao o 'encoding' do linux e mac eh 'UTF-8', o Windows eh 'windows 1252'

Para definir o 'encoding' que queremos, eh necessario adicionar ao final do metodo open() o tipo do 'encoding'.

Example: open(file_path, 'w', encoding='utf8'
"""
file_path = '/home/eliel/Documents/projects/pythonStudy/section4_intermediary/186_class.txt'

with open(file_path, 'w', encoding='iso-8859-1') as file:
    file.write('çã!\n')
