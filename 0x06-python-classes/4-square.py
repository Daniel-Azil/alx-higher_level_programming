#!/usr/bin/python3
""" Initilization of a class."""


class Square:
    """ Defined a class named Square."""

    def __init__(self, size):
        """ Made an instantiation."""
        self.size = size

    @property
    def size(self, size):
    """Getter and setter of size for square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ initialised setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ initialised method named area."""
        return (self.__size * self.__size)
