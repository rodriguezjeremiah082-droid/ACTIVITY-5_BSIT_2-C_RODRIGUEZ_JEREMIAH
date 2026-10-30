"""main.py - Menu-driven program for the Stacks and Queues lab.

Choose an implementation, perform any operation, and see the state of the
structure printed after every operation.

Run:  python main.py
"""

import sys

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

IMPLEMENTATIONS = {
    "1": ("Array Stack", "stack", True),
    "2": ("Linked Stack", "stack", False),
    "3": ("Array Queue (circular)", "queue", True),
    "4": ("Linked Queue", "queue", False),
}

# (label, method name, needs a value)
STACK_OPS = [("Push", "push", True), ("Pop", "pop", False), ("Peek", "peek", False)]
QUEUE_OPS = [("Enqueue", "enqueue", True), ("Dequeue", "dequeue", False),
             ("Peek front", "peek_front", False)]


class QuitProgram(Exception):
    """Raised when input ends (EOF) so the program can exit cleanly."""


def read(prompt):
    try:
        text = input(prompt).strip()
    except EOFError:
        raise QuitProgram
    if not sys.stdin.isatty():   # when input is piped, echo it so sample runs are readable
        print(text)
    return text


def read_capacity():
    while True:
        text = read("Enter capacity (positive integer): ")
        if text.isdigit() and int(text) >= 1:
            return int(text)
        print("  Invalid capacity. Try again.")


def create(choice):
    name, kind, is_array = IMPLEMENTATIONS[choice]
    if choice == "1":
        return ArrayStack(read_capacity())
    if choice == "2":
        return LinkedStack()
    if choice == "3":
        return ArrayQueue(read_capacity())
    return LinkedQueue()


def run_structure(choice):
    name, kind, _ = IMPLEMENTATIONS[choice]
    ds = create(choice)
    ops = STACK_OPS if kind == "stack" else QUEUE_OPS
    extra = [("Is empty?", "is_empty", False), ("Is full?", "is_full", False)]
    all_ops = ops + extra
    print(f"\n{name} created.")
    print(f"State: {ds}")

    while True:
        print(f"\n--- {name} operations ---")
        for i, (label, _, _) in enumerate(all_ops, start=1):
            print(f"  {i}. {label}")
        print("  0. Back to implementation menu")
        choice_text = read("Choose an operation: ")
        if choice_text == "0":
            return
        if not (choice_text.isdigit() and 1 <= int(choice_text) <= len(all_ops)):
            print("  Invalid choice.")
            continue
        label, method, needs_value = all_ops[int(choice_text) - 1]
        try:
            if needs_value:
                value = read("  Enter value: ")
                getattr(ds, method)(value)
                print(f"  {label}: {value!r} done.")
            else:
                result = getattr(ds, method)()
                print(f"  {label} -> {result!r}")
        except (IndexError, OverflowError) as error:
            print(f"  ERROR: {error}")
        print(f"State: {ds}")


def main():
    print("=== Stacks and Queues: Array vs. Linked List ===")
    try:
        while True:
            print("\nChoose an implementation:")
            for key, (name, _, _) in IMPLEMENTATIONS.items():
                print(f"  {key}. {name}")
            print("  0. Exit")
            choice = read("Your choice: ")
            if choice == "0":
                break
            if choice not in IMPLEMENTATIONS:
                print("  Invalid choice.")
                continue
            run_structure(choice)
    except QuitProgram:
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()
