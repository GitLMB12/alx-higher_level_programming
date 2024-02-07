#/bin/usr/python3
from sys import argv
def infinite_add(arguments):
    total = 0
    for arg in arguments:
        total += int(arg)
    print(total)
if __name__ == "__main__":
    arguments = argv[1:]
    infinite_add(arguments)
