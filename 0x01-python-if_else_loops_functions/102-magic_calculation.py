#!/usr/bin/pyton3
def magic_calculation(a, b, c):
    """ A function generated from a python bytecode

    Parameter:
      - a: First digit
      - b: Second digit
      - c: The third digit

    Return:
      - Whst is in the bytecode
    """
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
