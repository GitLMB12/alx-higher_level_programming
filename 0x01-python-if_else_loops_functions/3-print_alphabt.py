#!/usr/bin/python3
x = 97
ch_string = ""
while x <= 122:
    if chr(x) != 'e' and chr(x) != 'q':
        output_string += chr(x)
        x += 1
print("{}".format(output_string), end="")
