# Minimum Sum Subarray

## Problem

Given an integer array `arr[]`, find the **contiguous subarray** containing at least one element that has the **minimum sum**, and return that sum.

A subarray must contain **continuous elements**.

---

## Examples

### Example 1

**Input**

```text
arr = [3, -4, 2, -3, -1, 7, -5]
```

**Output**

```text
-6
```

**Explanation**

The minimum sum subarray is:

```text
[-4, 2, -3, -1]
```

Sum:

```text
-4 + 2 + (-3) + (-1) = -6
```

---

### Example 2

**Input**

```text
arr = [2, 6, 8, 1, 4]
```

**Output**

```text
1
```

**Explanation**

The minimum sum subarray is:

```text
[1]
```

Sum:

```text
1
```

---

# Approach (Modified Kadane's Algorithm)

This problem is the opposite of the **Maximum Subarray** problem.

Instead of finding the largest subarray sum, we find the **smallest**.

For every element, we have two choices:

1. Extend the previous subarray.
2. Start a new subarray from the current element.

Choose the option with the **smaller** sum.

Maintain two variables:

- `best_ans` → Minimum subarray sum ending at the current index.
- `ans` → Overall minimum subarray sum found so far.

---

# Code

```python
class Solution:
    def smallestSumSubarray(self, A, N):
        best_ans = A[0]
        ans = A[0]

        for i in range(1, len(A)):
            v1 = best_ans + A[i]
            v2 = A[i]

            best_ans = min(v1, v2)
            ans = min(best_ans, ans)

        return ans
```

---

# Explanation

Initialize both variables with the first element.

```python
best_ans = A[0]
ans = A[0]
```

Traverse the remaining elements.

```python
for i in range(1, len(A)):
```

Option 1: Extend the previous subarray.

```python
v1 = best_ans + A[i]
```

Option 2: Start a new subarray.

```python
v2 = A[i]
```

Choose the smaller sum.

```python
best_ans = min(v1, v2)
```

Update the overall minimum.

```python
ans = min(best_ans, ans)
```

Finally, return the answer.

```python
return ans
```

---

# Dry Run

### Example

```text
A = [3, -4, 2, -3, -1, 7, -5]
```

| Index | Current | Extend (`v1`) | New (`v2`) | best_ans | ans |
|------:|--------:|--------------:|-----------:|---------:|----:|
| 0 | 3 | - | - | 3 | 3 |
| 1 | -4 | -1 | -4 | -4 | -4 |
| 2 | 2 | -2 | 2 | -2 | -4 |
| 3 | -3 | -5 | -3 | -5 | -5 |
| 4 | -1 | -6 | -1 | -6 | -6 |
| 5 | 7 | 1 | 7 | 1 | -6 |
| 6 | -5 | -4 | -5 | -5 | -6 |

Final answer:

```text
-6
```

---

### Example

```text
A = [2, 6, 8, 1, 4]
```

| Index | best_ans | ans |
|------:|---------:|----:|
| 0 | 2 | 2 |
| 1 | 6 | 2 |
| 2 | 8 | 2 |
| 3 | 1 | 1 |
| 4 | 4 | 1 |

Return:

```text
1
```

---

# Time Complexity

```text
O(N)
```

The array is traversed exactly once.

---

# Space Complexity

```text
O(1)
```

Only a constant amount of extra space is used.

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
best_ans = ans = A[0]
```

### For Loop

```python
for i in range(1, len(A)):
```

### min() Function

```python
best_ans = min(v1, v2)
```

---

# Key Takeaways

- This is the **minimum** version of Kadane's Algorithm.
- At every index, decide whether to:
  - Extend the previous subarray.
  - Start a new subarray.
- `best_ans` stores the minimum subarray sum ending at the current index.
- `ans` stores the smallest subarray sum found so far.
- The algorithm runs in **O(N)** time using **O(1)** extra space.

---

## Author

**Ramit Sarker**
