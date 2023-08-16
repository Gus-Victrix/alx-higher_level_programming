#!/usr/bin/python3
def weight_average(my_list=[]):
    '''
    Returns the weighted average of all integers tuple (<score>, <weight>)
    '''
    if not my_list:
        return 0
    a = 0
    for score, weight in my_list:
        a += score * weight
    return a / len(my_list)
