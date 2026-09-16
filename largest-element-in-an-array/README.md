# Largest Element in an Array

## Problem

Given an array of integers `nums`, return the **largest element** in the array.

The array may contain:

- Positive numbers
- Negative numbers
- Zero
- Duplicate values

We need to find the maximum value present in the array.

---

# Examples

## Example 1

```text
Input:
nums = [3, 3, 6, 1]

Output:
6

Explanation:
The largest element in the array is 6.
```

---

## Example 2

```text
Input:
nums = [3, 3, 0, 99, -40]

Output:
99

Explanation:
The largest element in the array is 99.
```

---

## Example 3

```text
Input:
nums = [-4, -3, 0, 1, -8]

Output:
1
```

The largest value among:

```text
-4, -3, 0, 1, -8
```

is:

```text
1
```

---

# Approach

We solve this problem using a simple **linear traversal**.

The idea is to keep track of the largest element found so far.

We initialize:

```python
largest = nums[0]
```

Then we traverse the entire array.

For every element:

```python
if largest < nums[i]:
```

If the current element is greater than `largest`, we update:

```python
largest = nums[i]
```

After checking every element, `largest` contains the maximum value in the array.

---

# Code

```python
class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for i in range(len(nums)):
            if largest < nums[i]:
                largest = nums[i]

        return largest
```

---

# Explanation

## Step 1: Initialize `largest`

```python
largest = nums[0]
```

We initially assume that the **first element** is the largest.

For example:

```text
nums = [3, 3, 6, 1]
```

Initially:

```text
largest = 3
```

We will compare this value with every other element.

---

## Step 2: Traverse the Array

```python
for i in range(len(nums)):
```

This loop visits every index of the array.

For:

```text
nums = [3, 3, 6, 1]
```

the indices are:

```text
0 → 3
1 → 3
2 → 6
3 → 1
```

---

## Step 3: Compare With Current Largest

```python
if largest < nums[i]:
```

We check whether the current element is greater than the largest value found so far.

If it is:

```python
largest = nums[i]
```

we update `largest`.

---

## Step 4: Return the Largest Value

After the loop finishes:

```python
return largest
```

At this point, every element has been checked, so `largest` contains the maximum value.

---

# Dry Run

Let's take:

```text
nums = [3, 3, 6, 1]
```

Initially:

```text
largest = nums[0]
       = 3
```

---

### Iteration 1

Current element:

```text
3
```

Check:

```text
largest < nums[i]
3 < 3
```

False.

So:

```text
largest = 3
```

---

### Iteration 2

Current element:

```text
3
```

Check:

```text
3 < 3
```

False.

So:

```text
largest = 3
```

---

### Iteration 3

Current element:

```text
6
```

Check:

```text
3 < 6
```

True.

Update:

```text
largest = 6
```

---

### Iteration 4

Current element:

```text
1
```

Check:

```text
6 < 1
```

False.

So:

```text
largest = 6
```

---

### Final Answer

```text
6
```

---

# Dry Run Table

| Index | Current Element | Largest Before | Comparison | Largest After |
|---:|---:|---:|---|---:|
| 0 | 3 | 3 | `3 < 3` → False | 3 |
| 1 | 3 | 3 | `3 < 3` → False | 3 |
| 2 | 6 | 3 | `3 < 6` → True | 6 |
| 3 | 1 | 6 | `6 < 1` → False | 6 |

Final:

```text
Answer = 6
```

---

# Dry Run With Negative Numbers

Consider:

```text
nums = [-4, -3, 0, 1, -8]
```

Initially:

```text
largest = -4
```

Now compare each element:

```text
-4 → largest = -4
-3 → largest = -3
 0 → largest = 0
 1 → largest = 1
-8 → largest = 1
```

Therefore:

```text
Answer = 1
```

This is why initializing with:

```python
largest = nums[0]
```

is important.

We should **not** initialize:

```python
largest = 0
```

because the array could contain only negative numbers.

For example:

```text
nums = [-5, -2, -9]
```

The correct answer is:

```text
-2
```

not `0`.

---

# Why Does It Work?

At any point during the traversal, `largest` represents:

> The largest element among all elements checked so far.

For example:

```text
nums = [3, 3, 6, 1]
```

After checking:

```text
[3, 3]
```

we have:

```text
largest = 3
```

After checking:

```text
[3, 3, 6]
```

we have:

```text
largest = 6
```

Finally, after checking the entire array:

```text
[3, 3, 6, 1]
```

`largest` must therefore be the largest element in the complete array.

So returning:

```python
return largest
```

gives the correct answer.

---

# Algorithm

```text
1. Set largest = nums[0].

2. Traverse the array from beginning to end.

3. For each element:
   
   If nums[i] > largest:
       Update largest = nums[i]

4. After traversing the entire array,
   return largest.
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

We visit every element exactly once.

If the array contains `n` elements, the loop performs `n` iterations.

---

## Space Complexity

```text
O(1)
```

We use only one extra variable:

```text
largest
```

No additional array, dictionary, or data structure is required.

---

# Concepts Used

- Arrays
- Linear Search
- Traversal
- Comparison
- Maximum Element
- One-Pass Algorithm

---

# Python Features Used

### `for` Loop

```python
for i in range(len(nums)):
```

Used to visit every index of the array.

### Comparison Operator

```python
largest < nums[i]
```

Used to determine whether the current element is larger.

### Variable Update

```python
largest = nums[i]
```

Updates the maximum value whenever a larger element is found.

---

# Key Takeaways

- Initialize `largest` with the **first element**, not `0`.
- Traverse the entire array.
- Compare every element with the current `largest`.
- If the current element is larger, update `largest`.
- After the traversal, `largest` contains the maximum element.
- The solution works for positive, negative, and duplicate values.
- Time Complexity: **O(n)**.
- Space Complexity: **O(1)**.

---

## Author

**Ramit Sarker**
