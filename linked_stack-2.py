"""linked_stack.py - Stack built on a singly linked list (LIFO, no fixed capacity)."""

from node import Node


class LinkedStack:
    """Pushes and pops at the HEAD of the list, so both are O(1).
    (Popping from the tail of a singly linked list would be O(n).)"""

    def __init__(self):
        self.top = None      # head of the list = top of the stack
        self._size = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        """A linked stack never fills up (only memory limits it)."""
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top     # new node points to old top
        self.top = node          # new node becomes the top
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next   # move top down the chain
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek at")
        return self.top.value

    def __len__(self):
        return self._size

    def __str__(self):
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return f"LinkedStack (top -> bottom): [{', '.join(items)}] | size={self._size}"
