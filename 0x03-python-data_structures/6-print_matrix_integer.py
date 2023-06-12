#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Parameter:
     - matrix - list of list

    Return:
     - The contents of matrix
    """
    for row in matrix:
        for j in row:
            if j == row[-1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end=" ")
        print()
