"""
JOIN STRING

It is possible to join a string list with a specific character

Also, it is possible to join a string with a specific character too
"""
phrase = ("It has survived not only five centuries, but also the leap into electronic typesetting, remaining "
          "essentially unchanged.")

split_phrase = phrase.split()
print(split_phrase)

joined_phrase = '-'.join(split_phrase)
print(joined_phrase)

joined_string = '-'.join('abc')
print(joined_string)
