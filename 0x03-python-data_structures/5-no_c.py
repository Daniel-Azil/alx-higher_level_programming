#!/usr/bin/python3
def no_c(my_string):
    list_num_len = len(my_string)
    pointer = 0
    string_rtn = my_string[:]
    for element in range(list_num_len):
        if (my_string[element] == 'c' or my_string[element] == 'C'):
            string_rtn = string_rtn[:(element - pointer)] + my_string[(element + 1):]
            pointer += 1
    return (string_rtn)
