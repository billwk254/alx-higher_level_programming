#!/usr/bin/python3


"""
This module provides a function to indent text.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces
    text = text.strip()

    # Initialize an empty string for the indented text
    indented_text = ""

    # Iterate over each character in the text
    for char in text:
        indented_text += char

        # Check if the character is ., ? or :
        if char in ['.', '?', ':']:
            indented_text += "\n\n"

    print(indented_text)
