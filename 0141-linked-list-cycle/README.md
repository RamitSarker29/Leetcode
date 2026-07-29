# 141. Linked List Cycle

## Problem

Given the `head` of a singly linked list, determine whether the linked list contains a cycle.

A cycle exists if a node can be reached again by continuously following the `next` pointer.

Return:

- `True` if a cycle exists.
- `False` otherwise.

---

## Examples

### Example 1

**Input**

```text
head = [3,2,0,-4], pos = 1
```

**Output**

```text
True
```

**Explanation**

```text
3 → 2 → 0 → -4
    ↑         ↓
    └─────────┘
```

The last node points back to the node with value `2`.

---

### Example 2

**Input**

```text
head = [1,2], pos = 0
```

**Output**

```text
True
```

**Explanation**

```text
1 → 2
↑   ↓
└───┘
```

---

### Example 3

**Input**

```text
head = [1], pos = -1
```

**Output**

```text
False
```

**Explanation**

```text
1 → None
```

There is no cycle.

---

# Approach (Floyd's Cycle Detection Algorithm)

Use two pointers:

- **Slow Pointer** → Moves **one** step at a time.
- **Fast Pointer** → Moves **two** steps at a time.

### Observation

- If there is **no cycle**, the fast pointer will eventually reach the end of the linked list (`None`).
- If there **is a cycle**, the fast pointer will eventually catch up to the slow pointer.

Therefore,

- If `slow == fast`, return `True`.
- If the loop ends, return `False`.

---

# Code

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

---

# Explanation

Initialize both pointers at the head of the linked list.

```python
slow = fast = head
```

Continue traversing while the fast pointer can safely move two steps.

```python
while fast != None and fast.next != None:
```

Move the slow pointer by one node.

```python
slow = slow.next
```

Move the fast pointer by two nodes.

```python
fast = fast.next.next
```

If both pointers meet, a cycle exists.

```python
if slow == fast:
    return True
```

If the loop finishes, the fast pointer has reached the end of the list, meaning there is no cycle.

```python
return False
```

---

# Dry Run

### Example 1 (Cycle Exists)

```text
1 → 2 → 3 → 4 → 5
      ↑         ↓
      └─────────┘
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |
| 3 | 4 | 4 ✅ |

Since both pointers meet, return:

```text
True
```

---

### Example 2 (No Cycle)

```text
1 → 2 → 3 → 4 → None
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | None |

The fast pointer reaches `None`, so return:

```text
False
```

---

# Time Complexity

```text
O(n)
```

Each node is visited at most a constant number of times.

---

# Space Complexity

```text
O(1)
```

Only two pointers are used.

---

# Concepts Used

- Linked List
- Two Pointers
- Fast and Slow Pointer
- Floyd's Cycle Detection Algorithm
- Pointer Traversal

---

# Python Features Used

- Multiple Variable Assignment

```python
slow = fast = head
```

- `while` loop
- Pointer Manipulation
- Object Comparison

---

# Key Takeaways

- Use two pointers moving at different speeds.
- If a cycle exists, the fast pointer eventually catches the slow pointer.
- If the fast pointer reaches `None`, the linked list has no cycle.
- Before accessing `fast.next.next`, always ensure `fast` and `fast.next` are not `None`.
- Floyd's Cycle Detection solves the problem in **O(n)** time and **O(1)** extra space.

---

## Author

**Ramit Sarker**
