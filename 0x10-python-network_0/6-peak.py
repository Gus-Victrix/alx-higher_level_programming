#!/usr/bin/python3

"""
Interview questions peak
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of numbers
    args:
        list_of_intergers (list): List of int
    Return: None of not peak, the peak else
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    return find_peak_rec(list_of_integers, 0, len(list_of_integers))


def find_peak_rec(nums, start, end):
    """
    Find a peak in a list of numbers via recurtions
    args:
        num (list): List of int
        start (int): The idx start
        end (int): The idx end
    Return: None of not peak, the peak else
    """
    if start > end:
        return None

    middle = (start + end) // 2
    if middle == 0 and nums[middle + 1] <= nums[middle]:
        return nums[middle]
    if middle == len(nums) - 1 and nums[middle - 1] <= nums[middle]:
        return nums[middle]
    if nums[middle - 1] < nums[middle] and nums[middle + 1] < nums[middle]:
        return nums[middle]

    if nums[middle - 1] > nums[middle]:
        return find_peak_rec(nums, start, middle - 1)
    else:
        return find_peak_rec(nums, middle + 1, end)
