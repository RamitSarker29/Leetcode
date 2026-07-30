# 152. Maximum Product Subarray

## Problem

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) that has the **largest product**, and return its product.

The answer is guaranteed to fit in a **32-bit integer**.

---

## Examples

### Example 1

**Input**

```text
nums = [2,3,-2,4]
```

**Output**

```text
6
```

**Explanation**

The maximum product subarray is:

```text
[2,3]
```

Product:

```text
2 × 3 = 6
```

---

### Example 2

**Input**

```text
nums = [-2,0,-1]
```

**Output**

```text
0
```

**Explanation**

Although:

```text
(-2) × (-1) = 2
```

they are **not contiguous** because `0` lies between them.

The maximum product subarray is:

```text
[0]
```

---

# Approach (Dynamic Programming / Modified Kadane's Algorithm)

Unlike the Maximum Sum Subarray problem, a **negative number can completely change the answer**.

- Multiplying a **large positive** product by a negative number becomes a **large negative** product.
- Multiplying a **large negative** product by another negative number becomes a **large positive** product.

Therefore, at every index we maintain:

- `max_ans` → Maximum product of a subarray ending at the current index.
- `min_ans` → Minimum product of a subarray ending at the current index.

For every element, there are three possibilities:

1. Start a new subarray.
2. Extend the previous maximum product.
3. Extend the previous minimum product.

The overall answer is updated using the maximum product seen so far.

---

# Code

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ans = nums[0]
        max_ans = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = min_ans * nums[i]
            v3 = max_ans * nums[i]

            min_ans = min(v1, min(v2, v3))
            max_ans = max(v1, max(v2, v3))

            ans = max(ans, max(min_ans, max_ans))

        return ans
```

---

# Explanation

Initialize all three variables with the first element.

```python
min_ans = nums[0]
max_ans = nums[0]
ans = nums[0]
```

Traverse the remaining elements.

```python
for i in range(1, len(nums)):
```

Three possible products:

Start a new subarray.

```python
v1 = nums[i]
```

Extend the previous minimum product.

```python
v2 = min_ans * nums[i]
```

Extend the previous maximum product.

```python
v3 = max_ans * nums[i]
```

Find the new minimum product ending at the current index.

```python
min_ans = min(v1, v2, v3)
```

Find the new maximum product ending at the current index.

```python
max_ans = max(v1, v2, v3)
```

Update the overall maximum product.

```python
ans = max(ans, max(min_ans, max_ans))
```

Return the answer.

```python
return ans
```

---

# Dry Run

### Example

```text
nums = [2,3,-2,4]
```

| Index | Current | v1 | v2 | v3 | min_ans | max_ans | ans |
|------:|--------:|---:|---:|---:|--------:|--------:|----:|
| 0 | 2 | - | - | - | 2 | 2 | 2 |
| 1 | 3 | 3 | 6 | 6 | 3 | 6 | 6 |
| 2 | -2 | -2 | -6 | -12 | -12 | -2 | 6 |
| 3 | 4 | 4 | -48 | -8 | -48 | 4 | 6 |

Final answer:

```text
6
```

---

### Example

```text
nums = [-2,0,-1]
```

| Index | Current | min_ans | max_ans | ans |
|------:|--------:|--------:|--------:|----:|
| 0 | -2 | -2 | -2 | -2 |
| 1 | 0 | 0 | 0 | 0 |
| 2 | -1 | -1 | 0 | 0 |

Return:

```text
0
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

Only constant extra space is used.

---

# Concepts Used

- Dynamic Programming
- Modified Kadane's Algorithm
- Arrays
- Negative Number Handling

---

# Python Features Used

### Multiple Assignment

```python
min_ans = max_ans = ans = nums[0]
```

### For Loop

```python
for i in range(1, len(nums)):
```

### min() and max()

```python
min_ans = min(v1, v2, v3)
max_ans = max(v1, v2, v3)
```

---

# Key Takeaways

- Product problems are harder than sum problems because **negative numbers can flip signs**.
- Track **both the maximum and minimum products** ending at each index.
- At every step, consider:
  - Starting a new subarray.
  - Extending the previous maximum product.
  - Extending the previous minimum product.
- Update the global answer using the current maximum product.
- The algorithm runs in **O(n)** time and **O(1)** space.

---

## Author

**Ramit Sarker**
