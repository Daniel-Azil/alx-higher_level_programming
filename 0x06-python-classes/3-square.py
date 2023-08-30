#!/usr/bin/python3
""" Initialzation of Class """


class Square(self, size):
    """ Defining a class named Square """

    def __init__(self, size):
        """ 
        Initialising instance private attribute
        defining conditions of type and value errors
        """
        if type(size) is not int:
            print("size must be an integer")
        elif size < 0:
            print("")
        else:
            self.__size = size

    def area(self):
        return(self.__size * self.__size)
