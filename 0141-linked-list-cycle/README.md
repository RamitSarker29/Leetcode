# 141. Linked List Cycle

## Problem

Given the `head` of a singly linked list, determine whether the linked list contains a cycle.

A cycle exists if a node can be reached again by continuously following the `next` pointer.

Return:

- `True` if a cycle exists.
- `False` otherwise.

> **Follow-up:** Solve the problem using **O(1)** extra memory.

---

## Examples

### Example 1

![Example 1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Input**

```text
head = [3,2,0,-4], pos = 1
```

**Output**

```text
True
```

**Explanation**

The tail connects back to the node with value `2`, creating a cycle.

---

### Example 2

![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Input**

```text
head = [1,2], pos = 0
```

**Output**

```text
True
```

**Explanation**

The tail connects back to the first node.

---

### Example 3

![Example 3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Input**

```text
head = [1], pos = -1
```

**Output**

```text
False
```

**Explanation**

There is no cycle in the linked list.

---

# Approach (Floyd's Cycle Detection Algorithm)

Use two pointers:

- **Slow Pointer** → Moves one step at a time.
- **Fast Pointer** → Moves two steps at a time.

### Observation

- If the linked list **does not contain a cycle**, the fast pointer will eventually reach `None`.
- If the linked list **contains a cycle**, the fast pointer will eventually catch up with the slow pointer.

Therefore,

- If both pointers meet → return `True`.
- If the loop finishes → return `False`.

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

If both pointers point to the same node, a cycle exists.

```python
if slow == fast:
    return True
```

If the fast pointer reaches the end of the linked list, there is no cycle.

```python
return False
```

---

# Dry Run

### Example (Cycle Exists)

```text
3 → 2 → 0 → -4
    ↑       ↓
    └───────┘
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 3 | 3 |
| 1 | 2 | 0 |
| 2 | 0 | 2 |
| 3 | -4 | -4 ✅ |

The two pointers meet, so a cycle exists.

Return:

```text
True
```

---

### Example (No Cycle)

```text
1 → 2 → 3 → 4 → None
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | None |

The fast pointer reaches `None`, so the linked list does not contain a cycle.

Return:

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
- Fast & Slow Pointer Technique
- Floyd's Cycle Detection Algorithm
- Pointer Traversal

---

# Python Features Used

### Multiple Variable Assignment

```python
slow = fast = head
```

### While Loop

```python
while fast != None and fast.next != None:
```

### Pointer Manipulation

```python
slow = slow.next
fast = fast.next.next
```

### Object Comparison

```python
if slow == fast:
```

---

# Key Takeaways

- Use two pointers moving at different speeds.
- If there is a cycle, the fast pointer will eventually meet the slow pointer.
- If the fast pointer reaches `None`, the linked list has no cycle.
- Before accessing `fast.next.next`, always ensure both `fast` and `fast.next` exist.
- Floyd's Cycle Detection Algorithm solves the problem in **O(n)** time using **O(1)** extra space.

---

## Author

**Ramit Sarker**
