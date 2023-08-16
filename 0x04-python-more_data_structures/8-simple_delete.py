#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
    Deletes a key in a dictionary

    >>> a_dictionary = {'language':"C",'Number':89,'track':"Low",'ids':[1,2,3]}
    >>> simple_delete(a_dictionary, 'track')
    Number: 89
    ids: [1, 2, 3]
    language: C
    '''
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
