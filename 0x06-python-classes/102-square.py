#!/usr/bin/python3


"""
A module containing the square class
"""


class Square:
    """
    Represents a square.

    Attributes:
        size (float or int): Square size.

    Methods:
        __init__(self, size=0): Initializes a Square instance.
        area(self): Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal based on their areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if two squares are not equal based on their areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return not self == other

    def __gt__(self, other):
        """
        Checks if the current square is greater than the other square

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Uses area to check if current square is greater than other square

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is greater,false otherwise
        """
        return self > other or self == other

    def __lt__(self, other):
        """
        Uses area to check if current square is less than other square

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the current square is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Uses area to check if current square is equal to other square

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if current square is equal
        """
        return self < other or self == other
