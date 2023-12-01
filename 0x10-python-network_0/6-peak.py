#!/usr/bin/env python3
'''
This module defines a function to find a peak in a list of unsorted ints.
'''


def find_peak(list_of_integers):
    '''
    Finds peak in a list of ints using a linear search.

    Args:
        list_of_integers (list): The list of integers to be searched.

    Raises:
        TypeError: if input is not a list or a list of integers.

    Returns: First peak found.
    '''
    if list_of_integers is None:
        return None
    if not isinstance(list_of_integers, list):
        raise TypeError('Input must be a list of integers')
    for i in range(len(nums)):
        if (i == 0 or nums[i] >= nums[i - 1]) and (
                i == len(nums) - 1 or nums[i] >= nums[i + 1]):
            return nums[i]

    return None
