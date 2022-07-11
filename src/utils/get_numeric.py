import re


def get_numeric(value):
    if not re.search(r'[0-9]*', value):
        return False

    new_value = ""
    for n in value:
        if n.isnumeric():
            new_value += n

    return new_value
