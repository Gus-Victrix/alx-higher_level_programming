#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''
    Returns the exlusive or of the two input sets

    >>> only_diff_elements({1,2,3,4},{3,4,5,6})
    >>> {1,2,5,6}
    '''
    return set_1 ^ set_2
