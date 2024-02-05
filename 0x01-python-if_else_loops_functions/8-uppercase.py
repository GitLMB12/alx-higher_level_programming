#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
            print('{}'.format(uppercase_char), end='')
uppercase("best")
uppercase("Best School 98 Battery street")
