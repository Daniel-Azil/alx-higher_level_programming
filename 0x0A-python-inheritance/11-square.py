#!/usr/bin/python3
"""A module that contains a class Square that
   inherits from Rectangle (9-rectangle.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class inheritance
    """
    def __init__(self, size):
        """"Constuctor function

        Attributes:
            size (int): Length of square in
                        int datatype.
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        method that prints out [Square] <width>/<height>

        Returns:
            Returns [Square] <width>/<height>
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """Method that calculates the area of a circle
        """
        return self.__size ** 2
