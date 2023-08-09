#!/usr/bin/python3
def print-last-digit(number):
    if number < 0:
        number *= -1
    print(f"{number % 10:d}", end="")

    return (number % 10)
