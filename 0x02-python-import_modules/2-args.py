#!/usr/bin/python3
from sys import argv
def print_arguments():
    argument = len(argv) - 1
    if argument == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argument, "s" if argument > 1 else ""))
        for i, arg in enumerate(argv[1 :], start = 1):
            print("{}: {}".format(i, arg))
if __name__ == "__main__":
    print_arguments()
