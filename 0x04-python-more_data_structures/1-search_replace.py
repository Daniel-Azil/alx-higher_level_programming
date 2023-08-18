#!/usr/bin/python3
def search_replace(my_list, search, replace):
    v_element_ = list(map(lambda x: replace if x == search else x, my_list))
    return (v_element_)
