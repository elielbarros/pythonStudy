magical_word = "hello"
correct_words = ''
attempts = 0

print(f'Tip: Magical Word has {len(magical_word)} letters.')

while True:
    attempts += 1
    letter = input('Digit a letter to complete Magical Word: ').lower()

    if len(letter) > 1:
        print('You must provide just one letter')
        continue

    if letter in magical_word and letter not in correct_words:
        correct_words += letter

    formed_word = ''
    for magical_letter in magical_word:
        if magical_letter in correct_words:
            formed_word += magical_letter
        else:
            formed_word += '*'

    print(formed_word)

    if formed_word == magical_word:
        print(f"Congratulations! You've finished the Magical Word: {formed_word}")
        print(f"You've tried {attempts} times to discover the Magical Word.")
        correct_words = ''
        attempts = 0
