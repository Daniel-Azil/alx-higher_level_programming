#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    var_len_1 = len(tuple_a)
    var_len_2 = len(tuple_b)
    if var_len_1 == 0:
        var_len_3 = 0
        var_len_4 = 0
    elif var_len_1 == 1:
        var_len_3 = tuple_a[0]
        var_len_4 = 0
    else:
        var_len_3 = tuple_a[0]
        var_len_4 = tuple_a[1]
    if var_len_2 == 0:
        var1 = 0
        var2 = 0
    elif var_len_2 == 1:
        var1 = tuple_b[0]
        var2 = 0
    else:
        var1 = tuple_b[0]
        var2 = tuple_b[1]
    strc_rtn = (var_len_3 + var1, var_len_4 + var2)
    return (strc_rtn)
