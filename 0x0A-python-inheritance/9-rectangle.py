#!/usr/bin/python3
""" Submodule 'rectangle' containing classes
    and functions related to rectangles.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from the BaseGeometry class."""
    def __init__(self, width, height):
        """Constructor"""
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
