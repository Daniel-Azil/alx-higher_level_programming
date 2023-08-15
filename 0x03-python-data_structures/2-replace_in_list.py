#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    var_list_size = len(my_list)
    if idx > var_list_size - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
