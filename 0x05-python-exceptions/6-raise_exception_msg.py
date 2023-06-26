#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    A function that raises a name exception with a message
    Parameter:
      message: The message to be raised
    """
    try:
        raise NameError(message)
    except NameError as e:
        raise NameError(e)
