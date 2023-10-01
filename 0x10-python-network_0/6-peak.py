#!/usr/bin/python3
"""Module to define find_peak function
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers

        Param:
            list_of_integers: list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None

    elif len(list_of_integers) <= 2:
        return max(list_of_integers)

    new_list = []

    for i in range(len(list_of_integers) - 1):
        k = list_of_integers[i]
        j = list_of_integers[i - 1]
        m = list_of_integers[i + 1]
        if k >= j and k >= m:
            new_list.append(k)

    if not new_list:
        return max(list_of_integers)
    return find_peak(new_list)
