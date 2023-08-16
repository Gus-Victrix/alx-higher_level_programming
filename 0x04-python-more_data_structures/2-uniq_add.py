#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    Sums up unique elements of a list

    >>> uniq_add([1,3,4,5])
    >>> 15
    '''
    return sum(set(my_list))
