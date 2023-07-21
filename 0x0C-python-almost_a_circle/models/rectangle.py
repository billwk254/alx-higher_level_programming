#!/usr/bin/python3


"""
rectangle.py - This module contains the Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle - A class that represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): The id to assign to the rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The x-coordinate to set.

        Raises:
            TypeError: If the x-coordinate is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The y-coordinate to set.

        Raises:
            TypeError: If the y-coordinate is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value
