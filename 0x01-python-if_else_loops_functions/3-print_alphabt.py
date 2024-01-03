#!/usr/bin/python3
x = 97
output_string = ""
while x <= 122:
    if chr(x) not in ('e', 'q'):
        output_string += "{}".format(chr(x))
    x += 1
print("{}".format(output_string), end="")
