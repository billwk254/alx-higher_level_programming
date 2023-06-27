#!/usr/bin/python3


"""
A module that defines a Square class
"""


class Square:
    """
    A class representing a Square

    Attributes:
        __size (int): The square size
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): Square size.The default is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
