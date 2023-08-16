#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''
    Replaces or adds key/value in a dictionary.

    >>> a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    >>> new_dict = update_dictionary(a_dictionary, 'language', "Python")
    >>> print_sorted_dictionary(new_dict)
    language: Python
    number: 89
    track: Low level
    >>> new_dict = update_dictionary(new_dict, 'city', "San Francisco")
    >>> print_sorted_dictionary(new_dict)
    city: San Francisco
    language: Python
    number: 89
    track: Low level
    '''
    a_dictionary[key] = value
    return a_dictionary
