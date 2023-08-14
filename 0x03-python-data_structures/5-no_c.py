#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    for letters in new_string:
        if ord(letters) == ord("c") or ord(letters) == ord('C'):
            del letters
    return new_string
