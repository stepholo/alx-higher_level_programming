#!/usr/bin/python3
def multiple_returns(sentence):
    """
    A function that returns a tuple with a length of
    a string and its first character

    Parameter:
      Setence: The strings to get its length and first character

    Return:
      tuple containing length of setence and its first character
    """
    length = len(sentence)

    if length == 0:
        return (length, None)
    else:
        return (length, sentence[0])
