# 287. Find the Duplicate Number

## Problem

Given an integer array `nums` containing `n + 1` integers where every integer is in the range `[1, n]`, there is **exactly one duplicate number**.

Return the duplicate number.

### Constraints

- You **cannot modify** the input array.
- You must use **O(1)** extra space.

---

## Examples

### Example 1

**Input**

```text
nums = [1,3,4,2,2]
```

**Output**

```text
2
```

---

### Example 2

**Input**

```text
nums = [3,1,3,4,2]
```

**Output**

```text
3
```

---

### Example 3

**Input**

```text
nums = [3,3,3,3,3]
```

**Output**

```text
3
```

---

# Approach (Floyd's Cycle Detection Algorithm)

This problem can be converted into a linked list.

Think of every index as a node.

The value stored at each index points to the next index.

```text
next = nums[current]
```

Since there are `n + 1` numbers but only `n` possible values, at least one value must repeat.

A repeated value creates a cycle.

Therefore, finding the duplicate number is the same as finding the **starting node of the cycle**.

The algorithm works in two phases.

### Phase 1

Use a slow pointer and a fast pointer.

- Slow moves one step.
- Fast moves two steps.

If they meet, a cycle exists.

### Phase 2

Start another pointer from index `0`.

Move both pointers one step at a time.

The position where they meet is the duplicate number.

---

# Code

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                ptr = 0

                while ptr != slow:
                    slow = nums[slow]
                    ptr = nums[ptr]

                return ptr
```

---

# Explanation

Initialize both pointers.

```python
slow = fast = 0
```

Move the slow pointer one step.

```python
slow = nums[slow]
```

Move the fast pointer two steps.

```python
fast = nums[fast]
fast = nums[fast]
```

If both pointers meet, a cycle has been found.

```python
if slow == fast:
```

Create another pointer starting from index `0`.

```python
ptr = 0
```

Move both pointers one step at a time.

```python
while ptr != slow:
    ptr = nums[ptr]
    slow = nums[slow]
```

When they meet, return that value.

```python
return ptr
```

---

# Dry Run

### Example

```text
nums = [1,3,4,2,2]
```

Treat every index as a node.

```text
0 → 1
1 → 3
2 → 4
3 → 2
4 → 2
```

Graph:

```text
0 → 1 → 3 → 2 → 4
          ↑     │
          └─────┘
```

The cycle begins at **2**, so the duplicate number is **2**.

### Phase 1

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 0 | 0 |
| 1 | 1 | 3 |
| 2 | 3 | 4 |
| 3 | 2 | 4 |
| 4 | 4 | 4 ✅ |

The pointers meet inside the cycle.

---

### Phase 2

```text
ptr = 0
slow = 4
```

| Move | ptr | slow |
|------|-----|------|
| Start | 0 | 4 |
| 1 | 1 | 2 |
| 2 | 3 | 4 |
| 3 | 2 | 2 ✅ |

Both pointers meet at **2**.

Return:

```text
2
```

---

# Time Complexity

```text
O(n)
```

The array is traversed a constant number of times.

---

# Space Complexity

```text
O(1)
```

Only a few pointers are used.

---

# Concepts Used

- Floyd's Cycle Detection Algorithm
- Fast & Slow Pointer
- Two Pointers
- Array as Linked List
- Cycle Detection

---

# Python Features Used

### Multiple Variable Assignment

```python
slow = fast = 0
```

### Infinite Loop

```python
while True:
```

### Array Indexing

```python
slow = nums[slow]
fast = nums[nums[fast]]
```

---

# Key Takeaways

- Treat the array as a linked list where each value points to the next index.
- The duplicate number creates a cycle.
- Floyd's Cycle Detection Algorithm finds the cycle without modifying the array.
- After detecting the cycle, start one pointer from index `0` and move both pointers one step at a time.
- The point where they meet is the duplicate number.
- The solution satisfies the required **O(n)** time and **O(1)** extra space.

---

## Author

**Ramit Sarker**
