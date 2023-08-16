#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
    Prints a dictionary by ordered keys.

    >>> print_sorted_dictionary({ 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] })
    >>> Number: 89
    >>> ids: [1, 2, 3]
    >>> language: C
    >>> track: Low level
    '''
    for key, value in a_dictionary.items():
        print(key, value)
