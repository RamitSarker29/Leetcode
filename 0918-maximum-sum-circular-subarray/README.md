# 918. Maximum Sum Circular Subarray

## Problem

Given a **circular integer array** `nums`, return the **maximum possible sum** of a **non-empty subarray**.

A circular array means the last element is connected to the first element.

A subarray may wrap around the end of the array, but each element can be used **at most once**.

---

## Examples

### Example 1

**Input**

```text
nums = [1, -2, 3, -2]
```

**Output**

```text
3
```

**Explanation**

The best subarray is:

```text
[3]
```

Sum:

```text
3
```

---

### Example 2

**Input**

```text
nums = [5, -3, 5]
```

**Output**

```text
10
```

**Explanation**

The circular subarray is:

```text
5 ←→ 5
```

which is equivalent to removing:

```text
[-3]
```

Sum:

```text
5 + 5 = 10
```

---

### Example 3

**Input**

```text
nums = [-3, -2, -3]
```

**Output**

```text
-2
```

**Explanation**

All numbers are negative.

The best subarray is:

```text
[-2]
```

---

# Intuition

There are **two possible answers**.

### Case 1: Normal Subarray

The maximum subarray does **not** wrap around.

Example:

```text
[1, -2, 3, -2]
```

Answer:

```text
[3]
```

This is solved using **Kadane's Algorithm**.

---

### Case 2: Circular Subarray

The maximum subarray wraps around.

Example:

```text
[5, -3, 5]
```

Instead of directly finding the circular subarray, remove the **minimum subarray**.

```text
Total Sum - Minimum Subarray Sum
```

Example:

```text
Total = 7

Minimum Subarray = [-3]

Answer = 7 - (-3) = 10
```

Therefore,

```text
Answer = max(
    Maximum Subarray Sum,
    Total Sum - Minimum Subarray Sum
)
```

---

# Approach

Maintain:

- `max_sum` → Maximum subarray sum ending at current index.
- `max_ans` → Overall maximum subarray sum.
- `min_sum` → Minimum subarray sum ending at current index.
- `min_ans` → Overall minimum subarray sum.
- `total_sum` → Sum of the entire array.

---

# Code

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_ans = nums[0]

        min_sum = nums[0]
        min_ans = nums[0]

        total_sum = nums[0]

        for i in range(1, len(nums)):
            total_sum += nums[i]

            max_sum = max(max_sum + nums[i], nums[i])
            max_ans = max(max_sum, max_ans)

            min_sum = min(min_sum + nums[i], nums[i])
            min_ans = min(min_sum, min_ans)

        return max_ans if max_ans < 0 else max(max_ans, total_sum - min_ans)
```

---

# Explanation

Initialize all variables with the first element.

```python
max_sum = nums[0]
max_ans = nums[0]

min_sum = nums[0]
min_ans = nums[0]

total_sum = nums[0]
```

Traverse the remaining elements.

```python
for i in range(1, len(nums)):
```

Update the total sum.

```python
total_sum += nums[i]
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

Choose the larger.

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

- Start a new minimum subarray.

```python
nums[i]
```

Choose the smaller.

```python
min_sum = min(min_sum + nums[i], nums[i])
```

Update the overall minimum.

```python
min_ans = min(min_ans, min_sum)
```

---

### Handle All Negative Arrays

If every element is negative,

```python
max_ans < 0
```

then:

```python
total_sum - min_ans
```

becomes `0`, which represents removing the entire array (an empty subarray), which is **not allowed**.

Therefore,

```python
return max_ans
```

Otherwise,

```python
return max(max_ans, total_sum - min_ans)
```

---

# Dry Run

### Example

```text
nums = [5, -3, 5]
```

| Index | Value | total_sum | max_sum | max_ans | min_sum | min_ans |
|------:|------:|----------:|--------:|--------:|--------:|--------:|
| 0 | 5 | 5 | 5 | 5 | 5 | 5 |
| 1 | -3 | 2 | 2 | 5 | -3 | -3 |
| 2 | 5 | 7 | 7 | 7 | 2 | -3 |

Normal Kadane:

```text
7
```

Circular Kadane:

```text
7 - (-3) = 10
```

Answer:

```text
10
```

---

### Example

```text
nums = [1, -2, 3, -2]
```

| Index | Value | total_sum | max_ans | min_ans |
|------:|------:|----------:|--------:|--------:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | -2 | -1 | 1 | -2 |
| 2 | 3 | 2 | 3 | -2 |
| 3 | -2 | 0 | 3 | -2 |

Normal:

```text
3
```

Circular:

```text
0 - (-2) = 2
```

Answer:

```text
3
```

---

### Example

```text
nums = [-3, -2, -3]
```

Maximum subarray:

```text
-2
```

Since all elements are negative,

```python
max_ans < 0
```

Return:

```text
-2
```

---

# Time Complexity

```text
O(n)
```

The array is traversed exactly once.

---

# Space Complexity

```text
O(1)
```

Only constant extra space is used.

---

# Concepts Used

- Kadane's Algorithm
- Reverse Kadane's Algorithm
- Circular Arrays
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

### Conditional Return

```python
return max_ans if max_ans < 0 else max(max_ans, total_sum - min_ans)
```

---

# Key Takeaways

- There are **two possible answers**:
  - Normal maximum subarray.
  - Circular maximum subarray.
- The circular answer is obtained by:
  - Finding the total array sum.
  - Removing the minimum subarray.
- If every element is negative, return the normal Kadane answer.
- Runs in **O(n)** time and **O(1)** extra space.

---

## Author

**Ramit Sarker**
