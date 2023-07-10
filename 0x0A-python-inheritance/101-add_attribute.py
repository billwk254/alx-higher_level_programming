#!/usr/bin/python3


"""
A module with a function that adds a new attribute to an object
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attribute: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
