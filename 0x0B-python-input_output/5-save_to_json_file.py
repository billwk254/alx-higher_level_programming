#!/usr/bin/python3


"""
Module: save_to_json_file

A module that writes an object to a text file using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj (object): The object to be saved to the file.
        filename (str): The name of the file to write the object to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
