#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    var_list_size = len(my_list)
    if idx < 0 or idx >= var_list_size:
        return (my_list)
    del my_list[idx]
    return (my_list)
