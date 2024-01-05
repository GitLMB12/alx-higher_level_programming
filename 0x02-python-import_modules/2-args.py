#!/usr/bin/python3
from sys import argv

def print_arguments():
    num_arguments = len(argv) -1
    if num_arguments == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_arguments, "s" if num_arguments > 1 else ""))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
if __name__ == "__main__":
    print_arguments()
