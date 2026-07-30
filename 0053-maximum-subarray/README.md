# 53. Maximum Subarray

## Problem

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) that has the **largest sum**, and return its sum.

A subarray must consist of **continuous elements**.

---

## Examples

### Example 1

**Input**

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

**Output**

```text
6
```

**Explanation**

The maximum sum subarray is:

```text
[4, -1, 2, 1]
```

Sum:

```text
4 + (-1) + 2 + 1 = 6
```

---

### Example 2

**Input**

```text
nums = [1]
```

**Output**

```text
1
```

**Explanation**

The only subarray is:

```text
[1]
```

Maximum sum:

```text
1
```

---

### Example 3

**Input**

```text
nums = [5,4,-1,7,8]
```

**Output**

```text
23
```

**Explanation**

The entire array forms the maximum subarray.

```text
5 + 4 + (-1) + 7 + 8 = 23
```

---

# Approach (Kadane's Algorithm)

This problem can be solved in **O(n)** using **Kadane's Algorithm**.

For every element, we have two choices:

1. Extend the previous subarray.
2. Start a new subarray from the current element.

Choose whichever gives the larger sum.

Maintain:

- `best_ans` → Maximum subarray sum ending at the current index.
- `ans` → Overall maximum subarray sum found so far.

---

# Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        best_ans = nums[0]

        for i in range(1, len(nums)):
            v1 = best_ans + nums[i]
            v2 = nums[i]

            best_ans = max(v1, v2)
            ans = max(best_ans, ans)

        return ans
```

---

# Explanation

Initialize both variables with the first element.

```python
ans = nums[0]
best_ans = nums[0]
```

Traverse the remaining elements.

```python
for i in range(1, len(nums)):
```

Option 1: Extend the previous subarray.

```python
v1 = best_ans + nums[i]
```

Option 2: Start a new subarray.

```python
v2 = nums[i]
```

Choose the better option.

```python
best_ans = max(v1, v2)
```

Update the global maximum.

```python
ans = max(best_ans, ans)
```

Finally,

```python
return ans
```

---

# Dry Run

### Example

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

| Index | Current | Extend (`v1`) | New (`v2`) | best_ans | ans |
|------:|--------:|--------------:|-----------:|---------:|----:|
| 0 | -2 | - | - | -2 | -2 |
| 1 | 1 | -1 | 1 | 1 | 1 |
| 2 | -3 | -2 | -3 | -2 | 1 |
| 3 | 4 | 2 | 4 | 4 | 4 |
| 4 | -1 | 3 | -1 | 3 | 4 |
| 5 | 2 | 5 | 2 | 5 | 5 |
| 6 | 1 | 6 | 1 | 6 | 6 |
| 7 | -5 | 1 | -5 | 1 | 6 |
| 8 | 4 | 5 | 4 | 5 | 6 |

Final answer:

```text
6
```

---

### Example

```text
nums = [5,4,-1,7,8]
```

| Index | best_ans | ans |
|------:|---------:|----:|
| 0 | 5 | 5 |
| 1 | 9 | 9 |
| 2 | 8 | 9 |
| 3 | 15 | 15 |
| 4 | 23 | 23 |

Return:

```text
23
```

---

# Time Complexity

```text
O(n)
```

The array is traversed once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Kadane's Algorithm
- Dynamic Programming
- Greedy
- Arrays

---

# Python Features Used

### Multiple Assignment

```python
ans = best_ans = nums[0]
```

### For Loop

```python
for i in range(1, len(nums)):
```

### max() Function

```python
best_ans = max(v1, v2)
```

---

# Key Takeaways

- At every index, decide whether to **continue the current subarray** or **start a new one**.
- `best_ans` stores the best subarray ending at the current index.
- `ans` stores the overall maximum found so far.
- Kadane's Algorithm solves the problem in **O(n)** time and **O(1)** extra space.

---

## Author

**Ramit Sarker**
