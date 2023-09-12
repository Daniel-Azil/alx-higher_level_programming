#!/usr/bin/python3
"""Module for inspecting classes and their subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Determines whether the object is an instance of
    the specified class or one of its derived classes,
    returning True in that case, otherwise returning False.
    """
    return isinstance(obj, a_class)
