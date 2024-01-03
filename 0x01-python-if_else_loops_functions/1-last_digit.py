#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digits = number % 10
if last_digits > 5:
    print("Last digit of", number, "is", last_digits, "and is greater than 5")
elif last_digits == 0:
    print("Last digit of", number, "is", last_digits, "and is 0")
else:
print("Last digit of", number, "is", last_digits, "and is less than 6 and not 0")
