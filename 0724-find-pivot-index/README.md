# 724. Find Pivot Index

## Problem

Given an integer array `nums`, return the **pivot index**.

The **pivot index** is the index where:

- The sum of all elements to the **left** is equal to
- The sum of all elements to the **right**.

If multiple pivot indices exist, return the **leftmost** one.

If no pivot index exists, return `-1`.

---

## Examples

### Example 1

**Input**

```text
nums = [1,7,3,6,5,6]
```

**Output**

```text
3
```

**Explanation**

At index `3`:

```text
Left Sum  = 1 + 7 + 3 = 11
Right Sum = 5 + 6 = 11
```

Since both sums are equal, the pivot index is:

```text
3
```

---

### Example 2

**Input**

```text
nums = [1,2,3]
```

**Output**

```text
-1
```

No index satisfies the condition.

---

### Example 3

**Input**

```text
nums = [2,1,-1]
```

**Output**

```text
0
```

Explanation:

```text
Left Sum  = 0
Right Sum = 1 + (-1) = 0
```

---

# Intuition

A brute-force approach would calculate the left and right sums for every index.

For each index:

- Calculate left sum.
- Calculate right sum.

This takes:

```text
O(n²)
```

Instead, notice that the **total sum** of the array is already known.

If we also know the **left sum**, then the **right sum** can be calculated directly.

---

# Key Observation

At any index:

```text
Total Sum = Left Sum + Current Element + Right Sum
```

Rearranging,

```text
Right Sum = Total Sum - Left Sum - Current Element
```

So we never need to calculate the right side separately.

---

# Approach

1. Compute the total sum of the array.
2. Initialize:

```python
left = 0
```

3. Traverse the array.

For every index:

- Compute the right sum.

```python
right = total - left - nums[i]
```

- If:

```text
left == right
```

return the current index.

- Otherwise, move the current element to the left side.

```python
left += nums[i]
```

---

# Algorithm

### Step 1

Find the total sum.

```python
total = sum(nums)
```

---

### Step 2

Initialize:

```python
left = 0
```

---

### Step 3

Traverse the array.

```python
for i in range(len(nums)):
```

---

### Step 4

Find the right sum.

```python
right = total - left - nums[i]
```

---

### Step 5

Check whether the current index is the pivot.

```python
if left == right:
    return i
```

---

### Step 6

Move the current element to the left side.

```python
left += nums[i]
```

---

# Code

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - nums[i] - left

            if left == right:
                return i

            left += nums[i]

        return -1
```

---

# Dry Run

### Example

```text
nums = [1,7,3,6,5,6]
```

Total Sum:

```text
28
```

| Index | Left Sum | Current | Right Sum | Pivot? |
|------:|---------:|--------:|----------:|:------:|
| 0 | 0 | 1 | 27 | ❌ |
| 1 | 1 | 7 | 20 | ❌ |
| 2 | 8 | 3 | 17 | ❌ |
| 3 | 11 | 6 | 11 | ✅ |

Answer:

```text
3
```

---

# Why Does This Work?

At every index:

```text
Total Sum
=
Left Sum
+
Current Element
+
Right Sum
```

Since the total sum is already known,

we can calculate the right sum in **O(1)** time.

The left sum is maintained as a **running prefix sum**, so no extra array is required.

---

# Running Prefix Sum

Initially,

```text
left = 0
```

As we move through the array:

```python
left += nums[i]
```

`left` always represents:

```text
Sum of all elements before the current index.
```

This is why the solution uses only **O(1)** extra space.

---

# Time Complexity

```text
O(n)
```

- One pass to compute the total sum.
- One pass to find the pivot index.

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

No extra prefix array is created.

---

# Concepts Used

- Arrays
- Prefix Sum
- Running Prefix Sum

---

# Python Features Used

### Find Total Sum

```python
total = sum(nums)
```

---

### Traverse the Array

```python
for i in range(len(nums)):
```

---

### Running Prefix Sum

```python
left += nums[i]
```

---

# Key Takeaways

- A brute-force solution recalculates sums for every index, resulting in **O(n²)** time.
- Instead of computing the right sum repeatedly, use:

```text
Right Sum = Total Sum - Left Sum - Current Element
```

- Maintain the left sum as a **running prefix sum**.
- No extra prefix array is needed, giving **O(1)** space complexity.
- This is a classic application of the **Prefix Sum** pattern.

---

## Author

**Ramit Sarker**
