#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''
    Deletes keys with the input value of the input dictionary.
    '''
    while value in a_dictionary.values():
        for key, value_ in a_dictionary.items():
            if value_ == value:
                a_dictionary.pop(key)
                break
    return a_dictionary
