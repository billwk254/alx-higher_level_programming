#!/usr/bin/python3


"""
Module: write_file.py

A module that provides a function for writing a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    Args:
      filename (str): The name of the file to write (default is empty string).
      text (str): The string to write to the file (default is empty string).

    Returns:
      int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        characters_written = file.write(text)
        return characters_written
