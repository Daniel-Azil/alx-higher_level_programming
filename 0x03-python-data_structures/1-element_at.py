#!/usr/bin/python3
def element_at(my_list, idx):
    list_num_len = len(my_list)
    if idx < 0:
        return (None)
    if idx > list_num_len - 1:
        return (None)
    return(my_list[idx])
