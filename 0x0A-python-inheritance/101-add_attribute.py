#!/usr/bin/python3
""" A module the add attributes.
"""


def add_attribute(obj, attribute, value):
    """initialised the function to add attributes"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
