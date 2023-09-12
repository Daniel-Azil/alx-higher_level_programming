#!/usr/bin/python3
"""A class MyList that is derived from the list class.
"""


class MyList(list):
    """A class that inherits from the list class"""
    def print_sorted(self):
        """Displays the list in ascending sorted order.
        """
        print(sorted(self))
