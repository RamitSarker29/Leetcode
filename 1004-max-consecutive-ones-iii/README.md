# 1004. Max Consecutive Ones III

## Problem

You are given a binary array `nums` and an integer `k`.

You may flip **at most `k` zeros** into `1`s.

Return the **maximum number of consecutive `1`s** that can be obtained after performing at most `k` flips.

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

**Output**

```text
6
```

**Explanation**

Flip the two highlighted zeros:

```text
1 1 1 0 0 0 1 1 1 1 0
          ↑       ↑
```

Result:

```text
1 1 1 0 0 1 1 1 1 1 1
```

Longest consecutive ones:

```text
6
```

---

### Example 2

**Input**

```text
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
```

**Output**

```text
10
```

---

# Intuition

We want the **longest** valid window.

A window is **valid** if:

```text
Number of zeros ≤ k
```

As we expand the window:

- Count the number of zeros.
- If zeros become greater than `k`, the window becomes invalid.
- Shrink the window from the left until it becomes valid again.

This is a classic **Variable Size Sliding Window** problem.

---

# Approach

Maintain two pointers:

- `left`
- `right`

Also maintain:

```text
zero_count
```

For every element:

1. Expand the window by moving `right`.
2. If the current element is `0`, increment `zero_count`.
3. While the window becomes invalid (`zero_count > k`):
   - Move `left`.
   - If a zero leaves the window, decrement `zero_count`.
4. Update the maximum window length.

---

# Algorithm

### Step 1

Initialize:

```python
left = 0
zero_count = 0
max_len = 0
```

---

### Step 2

Traverse the array.

```python
for right in range(len(nums)):
```

---

### Step 3

Expand the window.

```python
if nums[right] == 0:
    zero_count += 1
```

---

### Step 4

Shrink until the window becomes valid.

```python
while zero_count > k:
    if nums[left] == 0:
        zero_count -= 1
    left += 1
```

---

### Step 5

Update the answer.

```python
max_len = max(max_len, right-left+1)
```

---

# Code

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
```

---

# Dry Run

### Example

```text
nums = [1,1,0,1,0]
k = 1
```

| Window | Zeros | Valid? | Maximum Length |
|---------|------:|:------:|---------------:|
| `[1]` | 0 | ✅ | 1 |
| `[1,1]` | 0 | ✅ | 2 |
| `[1,1,0]` | 1 | ✅ | 3 |
| `[1,1,0,1]` | 1 | ✅ | 4 |
| `[1,1,0,1,0]` | 2 | ❌ | Shrink Window |

After shrinking:

```text
[0,1,0]
```

Zeros become:

```text
1
```

Window becomes valid again.

---

# Why Does This Work?

The window is allowed to contain at most `k` zeros.

Whenever:

```text
zero_count > k
```

the window is no longer valid.

So we continuously remove elements from the left until:

```text
zero_count ≤ k
```

Once the window becomes valid again, we update the maximum length.

---

# Variable Sliding Window Pattern

```python
for right in range(len(nums)):

    # Expand window

    while window_is_invalid:
        # Shrink window

    # Update answer
```

This same template is used in many interview problems.

---

# Time Complexity

```text
O(n)
```

Both pointers move only forward.

Each element:

- Enters the window once.
- Leaves the window once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Sliding Window
- Two Pointers
- Arrays

---

# Python Features Used

### Expand Window

```python
if nums[right] == 0:
    zero_count += 1
```

---

### Shrink Window

```python
while zero_count > k:
    if nums[left] == 0:
        zero_count -= 1
    left += 1
```

---

### Update Maximum

```python
max_len = max(max_len, right-left+1)
```

---

# Key Takeaways

- This is a **Variable Size Sliding Window** problem.
- A valid window contains **at most `k` zeros**.
- Expand the window by moving `right`.
- Shrink the window whenever it becomes invalid.
- Update the answer only after the window is valid.
- Both pointers move only forward, giving **O(n)** time complexity.

---

## Author

**Ramit Sarker**
