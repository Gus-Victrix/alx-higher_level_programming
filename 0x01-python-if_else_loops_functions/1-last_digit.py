#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
b = "greater than 5" if a > 5 else ("is 0" if a == 0 else\
        "is less than 6 and not 0")
print(f"Last digit of {number:d} is {a:d} and is {b:s}")
