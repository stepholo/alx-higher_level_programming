#!/usr/bin/python3
def roman_to_int(roman_sting):
    """
    A function that converts roman number to an arabic number

    Parameter:
     - roman_sting: The string containing the roman number

    Return:
     - An integer
    """
    from functools import reduce

    dict_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(dict_n)

    string = roman_sting
    if type(string) is not str:
        return 0
    elif string is None:
        return 0
    else:
        roman = string.upper()
        digit = []

        for letter in roman:
            for key in keys:
                if key == letter:
                    digit.append(dict_n[key])

        i = 0
        while i < len(digit) - 1:
            if digit[i] < digit[i + 1]:
                difference = digit[i + 1] - digit[i]
                digit[i] = difference
                del digit[i + 1]

            else:
                i += 1

        arabic_number = reduce(lambda x, y: x + y, digit)

        return arabic_number
