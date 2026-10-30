# Analysis

**Why does the linked-list stack push at the head instead of the tail?**
A singly linked list only has `next` references, so there is no way to step backward. If the stack's top were the tail, `pop` would have to walk from the head through all n nodes to find the second-to-last node before it could remove the last one, making `pop` O(n). Pushing and popping at the head only needs to change one reference (`top`), so both operations stay O(1) no matter how many elements the stack holds.

**Why must the array queue be circular?**
In a plain array queue, every `dequeue` moves the front forward and leaves an unusable empty slot behind it, so the queue reports "full" even when most of the array is empty. The only non-circular fix is to shift all elements left after each `dequeue`, which makes it O(n). Using the modulo operator to wrap the front and rear indices back to 0 lets freed slots at the beginning be reused, so both `enqueue` and `dequeue` stay O(1) and the full capacity of the array is always usable.
