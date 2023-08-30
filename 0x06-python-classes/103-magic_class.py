#!/usr/bin/python3
"""creating a MagicClass."""

import math


class MagicClass:
    """class name magic circle."""

    def __init__(self, radius=0):
        """method for instanctiation.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """method for instanctiation."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """method for instanctiation."""
        return (2 * math.pi * self.__radius)
