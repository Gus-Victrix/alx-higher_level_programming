#!/usr/bin/python3
def weight_average(my_list=[]):
    '''
    Returns the weighted average of all integers tuple (<score>, <weight>)
    '''
    a = 0
    for score, weight in my_list:
        a += score * weight
    return a
