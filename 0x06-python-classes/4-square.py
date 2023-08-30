#!/usr/bin/python3
"""class initialization."""


class Square:
    """initailised class of the name square."""

    def __init__(self, size=0):
        """Initialize a method __init__.
           The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter for size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square number passed from the instance."""
        return (self.__size * self.__size)
