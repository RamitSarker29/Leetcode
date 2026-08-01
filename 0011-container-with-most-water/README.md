# 11. Container With Most Water

## Problem

You are given an integer array `height` where each element represents the height of a vertical line.

Choose **two lines** such that, together with the x-axis, they form a container capable of holding the **maximum amount of water**.

Return the maximum area of water that can be stored.

> **Note:** The container cannot be slanted.

---

## Examples

### Example 1

![Container With Most Water](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

**Input**

```text
height = [1,8,6,2,5,4,8,3,7]
```

**Output**

```text
49
```

**Explanation**

Choose the lines with heights:

```text
8 and 7
```

Width:

```text
8 - 1 = 7
```

Height:

```text
min(8,7) = 7
```

Area:

```text
7 × 7 = 49
```

---

### Example 2

**Input**

```text
height = [1,1]
```

**Output**

```text
1
```

---

# Intuition

The area of water between two lines depends on:

- The **distance** between the lines (width).
- The **shorter** of the two lines (height).

```text
Area = Width × Height
```

where

```text
Width = right - left
Height = min(height[left], height[right])
```

A brute-force solution checks every pair of lines, resulting in **O(n²)** time.

Instead, use the **Two Pointer** technique.

---

# Approach

1. Place one pointer at the beginning.
2. Place the other pointer at the end.
3. Calculate the current area.
4. Update the maximum area.
5. Move the pointer pointing to the **shorter line**.
6. Continue until the pointers meet.

---

# Why Move the Shorter Pointer?

Suppose:

```text
Left Height = 4
Right Height = 9
```

Current area:

```text
Width × min(4,9)
= Width × 4
```

If we move the **right pointer**:

- Width decreases.
- The minimum height is still limited by **4**.

So the area cannot increase.

However, if we move the **left pointer**, we may find a taller line:

```text
Left Height = 8
Right Height = 9
```

Now:

```text
Width × min(8,9)
```

Although the width decreased, the limiting height increased, giving us a chance to obtain a larger area.

**Therefore, always move the shorter pointer.**

---

# Algorithm

1. Initialize two pointers.

```python
left = 0
right = len(height) - 1
```

2. While `left < right`:

- Calculate the width.
- Calculate the limiting height.
- Update the maximum area.
- Move the pointer with the smaller height.

3. Return the maximum area.

---

# Code

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0

        while i < j:
            width = j - i
            length = min(height[i], height[j])

            area = max(area, width * length)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area
```

---

# Dry Run

### Example

```text
height = [1,8,6,2,5,4,8,3,7]
```

| Left | Right | Heights | Width | Height | Area | Max Area | Move |
|-----:|------:|---------|------:|-------:|-----:|---------:|------|
| 0 | 8 | 1,7 | 8 | 1 | 8 | 8 | Left |
| 1 | 8 | 8,7 | 7 | 7 | 49 | 49 | Right |
| 1 | 7 | 8,3 | 6 | 3 | 18 | 49 | Right |
| 1 | 6 | 8,8 | 5 | 8 | 40 | 49 | Right |
| 1 | 5 | 8,4 | 4 | 4 | 16 | 49 | Right |
| 1 | 4 | 8,5 | 3 | 5 | 15 | 49 | Right |
| 1 | 3 | 8,2 | 2 | 2 | 4 | 49 | Right |
| 1 | 2 | 8,6 | 1 | 6 | 6 | 49 | Right |

Final Answer:

```text
49
```

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

Only constant extra space is used.

---

# Concepts Used

- Two Pointers
- Greedy
- Arrays

---

# Python Features Used

### Finding Minimum Height

```python
min(height[i], height[j])
```

### Finding Maximum Area

```python
area = max(area, width * length)
```

### Two Pointer Traversal

```python
while i < j:
```

---

# Key Takeaways

- The width is the distance between the two indices.
- The water level is limited by the **shorter** line.
- Always move the pointer with the smaller height.
- Moving the taller pointer cannot increase the area because the shorter line still limits the water.
- Runs in **O(n)** time with **O(1)** extra space.

---

## Author

**Ramit Sarker**
