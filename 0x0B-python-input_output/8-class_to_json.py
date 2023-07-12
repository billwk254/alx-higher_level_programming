#!/usr/bin/python3


"""
Module: class_to_json
Description: This module provides a function for converting an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures

    Args:
        obj (object): An instance of a Class.

    Returns:
        dict: The dictionary representation of the object
    """
    if not isinstance(obj, type):
        attributes = {}
        for attr in obj.__dict__:
            value = obj.__dict__[attr]
            if isinstance(value, (list, dict, str, int, bool)):
                attributes[attr] = value
        return attributes
