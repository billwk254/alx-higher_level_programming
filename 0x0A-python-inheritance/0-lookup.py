#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list containing the attributes and methods of the object.
    """
    return dir(obj)
