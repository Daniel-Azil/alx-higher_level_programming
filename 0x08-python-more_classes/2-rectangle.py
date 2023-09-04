#!/usr/bin/python3
"""
      Initialised a class with constructor, getter and setter functionalities
"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ constructor containing variable attributes"""
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

    def area(self):
        """ Method that returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """ method that returns the perimeter calculation"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
