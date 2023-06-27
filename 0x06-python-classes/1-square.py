#!/usr/bin/python3


"""
A module with a square class which has a private instance size
"""


class Square:
    """
A class with a related size value

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The square size
        """
        self.__size = size
