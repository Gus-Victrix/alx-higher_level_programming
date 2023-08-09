#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            offset = 32
            uppercase_char = chr(ord(char) - offset)
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print()
