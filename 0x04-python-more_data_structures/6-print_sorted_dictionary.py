#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    var_azlist = list(a_dictionary.keys())
    var_azlist.sort()
    for aToz in var_azlist:
        print("{}: {}".format(aToz, a_dictionary.get(aToz)))
