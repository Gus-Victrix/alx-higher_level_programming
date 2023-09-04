#!/usr/bin/python3

"""
Multiply two matrix
"""


def matrix_mul(m_a, m_b):
    """
    Multiply 2 Matrix.
    Args:
        m_a (list of list): Matrix one.
        m_b (list of list): Matrix two.
    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of list
        TypeError: If m_a or m_b doesn't have each row of same size
        TypeError: If m_a or m_b not countain only int or float
        ValueError: If m_a or m_a is empty
        ValueError: If m_a and m_b can't be mul
    Returns: Return a new matrix, product of the two given in args.
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    size_a = len(m_a[0])
    for row in m_a:
        if size_a == 0:
            raise ValueError("m_a can't be empty")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')
        if size_a != len(row):
            raise TypeError("each row of m_a must be of the same size")

    size_b = len(m_b[0])
    for row in m_b:
        if size_b == 0:
            raise ValueError("m_b can't be empty")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')
        if size_b != len(row):
            raise TypeError("each row of m_b must be of the same size")

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    newMatrix = []
    for i in range(len(m_a)):
        newRow = []
        for j in range(size_b):
            num = 0
            for k in range(size_a):
                num += m_a[i][k] * m_b[k][j]
            newRow.append(num)
        newMatrix.append(newRow)
    return newMatrix
