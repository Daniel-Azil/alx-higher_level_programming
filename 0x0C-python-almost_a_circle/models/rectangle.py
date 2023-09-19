#!/usr/bin/python3

"""A module containing the class 'Rectangle'"""

from models.base import Base

class Rectangle(Base):
    """A custom class named Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Defined the constructor for the class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Initialised a getter for the attribute width"""
        return self.__width

    @width.setter
    def width(self, given_num):
        """Initialised setter for the attribute width"""
        if type(given_num) != int:
            raise TypeError("width must be an integer")
        if given_num <= 0:
            raise ValueError("width must be > 0")
        self.__width=given_num

    @property
    def height(self):
        """Initialised getter for the atribute height as a 
           private attribte
        """
        return self.__height

    @height.setter
    def height(self, given_num):
        """Initialised a setter method for the private 
           attribute height
        """
        if type(given_num) != int:
            raise TypeError("height must be an integer")
        if given_num <=0:
            raise ValueError("height must be > 0")
        self.__height = given_num

    @property
    def x(self):
        """Initialised a getter for the attribute x with the
           decorator function @property
        """
        return self.__x

    @x.setter
    def x(self, given_num):
        """ Initialised setter for the attribute x with the setter decorator
        """
        if type(given_num) != int:
            raise TypeError("x must be an integer")
        if given_num < 0:
            raise ValueError("x must be >= 0")
        self.__x = given_num

    @property
    def y(self):
        """ Initialised getter for the attribute y with the decorator '@property'
        """
        return self.__y


    @y.setter
    def y(self, given_num):
        """Initialised setter for the attribute y with the decorator '@y.setter'
        """
        if type(given_num) != int:
            raise TypeError("y must be an integer")
        if given_num < 0:
            raise ValueError("y must be >= 0")
        self.__y = given_num


    def area(self):
        """ A custom method that returns the area of the Class Rectangle"""
        return self.width * self.height

    def display(self):
        """ Initialising the display functionality for the class
            Rectangle
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        rectangle_str = ""
        for y in range(self.y):
            rectangle_str += "\n"
        for h in range(self.height):
            rectangle_str += " " * self.x
            rectangle_str += "#" * self.width
            rectangle_str += "\n"
        print(rectangle_str)

    def update(self, *args, **kwargs):
        """ A custom function that updaates the class Rectangle with
            un-specified set of key words and inputs

            Args:
                *args: Updated values of the instance attributes
                **Kwarg: Updated key of the instance attributes
        """
        if args and len(args) != 0:
            count = 0
            for value in args:
                if count == 0:
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif count == 1:
                    self.width = value
                elif count == 2:
                    self.height = value
                elif count == 3:
                    self.x = value
                elif count == 4:
                    self.y = value
                count += 1

        elif kwargs and len(kwargs) != 0:
            for count_key, count_value  in kwargs.items():
                if count_key == "id":
                    if count_value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = count_value
                elif count_key == "width":
                    self.width = count_value
                elif count_key == "height":
                    self.height = count_value
                elif count_key == "x":
                    self.x = count_value
                elif count_key == "y":
                    self.y = count_value

    def to_dictionary(self):
        """ converts given input to dictionary"""
        return {
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
            "id": self.id
            }



    def __str__(self):
        """A class Method the returns given functionality"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

