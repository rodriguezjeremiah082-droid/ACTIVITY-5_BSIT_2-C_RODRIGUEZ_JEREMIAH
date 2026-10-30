"""array_stack.py - Fixed-capacity stack built on a Python list (LIFO)."""


class ArrayStack:
    """Stack stored in a fixed-size list. `top` is the index of the top element
    (-1 when the stack is empty)."""

    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        """Insert value at the top. O(1). Raises OverflowError if full."""
        if self.is_full():
            raise OverflowError(
                f"Stack overflow: cannot push {value!r}, "
                f"the stack is full (capacity {len(self.data)})")
        self.top = self.top + 1          # move top up first
        self.data[self.top] = value      # then store

    def pop(self):
        """Remove and return the top element. O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.data[self.top]      # read the top value first
        self.data[self.top] = None       # clear the slot (avoids stale references)
        self.top = self.top - 1          # then move top down
        return value

    def peek(self):
        """Return the top element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek at")
        return self.data[self.top]

    def __len__(self):
        return self.top + 1

    def __str__(self):
        items = [str(self.data[i]) for i in range(self.top, -1, -1)]
        return (f"ArrayStack (top -> bottom): [{', '.join(items)}] | "
                f"size={len(self)}/{len(self.data)} | top index={self.top}")
