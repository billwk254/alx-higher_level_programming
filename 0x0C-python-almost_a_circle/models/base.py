#!/usr/bin/python3


"""
base.py - This module contains the Base class
"""


class Base:
    """
    Base - The base class to manage the 'id' attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): The id to assign to the 'id' attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
