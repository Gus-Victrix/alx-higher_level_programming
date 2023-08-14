#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    j = 0
    while (j < len(my_string):
            tmp = ord(my_string[j:j + 1])
            if tmp != ord("c") and tmp != ord("C"):
                new_string += my_string[j:j + 1]
            j++
    return new_string
