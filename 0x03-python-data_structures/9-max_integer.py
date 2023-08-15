#!/usr/bin/python3
def max_integer(my_list=[]):
    var_list_size = len(my_list)
    var = my_list[0]
    if var_list_size == 0:
        return (None)
    for i in range(1, var_list_size):
        if my_list[i] > var:
            var = my_list[i]
    return (var)
