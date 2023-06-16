#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    A function that returns the weighted average of all integers tuple

    Parameter:
     - my_list = the list to use

    Return:
       - the weighted average
    """

    score_1 = []
    weight_1 = []

    for i in my_list:
        a, b = i
        weight_1.append(b)
        score_1.append(a * b)

    total_s = 0
    for i in score_1:
        total_s += i

    sum_1 = 0
    for i in weight_1:
        sum_1 += i

    return (total_s/sum_1)
