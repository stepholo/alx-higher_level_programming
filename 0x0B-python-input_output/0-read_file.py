#!/usr/bin/python3
"""


Module to define read_file


"""


def read_file(filename=""):
    """Function to read a text file in UTF8 encoding

    Arg:
       filename: the file to read it's content

    Return:
       prints the content to the stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
