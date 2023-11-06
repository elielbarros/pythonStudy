magical_word = 'hello'
magical_star = len(magical_word) * '*'
magical_word_length = len(magical_word)
discovered_word = ''

print('')
print(f'The tip is that the Magical Word has {magical_word_length} letters. {magical_star}')
print('')

while True:
    character = input("Digit one character that you think is on the Magical Word: ")
    if len(character) > 1:
        print("You must provide only one character per time")
        continue

    if character.lower() in magical_word.lower():
        index = 0
        while index < magical_word_length:
            if character.lower() == magical_word[index]:
                discovered_word += character.lower()
                index += 1
                continue

            if len(discovered_word) < magical_word_length:
                discovered_word += '*'

            index += 1


    print(discovered_word)

