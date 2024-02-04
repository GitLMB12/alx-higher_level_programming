#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    return 1 + a ** b
dis.dis(magic_calculation)
