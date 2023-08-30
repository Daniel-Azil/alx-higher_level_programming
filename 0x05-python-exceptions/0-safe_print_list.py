#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Implementation of try and except
        functionality
    """
    azvar = 0
    for az in range(x):
        try:
            print("{}".format(my_list[az]), end="")
            azvar += 1
        except IndexError:
            break
    print("")
    return (azvar)
