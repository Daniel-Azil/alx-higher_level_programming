#!/usr/bin/python3
""" defined a class name square"""


class Square:
    """ defined a class named a square"""

    def __init__(self, size=0):
        """initialize size of a square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """returns the area of a square
        """
        return (self.__size * self.__size)
