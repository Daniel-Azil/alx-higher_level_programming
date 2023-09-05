#!/usr/bin/python3
""" initialising class with constructor, getter, setter, str, repr, and
    del functinality
"""


class Rectangle:
    """ initializing instance attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializing constructor with instance attributes"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ method with getter functionality
        """
        return self.__width

    @property
    def height(self):
        """ method with getter functionality
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ method with setter functionality
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ method with setter functionality
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method that returns the area of the class"""
        return self.__width * self.__height

    def perimeter(self):
        """ method that returns the perimeter of the class"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ method that returns #
        """
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ method that displays given strings
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ method that display given string when an instance attribute is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
