# 142. Linked List Cycle II

## Problem

Given the `head` of a singly linked list, return **the node where the cycle begins**. If there is **no cycle**, return `None`.

A cycle exists if a node can be reached again by continuously following the `next` pointer.

**Note:** Do **not** modify the linked list.

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
tail connects to node index 1
```

**Explanation**

The tail connects to the second node (value `2`), so the cycle starts there.

---

### Example 2

![Example 2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Input**

```text
head = [1,2], pos = 0
```

**Output**

```text
tail connects to node index 0
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
No cycle
```

---

# Approach (Floyd's Cycle Detection Algorithm)

This problem is solved in **two phases**.

## Phase 1: Detect whether a cycle exists

Use two pointers:

- **Slow Pointer** → Moves one step.
- **Fast Pointer** → Moves two steps.

If the two pointers meet, a cycle exists.

If `fast` reaches `None`, there is no cycle.

---

## Phase 2: Find the starting node of the cycle

Once `slow` and `fast` meet,

- Create another pointer `ptr` starting from `head`.
- Move both `ptr` and `slow` **one step at a time**.
- The node where they meet is the **starting node of the cycle**.

---

# Code

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr = head

                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None
```

---

# Explanation

Initialize both pointers.

```python
slow = fast = head
```

Move the pointers until they either meet or the fast pointer reaches the end.

```python
while fast != None and fast.next != None:
```

Move the slow pointer.

```python
slow = slow.next
```

Move the fast pointer.

```python
fast = fast.next.next
```

If both pointers meet, a cycle has been found.

```python
if slow == fast:
```

Create another pointer starting from the head.

```python
ptr = head
```

Move both pointers one step at a time.

```python
while ptr != slow:
    ptr = ptr.next
    slow = slow.next
```

When they meet, they are pointing to the **starting node of the cycle**.

```python
return ptr
```

If no cycle exists, return:

```python
return None
```

---

# Dry Run

### Example

```text
3 → 2 → 0 → -4
    ↑       ↓
    └───────┘
```

### Phase 1

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 3 | 3 |
| 1 | 2 | 0 |
| 2 | 0 | 2 |
| 3 | -4 | -4 ✅ |

The pointers meet at **-4**.

Notice that **-4 is NOT the start of the cycle**.

---

### Phase 2

Create another pointer.

```text
ptr = 3
slow = -4
```

Move both one step at a time.

| Move | ptr | slow |
|------|-----|------|
| Start | 3 | -4 |
| 1 | 2 | 2 ✅ |

They meet at node **2**, which is the beginning of the cycle.

Return:

```text
Node(2)
```

---

# Time Complexity

```text
O(n)
```

Each pointer traverses the linked list at most a constant number of times.

---

# Space Complexity

```text
O(1)
```

Only a few pointers are used.

---

# Concepts Used

- Linked List
- Two Pointers
- Fast & Slow Pointer Technique
- Floyd's Cycle Detection Algorithm
- Cycle Detection
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

- Floyd's algorithm works in **two phases**:
  1. Detect the cycle.
  2. Find the starting node.
- The first meeting point is **not necessarily** the start of the cycle.
- After the first meeting, move one pointer from `head` and the other from the meeting point.
- When both move one step at a time, they meet exactly at the beginning of the cycle.
- The solution achieves **O(n)** time and **O(1)** extra space.

---

## Author

**Ramit Sarker**
