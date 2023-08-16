#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    '''
    Returns the Hadamard square of a matrix
    '''
    return list(map(lambda row: list(map(lambda a: a**2 , row)), matrix))
