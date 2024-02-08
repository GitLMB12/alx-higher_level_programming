#!/usr/bin/python3
def no_c(my_string):
    """Remove all occurrences of 'c' and 'C' from a string."""
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result
