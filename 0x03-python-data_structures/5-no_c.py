#!/usr/bin/python3
def no_c(my_string):
    for letters in my_string:
        if letters == 'c' or letters == 'C':
            del letters
    return my_string
