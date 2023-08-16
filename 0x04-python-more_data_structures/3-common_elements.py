#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''
    Returns the set containing common elements in two sets

    >>> common_elements({1,2,3,4},{3,4,5,6})
    >>> {3,4}
    '''
    return set_1 & set_2
