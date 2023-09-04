#!/usr/bin/python3

"""
Task 1 for the 0x07 Python test driven development
Divide a given matrix by a given number
Test are avalaible in /tests/:
    python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by 3, and create a new one to stock the result
    Args:
        matrix (list of list of int): Given matrix
        div (int or float): Denominator
    Raises:
        TypeError: If div is not a num
        TypeError: If row of matrix is not the same size
        TypeError: If matrix is not a list of list of int or float
        ZeroDivisionError: If div is 0
    Returns: The new matrix
    """

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    sizeRow = len(matrix[0])
    for row in range(len(matrix)):
        if len(matrix[row]) != sizeRow:
            raise TypeError('Each row of the matrix must have the same size')
        if type(matrix[row]) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
        for elem in range(len(matrix[row])):
            if type(matrix[row][elem]) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')

    return [[float("{:.2f}".format(x / div)) for x in row] for row in matrix]
