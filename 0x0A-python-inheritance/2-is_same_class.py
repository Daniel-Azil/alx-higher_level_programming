#!/usr/bin/python3
"""Returns True if the object is an exact instance of the
   specified class; otherwise, it returns False.
"""


def is_same_class(obj, a_class):
    """Determines if the object is a precise instance of the
       specified class and returns True if so,
       otherwise returns False.
    """
    if type(obj) is a_class:
        return True
    return False
