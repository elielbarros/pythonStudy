phrase = ("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
Ipsum.""").lower()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
max_number = 0
char_repeated_most = 'a'
qtt_char_repeated_most = 0
index = 0
while index < len(alphabet):
    char = alphabet[index]

    if phrase.count(char) > phrase.count(char_repeated_most):
        char_repeated_most = char
        qtt_char_repeated_most = phrase.count(char)

    index += 1

print(char_repeated_most, ':', qtt_char_repeated_most)

"""
Today i learned about '.count' method.
With '.count' method it is possible to count how many times a letter was repeated on a phrase.
"""