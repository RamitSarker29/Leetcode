# 209. Minimum Size Subarray Sum

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return the **minimum length** of a contiguous subarray whose sum is **greater than or equal to** `target`.

If there is no such subarray, return `0`.

### Example 1

**Input**

```text
target = 7
nums = [2,3,1,2,4,3]
```

**Output**

```text
2
```

### Example 2

**Input**

```text
target = 4
nums = [1,4,4]
```

**Output**

```text
1
```

### Example 3

**Input**

```text
target = 11
nums = [1,1,1,1,1,1,1,1]
```

**Output**

```text
0
```

---

# Intuition

Since every element in the array is **positive**, increasing the window always increases the sum, while shrinking the window always decreases it.

We use a **Sliding Window** with two pointers:

- Expand the window until its sum becomes at least `target`.
- Once it becomes valid, shrink it as much as possible while maintaining the condition.
- Keep track of the smallest valid window found.

---

# Approach

1. Initialize:
   - `i = 0` (left pointer)
   - `window_sum = 0`
   - `min_len = ∞`

2. Traverse the array using `j` as the right pointer.

3. Add `nums[j]` to the current window.

4. While the window sum is greater than or equal to `target`:
   - Update the minimum length.
   - Remove the leftmost element from the window.
   - Move the left pointer forward.

5. If no valid window exists, return `0`; otherwise return `min_len`.

---

# Code

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        min_len = float('inf')
        window_sum = 0

        for j in range(len(nums)):
            window_sum += nums[j]

            while window_sum >= target:
                min_len = min(min_len, j - i + 1)
                window_sum -= nums[i]
                i += 1

        return 0 if min_len == float('inf') else min_len
```

---

# Explanation

Consider:

```text
target = 7
nums = [2,3,1,2,4,3]
```

### Step 1

Expand the window.

```text
[2]
Sum = 2
```

Not enough.

---

### Step 2

Expand.

```text
[2,3]
Sum = 5
```

Still less than `7`.

---

### Step 3

Expand.

```text
[2,3,1]
Sum = 6
```

Still less than `7`.

---

### Step 4

Expand.

```text
[2,3,1,2]
Sum = 8
```

Now the window satisfies the condition.

Length = `4`

Update answer.

Now shrink the window.

```text
[3,1,2]
Sum = 6
```

Stop shrinking.

---

### Step 5

Expand.

```text
[3,1,2,4]
Sum = 10
```

Valid window.

Length = `4`

Shrink.

```text
[1,2,4]
Sum = 7
Length = 3
```

Update answer.

Shrink again.

```text
[2,4]
Sum = 6
```

Stop.

---

### Step 6

Expand.

```text
[2,4,3]
Sum = 9
```

Valid.

Length = `3`

Shrink.

```text
[4,3]
Sum = 7
Length = 2
```

Update answer.

Shrink again.

```text
[3]
Sum = 3
```

Stop.

Final answer:

```text
2
```

---

# Dry Run

| Left (`i`) | Right (`j`) | Window | Sum | Minimum Length |
|------------|-------------|--------|-----|----------------|
| 0 | 0 | [2] | 2 | ∞ |
| 0 | 1 | [2,3] | 5 | ∞ |
| 0 | 2 | [2,3,1] | 6 | ∞ |
| 0 | 3 | [2,3,1,2] | 8 | 4 |
| 1 | 3 | [3,1,2] | 6 | 4 |
| 1 | 4 | [3,1,2,4] | 10 | 4 |
| 2 | 4 | [1,2,4] | 7 | 3 |
| 3 | 4 | [2,4] | 6 | 3 |
| 3 | 5 | [2,4,3] | 9 | 3 |
| 4 | 5 | [4,3] | 7 | **2** |
| 5 | 5 | [3] | 3 | **2** |

---

# Time Complexity

- Each element is added to the window once.
- Each element is removed from the window once.

**Time Complexity:** `O(n)`

---

# Space Complexity

Only a few variables are used.

**Space Complexity:** `O(1)`

---

# Concepts Used

- Sliding Window
- Two Pointers
- Greedy
- Array Traversal

---

# Python Features Used

- `for` loop
- `while` loop
- `min()`
- `float('inf')`
- Ternary operator
- List Indexing

---

# Key Takeaways

- Sliding Window works because all elements are **positive**.
- Expand the window until it becomes valid.
- Shrink it as much as possible to get the minimum length.
- Even with a nested `while` loop, the solution is **O(n)** because each pointer only moves forward.

---

# Author

**Ramit Sarker**
