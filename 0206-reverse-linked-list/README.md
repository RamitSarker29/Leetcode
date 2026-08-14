# 206. Reverse Linked List

## Problem

Given the `head` of a singly linked list, **reverse the list** and return the head of the reversed list.

---

## Examples

### Example 1

**Input**

```text
head = [1,2,3,4,5]
```

**Output**

```text
[5,4,3,2,1]
```

**Explanation:**

The original linked list:

```text
1 → 2 → 3 → 4 → 5 → None
```

After reversing:

```text
5 → 4 → 3 → 2 → 1 → None
```

![Reverse Linked List Example 1](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

---

### Example 2

**Input**

```text
head = [1,2]
```

**Output**

```text
[2,1]
```

**Explanation:**

Original:

```text
1 → 2 → None
```

Reversed:

```text
2 → 1 → None
```

![Reverse Linked List Example 2](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

---

### Example 3

**Input**

```text
head = []
```

**Output**

```text
[]
```

If the linked list is empty, there is nothing to reverse.

---

# Approach

We can reverse the linked list **iteratively** using three pointers:

```text
prev
current
dest
```

Initially:

```python
prev = None
current = head
```

The main idea is to reverse the `next` pointer of every node one by one.

For every node:

1. Save the next node in `dest`.
2. Reverse the current node's pointer.
3. Move `prev` to `current`.
4. Move `current` to `dest`.

---

# Why Do We Need `dest`?

This is the most important part of the algorithm.

Suppose we have:

```text
1 → 2 → 3 → None
```

and:

```python
current = 1
```

Before changing:

```python
current.next = prev
```

we first save:

```python
dest = current.next
```

So:

```text
dest = 2
```

Now we can safely reverse the pointer:

```python
current.next = prev
```

which changes:

```text
1 → 2
```

into:

```text
1 → None
```

Without storing `dest`, we would lose access to node `2`.

---

# The Three Pointers

### `current`

Points to the node we are currently processing.

### `prev`

Points to the already reversed part of the linked list.

Initially:

```text
prev = None
```

### `dest`

Temporarily stores the next node before we change `current.next`.

---

# Algorithm

For every node while `current` is not `None`:

```text
1. Save current.next
2. Reverse current.next
3. Move prev forward
4. Move current forward
```

In code:

```python
dest = current.next
current.next = prev
prev = current
current = dest
```

When the loop finishes:

```text
current = None
```

and `prev` points to the new head of the reversed linked list.

---

# Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current != None:
            dest = current.next
            current.next = prev
            prev = current
            current = dest

        return prev
```

---

# Dry Run

Consider:

```text
1 → 2 → 3 → None
```

Initially:

```text
current = 1
prev = None
```

---

### Step 1

Save the next node:

```python
dest = current.next
```

So:

```text
dest = 2
```

Reverse the pointer:

```python
current.next = prev
```

Now:

```text
1 → None
```

Move the pointers:

```python
prev = current
current = dest
```

Now:

```text
prev = 1
current = 2
```

The reversed part is:

```text
1 → None
```

---

### Step 2

Current node:

```text
current = 2
```

Save next:

```text
dest = 3
```

Reverse:

```text
2 → 1 → None
```

Move pointers:

```text
prev = 2
current = 3
```

Now:

```text
2 → 1 → None
```

---

### Step 3

Current node:

```text
current = 3
```

Save next:

```text
dest = None
```

Reverse:

```text
3 → 2 → 1 → None
```

Move pointers:

```text
prev = 3
current = None
```

---

### Loop Ends

Since:

```python
current == None
```

the loop stops.

Finally:

```python
return prev
```

`prev` points to:

```text
3 → 2 → 1 → None
```

Therefore:

```text
[3,2,1]
```

---

# Pointer Movement

A useful way to remember the process is:

```text
dest    = current.next
current.next = prev
prev    = current
current = dest
```

Think of it as:

```text
SAVE → REVERSE → MOVE → MOVE
```

Or:

```text
dest = current.next       # Save where we're going
current.next = prev       # Reverse the link
prev = current            # Move prev forward
current = dest            # Move current forward
```

---

# Visual Understanding

For:

```text
1 → 2 → 3 → None
```

Initially:

```text
prev
 ↓
None

current
   ↓
   1 → 2 → 3 → None
```

After processing `1`:

```text
None ← 1    2 → 3 → None
       ↑    ↑
      prev current
```

After processing `2`:

```text
None ← 1 ← 2    3 → None
             ↑    ↑
            prev current
```

After processing `3`:

```text
None ← 1 ← 2 ← 3
                 ↑
                prev
```

So the new linked list is:

```text
3 → 2 → 1 → None
```

---

# Why Does It Work?

At every iteration, the linked list is divided into two parts:

```text
Reversed Part       Unprocessed Part
     ↓                    ↓
prev                current
```

For example:

```text
None ← 1 ← 2    3 → 4 → 5 → None
             ↑
           current
```

The `prev` side is already reversed.

The `current` side has not been processed yet.

Each iteration moves one node from the unprocessed part to the reversed part.

When `current` becomes `None`, every node has been reversed, and `prev` is the new head.

---

# Edge Cases

### Empty List

```text
head = None
```

Initially:

```text
current = None
prev = None
```

The loop doesn't execute.

Return:

```text
None
```

---

### Single Node

```text
1 → None
```

The node's `next` already points to `None`.

After processing:

```text
1 → None
```

The same node is returned as the head.

---

# Complexity

Let:

```text
n = number of nodes
```

### Time Complexity

Every node is visited exactly once.

Therefore:

```text
O(n)
```

### Space Complexity

Only three pointers are used:

```text
current
prev
dest
```

No additional data structure is required.

Therefore:

```text
O(1)
```

---

# Key Takeaways

* Use three pointers: `current`, `prev`, and `dest`.
* `dest` saves the next node before changing the link.
* `current.next = prev` reverses the current pointer.
* `prev = current` moves the reversed portion forward.
* `current = dest` moves to the next unprocessed node.
* When `current` becomes `None`, `prev` is the new head.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`
* This is an **iterative** solution.
* The key pattern is:

```python
dest = current.next
current.next = prev
prev = current
current = dest
```

---

## Author

**Ramit Sarker**
