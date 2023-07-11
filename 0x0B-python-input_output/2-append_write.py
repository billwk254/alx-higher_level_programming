#!/usr/bin/python3


"""
Module: append_write.py

A module that provides a function for appending a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file to append
        text (str): The string to append to the file

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        characters_added = file.write(text)
        return characters_added
