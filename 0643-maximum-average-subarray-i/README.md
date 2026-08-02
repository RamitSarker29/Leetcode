# 643. Maximum Average Subarray I

## Problem

Given an integer array `nums` consisting of `n` elements and an integer `k`, find the contiguous subarray of **length exactly `k`** that has the maximum average value.

Return the maximum average.

---

## Examples

### Example 1

**Input**

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

**Output**

```text
12.75
```

**Explanation**

Possible windows of length `4`:

```text
[1,12,-5,-6]  → Sum = 2
[12,-5,-6,50] → Sum = 51
[-5,-6,50,3]  → Sum = 42
```

Maximum window sum:

```text
51
```

Maximum average:

```text
51 / 4 = 12.75
```

---

### Example 2

**Input**

```text
nums = [5]
k = 1
```

**Output**

```text
5.0
```

---

# Intuition

Since the window size is **fixed** (`k`), we don't need to recalculate the sum of every window.

Instead:

- Compute the sum of the **first window**.
- Move the window one position to the right.
- Remove the element leaving the window.
- Add the new element entering the window.

This updates the window sum in **O(1)** time.

---

# Approach

1. Calculate the sum of the first `k` elements.
2. Store it as the current maximum.
3. Slide the window one element at a time.
4. For every slide:
   - Add the new element.
   - Remove the old element.
   - Update the maximum window sum.
5. Return:

```text
Maximum Average = Maximum Window Sum / k
```

---

# Algorithm

1. Compute the first window sum.

```python
window_sum = sum(nums[:k])
```

2. Store it as the maximum.

```python
max_sum = window_sum
```

3. Slide the window.

```python
window_sum += nums[i]
window_sum -= nums[i-k]
```

4. Update the maximum sum.

```python
max_sum = max(max_sum, window_sum)
```

5. Return:

```python
max_sum / k
```

---

# Code

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
```

---

# Dry Run

### Example

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

### First Window

```text
[1,12,-5,-6]
```

```text
window_sum = 2
max_sum = 2
```

---

### Slide 1

Remove:

```text
1
```

Add:

```text
50
```

New window:

```text
[12,-5,-6,50]
```

```text
window_sum = 2 - 1 + 50 = 51
max_sum = 51
```

---

### Slide 2

Remove:

```text
12
```

Add:

```text
3
```

New window:

```text
[-5,-6,50,3]
```

```text
window_sum = 51 - 12 + 3 = 42
max_sum = 51
```

---

Final Answer

```text
51 / 4 = 12.75
```

---

# Why Does This Work?

Every time the window moves:

```text
Old Window

[a, b, c, d]

↓

New Window

[b, c, d, e]
```

Instead of computing:

```text
b + c + d + e
```

again, we simply do:

```text
Old Sum
- Element Leaving
+ Element Entering
```

This makes every slide **O(1)**.

---

# Time Complexity

```text
O(n)
```

- First window: `O(k)`
- Sliding the window: `O(n-k)`

Overall:

```text
O(n)
```

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Sliding Window
- Arrays

---

# Python Features Used

### First Window Sum

```python
window_sum = sum(nums[:k])
```

---

### Slide the Window

```python
window_sum += nums[i]
window_sum -= nums[i-k]
```

or

```python
window_sum += nums[i] - nums[i-k]
```

---

### Update Maximum

```python
max_sum = max(max_sum, window_sum)
```

---

# Key Takeaways

- This is a **Fixed Size Sliding Window** problem.
- The window size **never changes**.
- Build the first window once.
- Every slide:
  - Remove one element.
  - Add one element.
- No `while` loop is needed because the window size is always exactly `k`.
- Runs in **O(n)** time with **O(1)** extra space.

---

## Author

**Ramit Sarker**
