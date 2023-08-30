#!/usr/bin/python3
""" Initialization of class"""


class Square:
    """ initialized class named sqaure"""

    def __init__(self, size=0)::
        """ method instantiation """
        self.size = size

    @property
    def size(self):
        """getter for sqaure class
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for sqaure class
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """ defined method named area
        """
        return self.__size**2

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size
