# 876. Middle of the Linked List

## Problem

Given the `head` of a singly linked list, return **the middle node** of the linked list.

- If the linked list has **one middle node**, return that node.
- If the linked list has **two middle nodes**, return the **second middle** node.

---

## Examples

### Example 1

![Example 1](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)

**Input**

```text
head = [1,2,3,4,5]
```

**Output**

```text
[3,4,5]
```

**Explanation**

The linked list contains **5 nodes**, so there is only one middle node.

The middle node is **3**, and returning this node means the remaining linked list is:

```text
3 → 4 → 5
```

---

### Example 2

![Example 2](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)

**Input**

```text
head = [1,2,3,4,5,6]
```

**Output**

```text
[4,5,6]
```

**Explanation**

The linked list contains **6 nodes**, so there are two middle nodes (**3** and **4**).

According to the problem statement, we return the **second middle node**, which is **4**.

---

# Approach (Fast & Slow Pointer)

Use two pointers:

- **Slow Pointer** → Moves one node at a time.
- **Fast Pointer** → Moves two nodes at a time.

### Observation

- Every time the fast pointer moves **2 nodes**, the slow pointer moves **1 node**.
- When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle.
- For an even-length linked list, this naturally lands on the **second middle node**, which is exactly what the problem asks for.

---

# Code

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
```

---

# Explanation

Initialize both pointers at the head.

```python
slow, fast = head, head
```

Continue while the fast pointer can safely move two steps.

```python
while fast != None and fast.next != None:
```

Move the slow pointer one step.

```python
slow = slow.next
```

Move the fast pointer two steps.

```python
fast = fast.next.next
```

When the loop ends, the slow pointer is pointing to the middle node.

```python
return slow
```

---

# Dry Run

### Example 1

```text
1 → 2 → 3 → 4 → 5
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

`fast.next` is `None`, so the loop stops.

Return:

```text
3 → 4 → 5
```

---

### Example 2

```text
1 → 2 → 3 → 4 → 5 → 6
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |
| 3 | 4 | None |

The fast pointer becomes `None`, so the loop stops.

Return:

```text
4 → 5 → 6
```

Notice that for an even-length list, the algorithm automatically returns the **second middle node**.

---

# Time Complexity

```text
O(n)
```

The linked list is traversed only once.

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
- Pointer Traversal

---

# Python Features Used

### Multiple Variable Assignment

```python
slow, fast = head, head
```

### While Loop

```python
while fast != None and fast.next != None:
```

### Pointer Traversal

```python
slow = slow.next
fast = fast.next.next
```

---

# Key Takeaways

- Use one slow pointer and one fast pointer.
- The slow pointer moves **one node**, while the fast pointer moves **two nodes**.
- When the fast pointer reaches the end, the slow pointer is at the middle.
- This approach naturally returns the **second middle node** for even-length linked lists.
- The solution runs in **O(n)** time using **O(1)** extra space.

---

## Author

**Ramit Sarker**
