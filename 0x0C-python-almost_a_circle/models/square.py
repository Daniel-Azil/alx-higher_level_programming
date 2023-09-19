#!/usr/bin/python3

""" A modeule that contains the class Square with it's own given
    given functionalties
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that inherits from the class Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Created constructor for the class inheriting the
            attributes of the class Rectangle
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Initialised getter functionality for the
            the instance attribute size
        """
        return self.width

    @size.setter
    def size(self, given_num):
        """ Initialised setter functionality for the instance
            attribute size
        """
        self.width = given_num
        self.height = given_num

    def update(self, *args, **kwargs):
        """ Initialised a custom function that sets in an
            un-specified count of values and key values
            arguments
        """
        if args and len(args) != 0:
            arg_count = 0
            for spf_value in args:
                if arg_count == 0:
                    if spf_value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = spf_value
                elif arg_count == 1:
                    self.size = spf_value
                elif arg_count == 2:
                    self.x = spf_value
                elif arg_count == 3:
                    self.y = spf_value
                arg_count += 1
        elif kwargs and len(kwargs) != 0:
            for arg_keyValue, arg_value in kwargs.items():
                if arg_keyValue == "id":
                    if arg_value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg_value
                elif arg_keyValue == "size":
                    self.size = arg_value
                elif arg_keyValue == "x":
                    self.x = arg_value
                elif arg_keyValue == "y":
                    self.y = arg_value

    def to_dictionary(self):
        """ converts given input of the parameters into to key/values
            of dictionaries
        """
        return {
                "size": self.size,
                "x": self.x,
                "y": self.y,
                "id": self.id
                }

    def __str__(self):
        """ Display functionality of the class Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
