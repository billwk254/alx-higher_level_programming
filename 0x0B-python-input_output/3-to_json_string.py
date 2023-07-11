#!/usr/bin/python3


"""
Module: to_json_string.py

A module that provides a function for converting a object
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
