"""test_driver.py - Test driver for all four classes and the application exercises.

Run:  python test_driver.py
Every check prints PASS; any failure raises an AssertionError.
"""

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from applications import is_balanced, simulate_print_queue


def check(description, condition):
    assert condition, f"FAILED: {description}"
    print(f"  PASS: {description}")


def expect_error(description, exc_type, message_part, func, *args):
    try:
        func(*args)
    except exc_type as error:
        assert message_part in str(error), f"FAILED: wrong message: {error}"
        print(f"  PASS: {description} -> {exc_type.__name__}: {error}")
        return
    raise AssertionError(f"FAILED: {description} did not raise {exc_type.__name__}")


def test_stack(name, stack, capacity_limited):
    print(f"\n[{name}]")
    check("new stack is empty", stack.is_empty())
    expect_error("pop on empty (underflow)", IndexError, "underflow", stack.pop)
    expect_error("peek on empty", IndexError, "empty", stack.peek)
    for item in "ABC":
        stack.push(item)
    print(f"  {stack}")
    check("peek returns C (top)", stack.peek() == "C")
    check("pop returns C", stack.pop() == "C")
    check("peek then returns B", stack.peek() == "B")
    check("pop returns B then A (LIFO)", (stack.pop(), stack.pop()) == ("B", "A"))
    check("stack is empty again", stack.is_empty())
    if capacity_limited:
        for item in range(3):
            stack.push(item)
        check("is_full when at capacity", stack.is_full())
        expect_error("push on full (overflow)", OverflowError, "overflow", stack.push, 99)
        check("stack unchanged after failed push", stack.peek() == 2)
    else:
        for item in range(1000):
            stack.push(item)
        check("no overflow with 1000 pushes", not stack.is_full() and len(stack) == 1000)


def test_queue(name, queue, capacity_limited):
    print(f"\n[{name}]")
    check("new queue is empty", queue.is_empty())
    expect_error("dequeue on empty (underflow)", IndexError, "underflow", queue.dequeue)
    expect_error("peek_front on empty", IndexError, "empty", queue.peek_front)
    for item in "ABC":
        queue.enqueue(item)
    print(f"  {queue}")
    check("peek_front returns A", queue.peek_front() == "A")
    check("dequeue order is A, B, C (FIFO)",
          (queue.dequeue(), queue.dequeue(), queue.dequeue()) == ("A", "B", "C"))
    check("queue is empty again", queue.is_empty())
    if capacity_limited:
        for item in range(4):
            queue.enqueue(item)
        check("is_full when at capacity", queue.is_full())
        expect_error("enqueue on full (overflow)", OverflowError, "overflow", queue.enqueue, 99)
    else:
        for item in range(1000):
            queue.enqueue(item)
        check("no overflow with 1000 enqueues", not queue.is_full() and len(queue) == 1000)


def test_circular_wraparound():
    print("\n[ArrayQueue wrap-around demonstration, capacity 4]")
    q = ArrayQueue(4)
    for item in "ABCD":
        q.enqueue(item)
    print(f"  after enqueue A,B,C,D : {q}")
    check("dequeue A", q.dequeue() == "A")
    check("dequeue B", q.dequeue() == "B")
    print(f"  after dequeue A,B     : {q}")
    q.enqueue("E")   # goes to physical index 0 (wrap-around)
    q.enqueue("F")   # goes to physical index 1
    print(f"  after enqueue E,F     : {q}")
    check("E and F wrapped to indexes 0 and 1", q.data == ["E", "F", "C", "D"])
    check("queue is full (size counter, not front==rear)", q.is_full())
    check("FIFO order preserved across wrap: C, D, E, F",
          [q.dequeue() for _ in range(4)] == ["C", "D", "E", "F"])
    check("queue empty after draining", q.is_empty())


def test_linked_queue_reset():
    print("\n[LinkedQueue rear reset when emptied]")
    q = LinkedQueue()
    q.enqueue(1)
    q.dequeue()
    check("front is None after emptying", q.front is None)
    check("rear is None after emptying", q.rear is None)
    q.enqueue(2)
    q.enqueue(3)
    check("enqueue after emptying works (2 then 3)", (q.dequeue(), q.dequeue()) == (2, 3))


def test_applications():
    print("\n[Application exercises]")
    for text, expected in [("()", True), ("([]{})", True), ("{[()]}", True), ("(]", False),
                           ("((())", False), ("())", False), ("a(b[c]{d}e)f", True),
                           ("", True), ("}{", False)]:
        check(f"is_balanced({text!r}) is {expected}", is_balanced(text) == expected)
    report = simulate_print_queue([("J1", 5), ("J2", 12), ("J3", 3)])
    check("print jobs served in FIFO order", [r["job_id"] for r in report] == ["J1", "J2", "J3"])
    check("pages waited are 0, 5, 17", [r["pages_waited"] for r in report] == [0, 5, 17])


if __name__ == "__main__":
    test_stack("ArrayStack (capacity 3)", ArrayStack(3), True)
    test_stack("LinkedStack", LinkedStack(), False)
    test_queue("ArrayQueue (capacity 4)", ArrayQueue(4), True)
    test_queue("LinkedQueue", LinkedQueue(), False)
    test_circular_wraparound()
    test_linked_queue_reset()
    test_applications()
    print("\nAll tests passed.")
