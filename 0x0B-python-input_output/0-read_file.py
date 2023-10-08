#!/usr/bin/python3

"""A python Module that reads text from a given file"""


def read_file(filename=""):
    """
        A custom function that reads texts from a file

        Args:
           filename: The argument of file to be passed and read
    """

    with open(filename, "r", encoding="utf-8") as given_file:
        content = given_file.read()
        print(content, end="")

