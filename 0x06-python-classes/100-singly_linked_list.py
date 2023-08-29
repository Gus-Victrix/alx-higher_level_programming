#!/usr/bin/python3

"""Create a linked list class"""


class Node:
    """Create a Node"""
    def __init__(self, data, next_node=None):
        """I
        Init the Node
        Args:
            data (int): The data of the node
            next_node (Node): The next node
        Return: Nothing
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data
        Returns: The data
        """
        return self.__data

    @property
    def next_node(self):
        """
        Get the next_node
        Returns: The next_node
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Set the data value
        Args:
            value (int): The new value of the data
        Raises:
            TypeError: If the data isn't an int
        Returns: Nothing
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node
        Args:
            value (Node): The new value of the next_node
        Raises:
            TypeError: If the next_node is not can be None
                        or must be a Node
        Returns: Nothing
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create a Linked list"""
    def __init__(self):
        """
        Init the sll
        Returns: Nothing
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert in sorted mode the linked list
        Args:
            value (int): The value to insert
        Returns: Nothing
        """
        newNode = Node(value)
        current = self.__head
        if (not current or value < current.data):
            if current:
                newNode.next_node = current
            self.__head = newNode
        elif (current):
            while (current.next_node):
                if (current.next_node.data >= value):
                    break
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        """
        Print the linked list
        Returns: String to print
        """
        res = ""
        current = self.__head
        while (current):
            res += str(current.data)
            if (current.next_node):
                res += '\n'
            current = current.next_node
        return res
