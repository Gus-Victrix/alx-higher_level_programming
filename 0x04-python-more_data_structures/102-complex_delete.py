#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''
    Deletes keys with the input value of the input dictionary.
    '''
    if not a_dictionary:
        return a_dictionary
    a_dictionary = {k: v for k, v in a_dictionary.items() if v != value}
    return a_dictionary
