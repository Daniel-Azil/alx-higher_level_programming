#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Implementation of try and except functionality"""
    azvar = 0

    for az in range(x):
        try:
            print("{:d}".format(my_list[az]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            azvar += 1

    print()
    return (azvar)
