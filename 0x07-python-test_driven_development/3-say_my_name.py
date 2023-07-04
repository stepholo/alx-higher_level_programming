#!/usr/bin/python3
"""


This is a module that defines a function that prints a name


"""


def say_my_name(first_name, last_name=""):
    """ Function that prints my name is

    Arg:
      first_name: First name
      last_name: Last name. empty string by default

    Return:
      prints the full name

    """
    new_first = ""
    new_second = ""

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not first_name.isalpha():
        raise ValueError(f"{first_name} is not a valid name")

    else:
        new_first = first_name

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if not last_name.isalpha() and last_name != "":
        raise ValueError(f"{last_name} is not a valid name")

    else:
        new_second = last_name
    full_name = new_first + " " + new_second

    print("My name is {}".format(full_name))
