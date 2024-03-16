#!/usr/bin/python3

def uppercase(input_str):
    result = ""
    for c in input_str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    return result
