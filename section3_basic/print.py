"""
Print is used to show something on screen.
Print receive an argument.
* These argument are named "Not Named Argument"
* sep is an argument that will be between 12 and 34, like 12-34

About breakline
\r\n CRLF
\n LF
"""
print(12, 34, sep="-")
print(26, 9, 1995, sep=" ", end="\n\r")  # default
print(26, 9, 1995, sep="/", end="#")  # not default
print("Hello World!")
