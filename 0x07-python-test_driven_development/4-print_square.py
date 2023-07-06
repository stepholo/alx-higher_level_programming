#!/usr/bin/python3
def print_square(size):
    """prints a square with the character #
    arg:
      size: length of the square
    Return:
       area of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            if i < size - 1:
                print("{}".format('#' * size), end='\n')
            else:
                print("{}".format('#' * size))
