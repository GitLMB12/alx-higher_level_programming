#!/usr/bin/python3

from sys import argv

def infinite_add(arguments):
    T_Sum = 0
    for arg in arguments:
        T_Sum += int(arg)
    print(T_Sum)

if __name__ == "__main__":
    arguments = argv[1:]
    infinite_add(arguments)
