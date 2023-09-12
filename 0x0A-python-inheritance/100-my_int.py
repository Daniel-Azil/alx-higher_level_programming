#!/usr/bin/python3
"""A module that contains a class MyInt and
   and inherits from the int class.
"""


class MyInt(int):
    """ Initialised a subclass """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
