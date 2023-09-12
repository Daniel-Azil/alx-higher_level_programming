#!/usr/bin/python3
""" Defines a module for creating and manipulating
    rectangles.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class that inherits from the
       BaseGeometry class, allowing for geometric calculations
       related to rectangles.
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
