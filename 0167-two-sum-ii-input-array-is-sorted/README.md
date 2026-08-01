# 167. Two Sum II - Input Array Is Sorted

## Problem

Given a **1-indexed** sorted array `numbers` and an integer `target`, find two numbers such that they add up to the target.

Return their **1-based indices**.

- The array is sorted in **non-decreasing order**.
- Exactly **one solution** exists.
- You cannot use the same element twice.
- Use only **constant extra space**.

---

## Examples

### Example 1

**Input**

```text
numbers = [2,7,11,15]
target = 9
```

**Output**

```text
[1,2]
```

**Explanation**

```text
2 + 7 = 9
```

---

### Example 2

**Input**

```text
numbers = [2,3,4]
target = 6
```

**Output**

```text
[1,3]
```

---

### Example 3

**Input**

```text
numbers = [-1,0]
target = -1
```

**Output**

```text
[1,2]
```

---

# Intuition

Since the array is **already sorted**, we don't need a HashMap.

Use two pointers.

- Left pointer starts at the beginning.
- Right pointer starts at the end.

Compare their sum with the target.

---

# Approach

### Case 1

If

```text
current_sum > target
```

Move the **right pointer** left.

Since the array is sorted, moving left decreases the sum.

---

### Case 2

If

```text
current_sum < target
```

Move the **left pointer** right.

Moving right increases the sum.

---

### Case 3

If

```text
current_sum == target
```

Return the two indices.

---

# Algorithm

1. Initialize two pointers.

```python
i = 0
j = len(numbers) - 1
```

2. While the pointers haven't crossed:

- Compute the current sum.
- Compare it with the target.
- Move one pointer accordingly.

3. Return the indices when the target is found.

---

# Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]

            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            else:
                return i + 1, j + 1
```

---

# Dry Run

### Example

```text
numbers = [2,7,11,15]
target = 9
```

| Left | Right | Values | Sum | Action |
|-----:|------:|--------|----:|--------|
| 0 | 3 | 2,15 | 17 | Move right |
| 0 | 2 | 2,11 | 13 | Move right |
| 0 | 1 | 2,7 | 9 | Return `[1,2]` |

---

### Example

```text
numbers = [2,3,4]
target = 6
```

| Left | Right | Values | Sum | Action |
|-----:|------:|--------|----:|--------|
| 0 | 2 | 2,4 | 6 | Return `[1,3]` |

---

# Why Does This Work?

The array is sorted.

If

```text
numbers[left] + numbers[right] > target
```

then increasing the left pointer would only make the sum **larger**.

So the only way to reduce the sum is:

```text
Move the right pointer left.
```

Similarly,

If

```text
numbers[left] + numbers[right] < target
```

the only way to increase the sum is:

```text
Move the left pointer right.
```

This guarantees we never miss the correct pair.

---

# Time Complexity

```text
O(n)
```

Each pointer moves at most `n` times.

---

# Space Complexity

```text
O(1)
```

Only two pointers are used.

---

# Concepts Used

- Two Pointers
- Sorted Array
- Greedy

---

# Python Features Used

### While Loop

```python
while i < j:
```

### Conditional Statements

```python
if
elif
else
```

### Returning a List

```python
return i + 1, j + 1
```

---

# Key Takeaways

- Use two pointers because the array is already sorted.
- If the sum is too large, move the right pointer.
- If the sum is too small, move the left pointer.
- Runs in **O(n)** time with **O(1)** extra space.
- No HashMap is required.

---

## Author

**Ramit Sarker**
