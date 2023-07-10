#!/usr/bin/python3


"""
A module with a class representing a rebellious integer
"""


class MyInt(int):
    """
    Class representing a rebellious integer.

    Attributes:
        value (int): The value of the integer.
    """

    def __new__(cls, value):
        """
        Creates a new MyInt instance.

        Args:
            value (int): The value of the integer.

        Returns:
            MyInt: A new instance of MyInt.
        """
        return super().__new__(cls, value)

    def __eq__(self, other):
        """
        Override the equality operator (==).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
