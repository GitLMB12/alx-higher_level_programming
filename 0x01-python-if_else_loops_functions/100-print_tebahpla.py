#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print(chr(c - 32 * ((c - ord('a')) % 2)), end="")
