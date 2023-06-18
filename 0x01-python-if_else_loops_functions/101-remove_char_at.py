#!/usr/bin/python3
def remove_char_at(str, n):
    """ Removes a character of in a string

    Parameter:
      - str: The string
      - n: Character to be removed

    Return:
      - A copy of the string str without charcter n
    """
    a = str
    b = ""
    for i in range(len(a)):
        if i == n:
            continue
        else:
            b = b + a[i]

    return b
