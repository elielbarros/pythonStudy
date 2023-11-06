magical_word = 'hello'
magical_star = len(magical_word) * '*'
magical_word_length = len(magical_word)
discovered_word = len(magical_word) * '*'

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
        magical_star = ''
        while index < magical_word_length:
            if discovered_word[index] != '*':
                magical_star += discovered_word[index]
                index += 1
                continue

            if character.lower() == magical_word[index]:
                magical_star += character.lower()
                index += 1
                continue

            if discovered_word[index] == '*':
                magical_star += '*'

            index += 1

        discovered_word = magical_star
    print(discovered_word)

    if discovered_word == magical_word:
        print("You've discovered the word! Congratulations.")
        break

