#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    list_copy[idx] = element
    return (list_copy)
