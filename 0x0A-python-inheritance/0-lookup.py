#!/usr/bin/python3
"""Retrieves the list of attributes and methods
   that an object possesses.
"""


def lookup(obj):
    """Provides a list of accessible attributes."""
    return dir(obj)
