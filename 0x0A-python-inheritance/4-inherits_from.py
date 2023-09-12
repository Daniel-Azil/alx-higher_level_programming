#!/usr/bin/python3
"""Restricts the module to only allow subclassing.
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a
    class that inherits, either directly or indirectly,
    from the specified class; otherwise, it returns False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
