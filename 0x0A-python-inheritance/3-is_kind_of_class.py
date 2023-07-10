#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if it an instance of the class, False otherwise
    """
    return isinstance(obj, a_class)
