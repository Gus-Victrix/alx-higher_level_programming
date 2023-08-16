#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    Replaces all occurences of an element with another in a new list.

    >>> search_replace([1, 2, 3, 4, 5], 2, 89)
    >>> [1, 89, 3, 4, 5]
    '''
    return [n if n != search else replace for n in my_list]

