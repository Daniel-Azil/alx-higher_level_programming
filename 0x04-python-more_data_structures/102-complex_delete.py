#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dal_var = list(a_dictionary.keys())

    for elementL in dal_var:
        if value == a_dictionary.get(elementL):
            del a_dictionary[elementL]

    return (a_dictionary)
