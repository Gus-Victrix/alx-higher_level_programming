#!/usr/bin/python3

"""
Create a pascal triangle of size n
"""


def pascal_triangle(n):
    """
    Create a pascal triangle of size n
    Args:
        n (int): The size
    """
    returnList = []
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(returnList[i - 1][j - 1] + returnList[i - 1][j])
        returnList.append(line)
    return returnList
