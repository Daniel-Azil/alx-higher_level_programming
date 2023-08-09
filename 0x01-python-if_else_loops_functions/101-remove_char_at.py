#!/usr/bin/python3
def remove_char_at(str, n):
    copy_of_str = ""
    for elements in range(len(str)):
        if elements != n:
            elements = elements + str[elements]
    return (elements)
