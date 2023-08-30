#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ Created class named Square"""
    def __init__(self, size=0):
        """ initialised an Instantiation
        """
        self.size = size

    @property
    def size(self):
        """ initialised a getter for __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Initialised a setter for size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Initialised method named area
        """
        return self.__size**2

    def my_print(self):
        """ a method to print"""

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
