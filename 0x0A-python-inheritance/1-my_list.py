#!/usr/bin/python3


"""
A module with Mylist class
"""


class MyList(list):
    """
    Custom list class that inherits from list.

    Public Methods:
        print_sorted(self): Prints the list in sorted order (ascending sort).
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).

        Example:
            >>> my_list = MyList([3, 1, 2])
            >>> my_list.print_sorted()
            [1, 2, 3]
        """
        sorted_list = sorted(self)
        print(sorted_list)
