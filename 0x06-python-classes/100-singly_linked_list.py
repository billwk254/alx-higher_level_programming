#!/usr/bin/python3


"""
A module with a Node and Singlylist classes
"""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): Node data
        __next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data attribute.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.

        Args:
            value (int): The data value to be assigned.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next_node attribute.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.

        Args:
            value (Node): The next node to be assigned.

        Raises:
            TypeError: If the value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list

    Attributes:
        head: The head node of the list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node at the correct position

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                current.next_node is not None and
                current.next_node.data < new_node.data
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        node = self.head
        result = ""
        while node is not None:
            result += str(node.data) + "\n"
            node = node.next_node
        return result.rstrip("\n")
