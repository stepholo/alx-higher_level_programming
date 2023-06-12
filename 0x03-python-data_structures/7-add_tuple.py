def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise assuming they contain integers

    Parameters:
     - tuple_a: First tuple
     - tuple_b: Second tuple

    Return:
      - A new tuple containing the element-wise sum
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuble_a = 0, 0
        else:
            tuble_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
