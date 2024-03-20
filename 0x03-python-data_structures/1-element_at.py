#!/usr/bin/python3
""" Returns the element at a particular index
    
    Args:
    my_list: List containing elements
    idx: Index of element to be returned

    Return:
    element at given index
"""
def element_at(my_list,idx):
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
