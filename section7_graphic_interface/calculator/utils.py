import re

NUMBER_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(value: str):
    return bool(NUMBER_OR_DOT_REGEX.search(value))


def isEmpty(value: str):
    return len(value) == 0


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        print('Failed to check number')

    return valid
