#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            offset = 32
            character = chr(ord(char) - offset)
        else:
            character = char
        print("{}".format(character), end="")
    print("{}".format(""))
