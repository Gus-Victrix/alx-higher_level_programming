#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10 if number >= 0 else ((-number % 10) * (-1))
b = "greater than 5" if a > 5 else ("0" if a == 0 else
        "less than 6 and not 0")
print(f"Last digit of {number:d} is {a:d} and is {b:s}")
