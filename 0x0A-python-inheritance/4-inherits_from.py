#!/usr/bin/python3


"""
Module that checks if object is instance of class that inherited
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if the object is an instance of a class,False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
