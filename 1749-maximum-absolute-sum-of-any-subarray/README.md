# 1749. Maximum Absolute Sum of Any Subarray

## Problem

Given an integer array `nums`, return the **maximum absolute sum** of any (possibly empty) subarray.

The absolute sum of a subarray is:

```text
abs(sum of all elements in the subarray)
```

The absolute value is defined as:

- If `x >= 0`, then `abs(x) = x`
- If `x < 0`, then `abs(x) = -x`

---

## Examples

### Example 1

**Input**

```text
nums = [1, -3, 2, 3, -4]
```

**Output**

```text
5
```

**Explanation**

The maximum absolute sum comes from:

```text
[2, 3]
```

Sum:

```text
2 + 3 = 5
```

Absolute Sum:

```text
|5| = 5
```

---

### Example 2

**Input**

```text
nums = [2, -5, 1, -4, 3, -2]
```

**Output**

```text
8
```

**Explanation**

The maximum absolute sum comes from:

```text
[-5, 1, -4]
```

Sum:

```text
-5 + 1 + (-4) = -8
```

Absolute Sum:

```text
|-8| = 8
```

---

# Intuition

The maximum absolute sum can come from:

- A **very large positive** subarray sum.
- A **very large negative** subarray sum.

Therefore, we solve **two Kadane's Algorithms simultaneously**.

- One finds the **maximum subarray sum**.
- One finds the **minimum subarray sum**.

Finally,

```text
Answer = max(maximum_sum, |minimum_sum|)
```

---

# Approach

Maintain four variables.

### 1. `max_sum`

Maximum subarray sum ending at the current index.

### 2. `max_ans`

Overall maximum subarray sum.

### 3. `min_sum`

Minimum subarray sum ending at the current index.

### 4. `min_ans`

Overall minimum subarray sum.

---

# Code

```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_ans = nums[0]

        min_sum = nums[0]
        min_ans = nums[0]

        for i in range(1, len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            max_ans = max(max_ans, max_sum)

            min_sum = min(min_sum + nums[i], nums[i])
            min_ans = min(min_sum, min_ans)

        return max(max_ans, abs(min_ans))
```

---

# Explanation

Initialize all variables using the first element.

```python
max_sum = nums[0]
max_ans = nums[0]

min_sum = nums[0]
min_ans = nums[0]
```

Traverse the remaining elements.

```python
for i in range(1, len(nums)):
```

---

### Maximum Kadane

Either:

- Extend the previous subarray.

```python
max_sum + nums[i]
```

or

- Start a new subarray.

```python
nums[i]
```

Choose the larger one.

```python
max_sum = max(max_sum + nums[i], nums[i])
```

Update the overall maximum.

```python
max_ans = max(max_ans, max_sum)
```

---

### Minimum Kadane

Either:

- Extend the previous minimum subarray.

```python
min_sum + nums[i]
```

or

- Start a new subarray.

```python
nums[i]
```

Choose the smaller one.

```python
min_sum = min(min_sum + nums[i], nums[i])
```

Update the overall minimum.

```python
min_ans = min(min_ans, min_sum)
```

---

Finally,

```python
return max(max_ans, abs(min_ans))
```

because the largest absolute value can come from either the largest positive sum or the smallest negative sum.

---

# Dry Run

### Example

```text
nums = [2, -5, 1, -4, 3, -2]
```

| Index | Value | max_sum | max_ans | min_sum | min_ans |
|------:|------:|--------:|--------:|--------:|--------:|
| 0 | 2 | 2 | 2 | 2 | 2 |
| 1 | -5 | -3 | 2 | -5 | -5 |
| 2 | 1 | 1 | 2 | -4 | -5 |
| 3 | -4 | -3 | 2 | -8 | -8 |
| 4 | 3 | 3 | 3 | -5 | -8 |
| 5 | -2 | 1 | 3 | -7 | -8 |

Maximum positive sum:

```text
3
```

Minimum subarray sum:

```text
-8
```

Absolute values:

```text
|3| = 3
|-8| = 8
```

Final answer:

```text
8
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

Only a constant amount of extra space is used.

---

# Concepts Used

- Kadane's Algorithm
- Reverse Kadane's Algorithm
- Dynamic Programming
- Arrays

---

# Python Features Used

### max()

```python
max(a, b)
```

### min()

```python
min(a, b)
```

### abs()

```python
abs(x)
```

---

# Key Takeaways

- The maximum absolute sum is **not always** the maximum subarray sum.
- A large negative subarray can have a larger absolute value.
- Run **Kadane's Algorithm** for:
  - Maximum subarray sum.
  - Minimum subarray sum.
- Return the larger of:
  - Maximum positive sum.
  - Absolute value of the minimum (most negative) sum.
- Runs in **O(n)** time and **O(1)** extra space.

---

## Author

**Ramit Sarker**
