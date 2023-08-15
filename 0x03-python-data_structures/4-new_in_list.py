#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_num_len = len(my_list)
    var_list = my_list[:]
    if 0 <= idx < list_num_len:
        var_list[idx] = element
    return (var_list)
