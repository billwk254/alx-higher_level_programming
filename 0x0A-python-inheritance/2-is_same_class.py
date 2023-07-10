#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if the object is exactly an instance of the specified class; False otherwise.
    """
    return obj.__class__ is a_class
