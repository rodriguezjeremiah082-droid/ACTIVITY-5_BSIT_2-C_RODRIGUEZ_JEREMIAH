# Sample Runs

All outputs below were produced by running the programs in this repository. For the menu runs, input was piped in, so the typed answers are echoed after each prompt.

## 1. Test driver (`python test_driver.py`)
```text

[ArrayStack (capacity 3)]
  PASS: new stack is empty
  PASS: pop on empty (underflow) -> IndexError: Stack underflow: cannot pop from an empty stack
  PASS: peek on empty -> IndexError: Stack is empty: nothing to peek at
  ArrayStack (top -> bottom): [C, B, A] | size=3/3 | top index=2
  PASS: peek returns C (top)
  PASS: pop returns C
  PASS: peek then returns B
  PASS: pop returns B then A (LIFO)
  PASS: stack is empty again
  PASS: is_full when at capacity
  PASS: push on full (overflow) -> OverflowError: Stack overflow: cannot push 99, the stack is full (capacity 3)
  PASS: stack unchanged after failed push

[LinkedStack]
  PASS: new stack is empty
  PASS: pop on empty (underflow) -> IndexError: Stack underflow: cannot pop from an empty stack
  PASS: peek on empty -> IndexError: Stack is empty: nothing to peek at
  LinkedStack (top -> bottom): [C, B, A] | size=3
  PASS: peek returns C (top)
  PASS: pop returns C
  PASS: peek then returns B
  PASS: pop returns B then A (LIFO)
  PASS: stack is empty again
  PASS: no overflow with 1000 pushes

[ArrayQueue (capacity 4)]
  PASS: new queue is empty
  PASS: dequeue on empty (underflow) -> IndexError: Queue underflow: cannot dequeue from an empty queue
  PASS: peek_front on empty -> IndexError: Queue is empty: nothing to peek at
  ArrayQueue (front -> rear): [A, B, C] | size=3/4 | front index=0 | raw array=[A, B, C, _]
  PASS: peek_front returns A
  PASS: dequeue order is A, B, C (FIFO)
  PASS: queue is empty again
  PASS: is_full when at capacity
  PASS: enqueue on full (overflow) -> OverflowError: Queue overflow: cannot enqueue 99, the queue is full (capacity 4)

[LinkedQueue]
  PASS: new queue is empty
  PASS: dequeue on empty (underflow) -> IndexError: Queue underflow: cannot dequeue from an empty queue
  PASS: peek_front on empty -> IndexError: Queue is empty: nothing to peek at
  LinkedQueue (front -> rear): [A, B, C] | size=3
  PASS: peek_front returns A
  PASS: dequeue order is A, B, C (FIFO)
  PASS: queue is empty again
  PASS: no overflow with 1000 enqueues

[ArrayQueue wrap-around demonstration, capacity 4]
  after enqueue A,B,C,D : ArrayQueue (front -> rear): [A, B, C, D] | size=4/4 | front index=0 | raw array=[A, B, C, D]
  PASS: dequeue A
  PASS: dequeue B
  after dequeue A,B     : ArrayQueue (front -> rear): [C, D] | size=2/4 | front index=2 | raw array=[_, _, C, D]
  after enqueue E,F     : ArrayQueue (front -> rear): [C, D, E, F] | size=4/4 | front index=2 | raw array=[E, F, C, D]
  PASS: E and F wrapped to indexes 0 and 1
  PASS: queue is full (size counter, not front==rear)
  PASS: FIFO order preserved across wrap: C, D, E, F
  PASS: queue empty after draining

[LinkedQueue rear reset when emptied]
  PASS: front is None after emptying
  PASS: rear is None after emptying
  PASS: enqueue after emptying works (2 then 3)

[Application exercises]
  PASS: is_balanced('()') is True
  PASS: is_balanced('([]{})') is True
  PASS: is_balanced('{[()]}') is True
  PASS: is_balanced('(]') is False
  PASS: is_balanced('((())') is False
  PASS: is_balanced('())') is False
  PASS: is_balanced('a(b[c]{d}e)f') is True
  PASS: is_balanced('') is True
  PASS: is_balanced('}{') is False
  PASS: print jobs served in FIFO order
  PASS: pages waited are 0, 5, 17

All tests passed.
```

## 2. Application exercises (`python applications.py`)
```text
=== Balanced parentheses checker (stack) ===
  '()'               -> balanced
  '([]{})'           -> balanced
  '{[()]}'           -> balanced
  '(]'               -> NOT balanced
  '((())'            -> NOT balanced
  '())'              -> NOT balanced
  'a(b[c]{d}e)f'     -> balanced
  ''                 -> balanced

=== Print queue simulation (FIFO) ===
Submitted (in order): J101 (5 pages), J102 (12 pages), J103 (3 pages), J104 (8 pages)
Order Job ID  Pages  Pages printed before it started
1     J101    5      0
2     J102    12     5
3     J103    3      17
4     J104    8      20
```

## 3. Menu program: ArrayStack with underflow and overflow (`python main.py`)
Inputs: implementation 1, capacity 3, pop on empty, push A/B/C/D, peek, pop, is_full, exit.
```text
=== Stacks and Queues: Array vs. Linked List ===

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 1
Enter capacity (positive integer): 3

Array Stack created.
State: ArrayStack (top -> bottom): [] | size=0/3 | top index=-1

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  ERROR: Stack underflow: cannot pop from an empty stack
State: ArrayStack (top -> bottom): [] | size=0/3 | top index=-1

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: A
  Push: 'A' done.
State: ArrayStack (top -> bottom): [A] | size=1/3 | top index=0

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: B
  Push: 'B' done.
State: ArrayStack (top -> bottom): [B, A] | size=2/3 | top index=1

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: C
  Push: 'C' done.
State: ArrayStack (top -> bottom): [C, B, A] | size=3/3 | top index=2

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: D
  ERROR: Stack overflow: cannot push 'D', the stack is full (capacity 3)
State: ArrayStack (top -> bottom): [C, B, A] | size=3/3 | top index=2

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 3
  Peek -> 'C'
State: ArrayStack (top -> bottom): [C, B, A] | size=3/3 | top index=2

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Pop -> 'C'
State: ArrayStack (top -> bottom): [B, A] | size=2/3 | top index=1

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 5
  Is full? -> False
State: ArrayStack (top -> bottom): [B, A] | size=2/3 | top index=1

--- Array Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 0

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 0
Goodbye!
```

## 4. Menu program: circular ArrayQueue with wrap-around, overflow and underflow
Inputs: implementation 3, capacity 3, enqueue A/B/C/D, dequeue twice, enqueue E/F (wraps around), dequeue until empty, then dequeue again.
```text
=== Stacks and Queues: Array vs. Linked List ===

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 3
Enter capacity (positive integer): 3

Array Queue (circular) created.
State: ArrayQueue (front -> rear): [] | size=0/3 | front index=0 | raw array=[_, _, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: A
  Enqueue: 'A' done.
State: ArrayQueue (front -> rear): [A] | size=1/3 | front index=0 | raw array=[A, _, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: B
  Enqueue: 'B' done.
State: ArrayQueue (front -> rear): [A, B] | size=2/3 | front index=0 | raw array=[A, B, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: C
  Enqueue: 'C' done.
State: ArrayQueue (front -> rear): [A, B, C] | size=3/3 | front index=0 | raw array=[A, B, C]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: D
  ERROR: Queue overflow: cannot enqueue 'D', the queue is full (capacity 3)
State: ArrayQueue (front -> rear): [A, B, C] | size=3/3 | front index=0 | raw array=[A, B, C]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'A'
State: ArrayQueue (front -> rear): [B, C] | size=2/3 | front index=1 | raw array=[_, B, C]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'B'
State: ArrayQueue (front -> rear): [C] | size=1/3 | front index=2 | raw array=[_, _, C]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: E
  Enqueue: 'E' done.
State: ArrayQueue (front -> rear): [C, E] | size=2/3 | front index=2 | raw array=[E, _, C]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: F
  Enqueue: 'F' done.
State: ArrayQueue (front -> rear): [C, E, F] | size=3/3 | front index=2 | raw array=[E, F, C]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'C'
State: ArrayQueue (front -> rear): [E, F] | size=2/3 | front index=0 | raw array=[E, F, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'E'
State: ArrayQueue (front -> rear): [F] | size=1/3 | front index=1 | raw array=[_, F, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'F'
State: ArrayQueue (front -> rear): [] | size=0/3 | front index=2 | raw array=[_, _, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  ERROR: Queue underflow: cannot dequeue from an empty queue
State: ArrayQueue (front -> rear): [] | size=0/3 | front index=2 | raw array=[_, _, _]

--- Array Queue (circular) operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 0

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 0
Goodbye!
```

## 5. Menu program: LinkedStack
```text
=== Stacks and Queues: Array vs. Linked List ===

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 2

Linked Stack created.
State: LinkedStack (top -> bottom): [] | size=0

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: X
  Push: 'X' done.
State: LinkedStack (top -> bottom): [X] | size=1

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: Y
  Push: 'Y' done.
State: LinkedStack (top -> bottom): [Y, X] | size=2

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 3
  Peek -> 'Y'
State: LinkedStack (top -> bottom): [Y, X] | size=2

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Pop -> 'Y'
State: LinkedStack (top -> bottom): [X] | size=1

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Pop -> 'X'
State: LinkedStack (top -> bottom): [] | size=0

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  ERROR: Stack underflow: cannot pop from an empty stack
State: LinkedStack (top -> bottom): [] | size=0

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 5
  Is full? -> False
State: LinkedStack (top -> bottom): [] | size=0

--- Linked Stack operations ---
  1. Push
  2. Pop
  3. Peek
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 0

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 0
Goodbye!
```

## 6. Menu program: LinkedQueue
```text
=== Stacks and Queues: Array vs. Linked List ===

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 4

Linked Queue created.
State: LinkedQueue (front -> rear): [] | size=0

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: X
  Enqueue: 'X' done.
State: LinkedQueue (front -> rear): [X] | size=1

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 1
  Enter value: Y
  Enqueue: 'Y' done.
State: LinkedQueue (front -> rear): [X, Y] | size=2

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 3
  Peek front -> 'X'
State: LinkedQueue (front -> rear): [X, Y] | size=2

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'X'
State: LinkedQueue (front -> rear): [Y] | size=1

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  Dequeue -> 'Y'
State: LinkedQueue (front -> rear): [] | size=0

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 2
  ERROR: Queue underflow: cannot dequeue from an empty queue
State: LinkedQueue (front -> rear): [] | size=0

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 4
  Is empty? -> True
State: LinkedQueue (front -> rear): [] | size=0

--- Linked Queue operations ---
  1. Enqueue
  2. Dequeue
  3. Peek front
  4. Is empty?
  5. Is full?
  0. Back to implementation menu
Choose an operation: 0

Choose an implementation:
  1. Array Stack
  2. Linked Stack
  3. Array Queue (circular)
  4. Linked Queue
  0. Exit
Your choice: 0
Goodbye!
```
