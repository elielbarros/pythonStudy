"""
Strip

Strip will remove spaces from the beginning and end of the string.
"""
              # 0123456 = 7 numbers
string_strip = ' space '.strip()
print(string_strip, len(string_strip))

# We also have rstrip() that will only remove spaces from the end of the string
string_rstrip = ' space '.rstrip()
print(string_rstrip, len(string_rstrip))

# We also have lstrip() that will only remove spaces from the beginning of the string
string_lstrip = ' space '.lstrip()
print(string_lstrip, len(string_lstrip))
