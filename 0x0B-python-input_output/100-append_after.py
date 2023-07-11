#!/usr/bin/python3


"""
Module: append_after.py

A module that provides a function for inserting a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file

    Args:
        filename (str): The name of the file to modify
        search_string (str): The string to search for
        new_string (str): The line of text to insert

    Returns:
        None
    """
    lines = []
    with open(filename, mode="r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, mode="w") as file:
        file.writelines(lines)
