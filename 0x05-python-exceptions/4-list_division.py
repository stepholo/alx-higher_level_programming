#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides element by element 2 lists

    Parameter:
       my_list_1: The first list
       my_list_2: The second list
       list_length: The number of times to do the division

    Returns:
       a new list with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
