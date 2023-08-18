#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    vdict_element_ = a_dictionary.copy()
    dal_var = list(vdict_element_.keys())

    for aToz in dal_var:
        vdict_element_[aToz] *= 2

    return (vdict_element_)
