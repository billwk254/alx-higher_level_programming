#!/usr/bin/python3


"""
A module with the is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if the object is an instance of the class,false otherwise
    """
    return obj.__class__ is a_class
