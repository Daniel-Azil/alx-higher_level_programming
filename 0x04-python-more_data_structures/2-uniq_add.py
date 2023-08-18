#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_hash_set_az = set(my_list)
    az_var = 0

    for aToz in list_hash_set_az:
        az_var += aToz

    return (az_var)
