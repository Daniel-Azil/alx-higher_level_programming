#!/usr/bin/python3
""" Initialzation of Class of the name Sqaure"""


class Square(self, size):
    """ Defining a class named Square """

    def __init__(self, size):
        """

        Initialising instance Square
        defining conditions of type and value errors
        """

        if type(size) is not int:
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns attribute value of the class sqaure"""
        return (self.__size * self.__size)
