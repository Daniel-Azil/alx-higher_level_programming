#!/usr/bin/python3
"""
    Initialised a class with constructor, setter and
    getter functionaliies
"""


class Rectangle:
    """ initialised constructor with instance attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
        """  method with setter functionality
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
