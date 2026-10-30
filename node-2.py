"""node.py - Singly linked list node shared by LinkedStack and LinkedQueue."""


class Node:
    """A single node of a singly linked list."""

    def __init__(self, value):
        self.value = value   # data stored in this node
        self.next = None     # reference to the next node (None = end of list)
