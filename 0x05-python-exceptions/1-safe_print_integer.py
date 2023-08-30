#!/usr/bin/python3
def safe_print_integer(value):
    """ Implementation of try and except
        functionality.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
