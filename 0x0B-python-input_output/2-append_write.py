#!/usr/bin/python3
"""


Module to define append_write function


"""


def append_write(filename="", text=""):
    """Function that appends text to a file

    Arg:
      filname: file to append text to
      text: The characters to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        char = f.write(text)

    return char
