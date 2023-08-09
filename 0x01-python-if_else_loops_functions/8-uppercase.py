#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            offset = 32
            printed = chr(ord(char) - offset)
        else:
            printed = char
        print("{}".format(printed), end="")
    print("{}".format(""))
