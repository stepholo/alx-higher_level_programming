#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """A function that executes function safely

    Arg:
      fct: Pointer to a function
      *args: pointer to function fct parameters

    Return:
      The result of the function else None and exception error
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
