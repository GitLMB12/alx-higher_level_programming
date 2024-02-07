#/bin/usr/python3
from sys import argv
def infinite_add(arguments):
    total = 0
    for arg in arguments:
        total += int(arg)
    return total
if __name__ == "__main__":
    arguments = argv[1:]
    result = infinite_add(arguments)
    print(result )
