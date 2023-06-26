#!/usr/bin/python3
def safe_print_integer_err(value):
    """ A function that prints an integer """
    import sys
    try:
        print("{:d}".format(value), end='\n')
        return True
    except ValueError:
        error_message = "Unknown format code 'd' for object of type 'str'"
        print("Exception: {}".format(error_message), file=sys.stderr)
        return False
