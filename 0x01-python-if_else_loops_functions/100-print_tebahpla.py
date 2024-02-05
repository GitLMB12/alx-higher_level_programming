#!/usr/bin/python3
print("{}".format("".join([chr(c) for c in range(ord('z'), ord('A') - 1, -1) if c % 2 == 0])))
