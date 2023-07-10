#!/usr/bin/python3


"""
A module with a class representing the base geometry
"""


class BaseGeometry:
    """
    Base class representing the base geometry.

    Public Methods:
        area(self): Raises an Exception message
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented.")
