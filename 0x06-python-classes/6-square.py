#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialized __init__ method
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Initialised getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ initialised setter for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """initialised getter for position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """initialised method name area to return size value."""
        return (self.__size * self.__size)

    def my_print(self):
        """method used in printing the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for z in range(0, self.__position[0])]
            [print("#", end="") for az in range(0, self.__size)]
            print("")
