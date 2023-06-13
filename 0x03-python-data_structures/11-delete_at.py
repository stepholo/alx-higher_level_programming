#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Function that deletes item at a a given index

    Parameters:
     - my_list: The list containing the elements
     - idx: The index specification of the element to be deleted

    Return:
     - The list without the deleted value
    """
    if idx <= 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        for i in range(len(my_list) - 1):
            if i == idx:
                del my_list[i:(i+1)]
        return my_list
