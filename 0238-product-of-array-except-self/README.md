# 238. Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] = product of all elements of nums except nums[i]
````

The solution must:

* Run in **O(n)** time.
* Not use division.
* Use **O(1) extra space**, excluding the output array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
[24,12,8,6]
```

For example:

```text
answer[0] = 2 × 3 × 4 = 24
answer[1] = 1 × 3 × 4 = 12
answer[2] = 1 × 2 × 4 = 8
answer[3] = 1 × 2 × 3 = 6
```

---

### Example 2

**Input**

```text
nums = [-1,1,0,-3,3]
```

**Output**

```text
[0,0,9,0,0]
```

---

# Approach

The product excluding `nums[i]` can be divided into two parts:

```text
product before i × product after i
```

For example:

```text
nums = [1,2,3,4]
```

For index `2`:

```text
product before = 1 × 2 = 2
product after  = 4
```

Therefore:

```text
answer[2] = 2 × 4 = 8
```

We calculate these two products using two traversals.

---

# First Traversal — Prefix Product

Use the output array itself to store the product of all elements **before** the current index.

Initially:

```python
answer = [1] * len(nums)
prefix = 1
```

For every index:

```python
answer[i] *= prefix
prefix *= nums[i]
```

For:

```text
nums = [1,2,3,4]
```

after the first traversal:

```text
answer = [1,1,2,6]
```

These values represent:

```text
index 0 → nothing before → 1
index 1 → 1 → 1
index 2 → 1×2 → 2
index 3 → 1×2×3 → 6
```

---

# Second Traversal — Suffix Product

Now traverse from **right to left**.

Maintain a variable:

```python
suffix = 1
```

At each index:

```python
answer[j] *= suffix
suffix *= nums[j]
```

`answer[j]` already contains the prefix product.

`suffix` contains the product of everything to the right.

Therefore:

```text
prefix × suffix
```

gives the required answer.

For:

```text
nums = [1,2,3,4]
```

the final result becomes:

```text
[24,12,8,6]
```

---

# Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        suffix = 1

        # Prefix products
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]

        # Suffix products
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]

        return answer
```

---

# Dry Run

For:

```text
nums = [1,2,3,4]
```

### First traversal

```text
answer = [1,1,2,6]
```

### Second traversal

Starting with:

```text
suffix = 1
```

From right to left:

```text
index 3:
answer[3] = 6 × 1 = 6
suffix = 4

index 2:
answer[2] = 2 × 4 = 8
suffix = 12

index 1:
answer[1] = 1 × 12 = 12
suffix = 24

index 0:
answer[0] = 1 × 24 = 24
```

Final:

```text
[24,12,8,6]
```

---

# Why It Works

For every index `i`:

```text
answer[i]
=
(product of elements before i)
×
(product of elements after i)
```

The first traversal stores the first part in `answer`.

The second traversal calculates the second part using only one variable, `suffix`.

This also handles zeros automatically because no division is used.

---

# Complexity

### Time Complexity

Two linear traversals:

```text
O(n) + O(n) = O(n)
```

Therefore:

```text
O(n)
```

### Space Complexity

Only `prefix` and `suffix` are additional variables.

The `answer` array is the required output and **does not count as extra space** according to the problem.

Therefore:

```text
O(1) extra space
```

---

# Key Takeaways

* Use **prefix products** from left to right.
* Use **suffix products** from right to left.
* Store prefix products directly in the output array.
* Keep the suffix product in a single variable.
* No division is required.
* Handles `0` and negative numbers naturally.
* Final complexity: **O(n) time, O(1) extra space**.

**Author**
**Ramit Sarker**

```
```
