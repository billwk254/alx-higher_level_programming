#!/usr/bin/python3


"""
base.py - This module contains the Base class
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
