#!/usr/bin/python3
def safe_print_division(a, b):
    """
    A function that divides 2 integers and prints the result

    Parameter:
      a: First integer
      b: Second integer

    Return:
      The result of division on none
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
