#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Computes the square value of all integers of a matrix

    >>> square_matrix_simple([[1,2,3],[4,5,6],[7,8,9]])
    >>> [[1,4,9],[16,25,36],[49,64,81]]
    '''
    return list(map(lambda row: list(map(lambda num: num ** 2, row)), matrix))
