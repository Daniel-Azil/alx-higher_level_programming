#!/usr/bin/python3
"""Introduction to the fundamental geometry class
   known as BaseGeometry.
"""


class BaseGeometry:
    """Representation of the fundamental geometry
      class, BaseGeometry.
    """

    def area(self):
        """Feature has not been defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if a parameter is an integer and greater
        than zero.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
             TypeError: If param_value is not an integer.
             ValueError: If param_value is less than or equal
                         to zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
