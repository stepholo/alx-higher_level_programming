#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ A Function that computes the square value of all integers
    of a matrix

    Parameters:
        - matrix: a two dimensional array list

    Return:
        - The square of each element of matrix
    """
    matrix_copy = [[] * x for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_copy[i].append(matrix[i][j])

    matrix_square = list(map(lambda y: list(map(lambda x: x ** 2, y)),
                             matrix_copy))

    return matrix_square
