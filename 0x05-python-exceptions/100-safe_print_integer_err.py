#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ A function that prints an integer
    Arg:
       value: value to print
    """
    try:
        print("{:d}".format(value), end='\n')
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
