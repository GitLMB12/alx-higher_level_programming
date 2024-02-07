#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg = argv[1:]
    total = 0
    for ar in arg:
        total += int(ar)
    print("{}".format(total))
