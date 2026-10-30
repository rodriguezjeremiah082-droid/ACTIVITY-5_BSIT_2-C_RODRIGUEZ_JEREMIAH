# Stacks and Queues: Array vs. Linked List

Laboratory activity for **Module 5 - Fundamental Data Structures: Stacks and Queues**.
All four structures are built from first principles (no `list.insert(0, x)` or `list.pop(0)` tricks), raise descriptive exceptions on underflow and overflow, and print their state after every operation in the menu program.

## Requirements

- Python 3.8 or newer. No third-party packages are needed.

## Files

| File | Description |
|------|-------------|
| `node.py` | `Node` class shared by the linked stack and linked queue. |
| `array_stack.py` | `ArrayStack`: fixed-capacity stack using a list and a `top` index (starts at `-1`). |
| `linked_stack.py` | `LinkedStack`: singly linked stack; push and pop at the head, no fixed capacity. |
| `array_queue.py` | `ArrayQueue`: circular queue using modulo arithmetic with `front` and a `size` counter. |
| `linked_queue.py` | `LinkedQueue`: singly linked queue with head (`front`) and tail (`rear`) references. |
| `main.py` | Menu-driven program: choose an implementation and run any operation. |
| `applications.py` | Application exercises: balanced-parentheses checker and print-queue simulation. |
| `test_driver.py` | Automated test driver covering all classes, error handling and wrap-around. |
| `sample_runs.md` | Captured sample runs, including underflow and overflow handling. |
| `analysis.md` | Written answer to the analysis question. |

## Operations

| Structure | Operations (all O(1)) |
|-----------|-----------------------|
| `ArrayStack`, `LinkedStack` | `push(x)`, `pop()`, `peek()`, `is_empty()`, `is_full()` |
| `ArrayQueue`, `LinkedQueue` | `enqueue(x)`, `dequeue()`, `peek_front()`, `is_empty()`, `is_full()` |

- Array versions have a fixed capacity: `is_full()` can be true and `push` / `enqueue` raise `OverflowError` when full.
- Linked versions have no fixed capacity: `is_full()` always returns `False`.
- `pop`, `peek`, `dequeue` and `peek_front` on an empty structure raise `IndexError` (underflow).

## How to run

Run every command from the repository folder.

**1. Menu-driven program** (all four implementations)

```bash
python main.py
```

1. Choose an implementation: `1` Array Stack, `2` Linked Stack, `3` Array Queue (circular), `4` Linked Queue. The array versions ask for a capacity.
2. Choose an operation by number and enter a value when asked.
3. The state of the structure is printed after every operation. Errors (underflow / overflow) are shown as `ERROR: ...` and the program keeps running.
4. Enter `0` to go back, then `0` again to exit.

**2. Each implementation individually** (in the menu program)

```bash
python main.py   # then choose 1 for ArrayStack
python main.py   # then choose 2 for LinkedStack
python main.py   # then choose 3 for ArrayQueue (circular)
python main.py   # then choose 4 for LinkedQueue
```

**3. Application exercises**

```bash
python applications.py
```

Runs the stack-based balanced-parentheses checker for `()`, `[]`, `{}` and the FIFO print-queue simulation, which reports the print order and how many pages were printed before each job started.

**4. Test driver**

```bash
python test_driver.py
```

Prints `PASS` for each check and `All tests passed.` at the end. It includes the circular-queue wrap-around demonstration (enqueue past the physical end of the array) and the underflow / overflow checks.

## Design notes

- `ArrayStack`: `top` starts at `-1`; `push` increments `top` then stores, `pop` reads then decrements.
- `LinkedStack`: operates only at the head, keeping `pop` O(1).
- `ArrayQueue`: the rear index is computed as `(front + size) % capacity`, and a `size` counter (not `front == rear`) tells empty from full.
- `LinkedQueue`: `rear` is reset to `None` whenever the queue becomes empty.

## Author

Name: _(replace with your name)_  
Section: _(replace with your section)_
