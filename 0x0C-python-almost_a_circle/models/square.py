#!/usr/bin/python3


"""
square.py - This module contains the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - A class that represents a square

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
            y (int, optional): The y-coordinate of the square.
            id (int, optional): The id to assign to the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square.

        Args:
            *args: The list of arguments - no-keyworded arguments.
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            **kwargs: A dictionary of key-value arguments
                Each key represents an attribute to the instance.

        Note:
            **kwargs must be skipped if *args exists and is not empty.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
