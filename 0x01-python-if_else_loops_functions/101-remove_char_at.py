#!/usr/bin/python3
def remove_char_at(str, n):
    copy_of_str = ""
    az_var = 0
    for element in str:
        if az_var != n:
            copy_of_str += element
        az_var += 1
    return copy_of_str
