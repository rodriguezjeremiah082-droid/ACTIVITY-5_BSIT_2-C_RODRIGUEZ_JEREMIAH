"""applications.py - Application exercises.

a) Balanced-parentheses checker using a stack.
b) Print-queue simulation using a queue (FIFO).

Run:  python applications.py
"""

from array_stack import ArrayStack
from linked_queue import LinkedQueue

PAIRS = {")": "(", "]": "[", "}": "{"}
OPENERS = set(PAIRS.values())


def is_balanced(text):
    """Return True if every (), [], {} in `text` is properly opened, closed and
    nested. Characters other than brackets are ignored."""
    stack = ArrayStack(max(len(text), 1))   # can never overflow
    for ch in text:
        if ch in OPENERS:
            stack.push(ch)
        elif ch in PAIRS:
            if stack.is_empty():            # closer with nothing to match
                return False
            if stack.pop() != PAIRS[ch]:    # wrong type of opener
                return False
    return stack.is_empty()                 # leftover openers -> unbalanced


def simulate_print_queue(jobs):
    """`jobs` is a list of (job_id, pages) in submission order. Jobs are enqueued,
    then dequeued and 'printed' in FIFO order. Returns a list of dicts with the
    print position and how many pages were printed before each job started."""
    queue = LinkedQueue()
    for job_id, pages in jobs:
        queue.enqueue((job_id, pages))
    report = []
    pages_before = 0
    position = 0
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        position += 1
        report.append({"position": position, "job_id": job_id, "pages": pages,
                       "pages_waited": pages_before})
        pages_before += pages
    return report


def demo_parentheses():
    print("=== Balanced parentheses checker (stack) ===")
    samples = ["()", "([]{})", "{[()]}", "(]", "((())", "())", "a(b[c]{d}e)f", ""]
    for s in samples:
        verdict = "balanced" if is_balanced(s) else "NOT balanced"
        print(f"  {s!r:18} -> {verdict}")


def demo_print_queue():
    print("\n=== Print queue simulation (FIFO) ===")
    jobs = [("J101", 5), ("J102", 12), ("J103", 3), ("J104", 8)]
    print("Submitted (in order): " + ", ".join(f"{j} ({p} pages)" for j, p in jobs))
    print(f"{'Order':<6}{'Job ID':<8}{'Pages':<7}Pages printed before it started")
    for r in simulate_print_queue(jobs):
        print(f"{r['position']:<6}{r['job_id']:<8}{r['pages']:<7}{r['pages_waited']}")


if __name__ == "__main__":
    demo_parentheses()
    demo_print_queue()
