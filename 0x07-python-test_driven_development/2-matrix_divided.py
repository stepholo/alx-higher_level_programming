#!/usr/bin/python3
"""

This module is a function that divides a matrix with a number

"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Arg:
      matrix: list of list
      div: number to divide the elemnts of a list

    Return:
       a new list of list containing the resuslt of division
    """
    error = "matrix must be a matrix (list of list) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(error)
        elif len(item) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for i in item:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(error)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[] for item in matrix]

    j = 0

    for item in matrix:
        for i in item:
            result = round((i / div), 2)
            new_matrix[j].append(result)
        j += 1

    return new_matrix
