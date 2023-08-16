#!/usr/bin/python3
def weight_average(my_list=[]):
    '''
    Returns the weighted average of all integers tuple (<score>, <weight>)
    '''
    if not my_list:
        return 0
    total_score = 0
    total_weight = 0
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight
    if total_weight == 0:
        return 0
    return total_score / total_weight
