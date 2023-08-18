#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    vdict_element_ = 0
    dal_var = 0
    for aToz in my_list:
        vdict_element_ += aToz[0] * aToz[1]
        dal_var += aToz[1]
    return (vdict_element_ / dal_var)
