#!/usr/bin/python3
"""


Module to define write_file


"""


def write_file(filename="", text=""):
    """A function that writes a strings to a text file(UTF8)
       and returns the number of the characters

    Arg:
       filename: The file to write to
       text: The text to write

    Return:
      the number of charactes written
    """
    with open(filename, "w", encoding="utf-8") as f:
        char = f.write(text)

    return char
