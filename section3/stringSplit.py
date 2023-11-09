"""
SPLIT STRING

1. It is possible to divide (as default) by spaces a string with split

2. Also, it is possible to divide the string by a specific character with split
"""
phrase = ("It has survived not only five centuries, but also the leap into electronic typesetting, remaining "
          "essentially unchanged.")

split_phrase = phrase.split()
print(split_phrase)

split_phrase = phrase.split(',')
print(split_phrase)


