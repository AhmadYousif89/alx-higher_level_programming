#!/usr/bin/python3
"""Define a Node Class"""


class Node:
    """Create some nodes for the single linked list."""

    def __init__(self, data=0, next_node=None) -> None:
        """Initialize the Node class.

        Args:
        - data (int): The data of the node.
        - next_node (None): Reference to the next node in the list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get/Set the data value of each node."""
        return self.__data

    @data.setter
    def data(self, data=0):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data

    @property
    def next_node(self):
        """Get/Set the next_node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node=None):
        if not isinstance(next_node, Node) and not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node


"""Define a SinglyLinkedList Class"""


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    Attributes:
    - __head: The head node of the linked list.
    """

    def __init__(self) -> None:
        """Initialize the Node class."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.__next_node
        return result.rstrip()

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.
        Parameters:
        - value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if not self.__head:
            new_node.__next_node = None
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.__next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.__next_node and current.__next_node.data < value:
            current = current.__next_node

        new_node.__next_node = current.__next_node
        current.__next_node = new_node
