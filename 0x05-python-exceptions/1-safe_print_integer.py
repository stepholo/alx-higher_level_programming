#!/usr/bin/python3
def safe_print_integer(value):
    """ A function tha prints integer
    Parameter:
      value: The value to be printed
    Return:
      True if integer otherwise False
    """
    try:
        print("{:d}".format(value), end="\n")
        return True
    except (ValueError, TypeError):
        return False
