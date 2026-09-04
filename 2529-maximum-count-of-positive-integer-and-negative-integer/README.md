# 2614. Maximum Count of Positive Integer and Negative Integer

## Problem

Given an array `nums` sorted in **non-decreasing order**, return the maximum between:

- The number of **negative integers**
- The number of **positive integers**

`0` is neither positive nor negative.

The goal is to solve the problem in **O(log n)** time.

---

## Examples

### Example 1

**Input**

```text
nums = [-2,-1,-1,1,2,3]
```

**Output**

```text
3
```

**Explanation**

There are:

```text
Negative → 3
Positive → 3
```

Therefore:

```text
max(3, 3) = 3
```

---

### Example 2

**Input**

```text
nums = [-3,-2,-1,0,0,1,2]
```

**Output**

```text
3
```

**Explanation**

There are:

```text
Negative → 3
Positive → 2
```

Therefore:

```text
max(3, 2) = 3
```

---

### Example 3

**Input**

```text
nums = [5,20,66,1314]
```

**Output**

```text
4
```

**Explanation**

All four elements are positive:

```text
Positive → 4
Negative → 0
```

Therefore:

```text
max(4, 0) = 4
```

---

# Approach

Because the array is sorted, all negative numbers appear at the **beginning**, followed by zeros, followed by positive numbers.

For example:

```text
[-3,-2,-1,0,0,1,2,3]
  ↑         ↑       ↑
negative   zero   positive
```

This sorted structure allows us to use **Binary Search** instead of checking every element.

We perform two binary searches:

1. Find the first element that is **not negative** (`>= 0`).
2. Find the first element that is **positive** (`> 0`).

From these positions, we can calculate both counts.

---

# Finding the Number of Negative Integers

We want to find the first index where:

```text
nums[index] >= 0
```

Everything before that index must be negative.

For example:

```text
nums = [-3,-2,-1,0,0,1,2]
        0  1  2 3 4 5 6
```

The first element that is `>= 0` is:

```text
index = 3
```

Therefore:

```text
negative = 3
```

because indices:

```text
0, 1, 2
```

are all negative.

---

# Binary Search for Negatives

The code is:

```python
low = 0
high = len(nums) - 1

while low <= high:

    mid = (low + high) // 2

    if nums[mid] >= 0:
        high = mid - 1
    else:
        low = mid + 1
```

When the loop finishes:

```python
low
```

is the first index containing a value greater than or equal to zero.

Therefore:

```python
negative = low
```

---

# Why Does `low` Give the Negative Count?

Suppose:

```text
nums = [-3,-2,-1,0,0,1,2]
```

At the end:

```text
low = 3
```

The indices before `3` are:

```text
0, 1, 2
```

There are exactly `3` of them.

So:

```python
negative = low
```

gives:

```text
negative = 3
```

This works because the array is sorted.

---

# Finding the Number of Positive Integers

Now we want to find the first element that is **strictly positive**:

```text
nums[index] > 0
```

For:

```text
[-3,-2,-1,0,0,1,2]
```

the first positive number is:

```text
1
```

at index:

```text
5
```

Everything from index `5` onward is positive:

```text
1, 2
```

So:

```text
positive = len(nums) - 5
         = 7 - 5
         = 2
```

---

# Binary Search for Positives

The code is:

```python
low = 0
high = len(nums) - 1

while low <= high:

    mid = (low + high) // 2

    if nums[mid] > 0:
        high = mid - 1
    else:
        low = mid + 1
```

When the loop finishes:

```python
low
```

is the first index containing a positive number.

Therefore:

```python
positive = len(nums) - low
```

---

# Why `len(nums) - low`?

Suppose:

```text
nums = [-3,-2,-1,0,0,1,2]
```

and:

```text
low = 5
```

The positive elements are:

```text
indices: 5, 6
```

The number of elements from index `5` to the end is:

```text
7 - 5 = 2
```

Therefore:

```python
positive = len(nums) - low
```

---

# Important Difference Between the Two Searches

The two binary searches look very similar, but their conditions are slightly different.

### Negative Search

We want the first element that is:

```text
>= 0
```

So:

```python
if nums[mid] >= 0:
    high = mid - 1
```

Otherwise:

```python
else:
    low = mid + 1
```

---

### Positive Search

We want the first element that is:

```text
> 0
```

So:

```python
if nums[mid] > 0:
    high = mid - 1
```

Otherwise:

```python
else:
    low = mid + 1
```

The difference is:

```text
Negative search → >= 0
Positive search → > 0
```

This correctly handles zeros.

---

# Why Are Zeros Not Counted?

The problem states:

```text
0 is neither positive nor negative.
```

Suppose:

```text
nums = [-2,-1,0,0,1,2]
```

The first non-negative element is:

```text
0
```

So the negative count stops before it:

```text
negative = 2
```

For the positive count, we specifically search for:

```text
> 0
```

so both zeros are skipped.

Therefore:

```text
positive = 2
```

The zeros are never included in either count.

---

# Code

```python
class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        positive = 0
        negative = 0

        # Find first non-negative element
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] >= 0:
                high = mid - 1
            else:
                low = mid + 1

        negative = low

        # Find first positive element
        low = 0
        high = len(nums) - 1

        positive = 0

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] > 0:
                high = mid - 1
            else:
                low = mid + 1

        positive = len(nums) - low

        return max(positive, negative)
```

---

# Dry Run

Consider:

```text
nums = [-3,-2,-1,0,0,1,2]
```

Index:

```text
       0   1   2  3  4  5  6
nums = -3  -2  -1  0  0  1  2
```

---

## Part 1: Find Negative Count

Initially:

```text
low = 0
high = 6
```

### First iteration

```text
mid = (0 + 6) // 2
mid = 3
```

Value:

```text
nums[3] = 0
```

Since:

```text
0 >= 0
```

we move left:

```text
high = mid - 1
high = 2
```

---

### Second iteration

```text
low = 0
high = 2

mid = 1
```

Value:

```text
nums[1] = -2
```

Since:

```text
-2 < 0
```

we move right:

```text
low = mid + 1
low = 2
```

---

### Third iteration

```text
low = 2
high = 2

mid = 2
```

Value:

```text
nums[2] = -1
```

Again:

```text
-1 < 0
```

So:

```text
low = 3
```

Now:

```text
low = 3
high = 2
```

The loop stops.

Therefore:

```text
negative = low
         = 3
```

There are `3` negative numbers.

---

# Part 2: Find Positive Count

Reset:

```text
low = 0
high = 6
```

### First iteration

```text
mid = 3
nums[3] = 0
```

Since:

```text
0 <= 0
```

we move right:

```text
low = 4
```

---

### Second iteration

```text
low = 4
high = 6

mid = 5
```

Value:

```text
nums[5] = 1
```

Since:

```text
1 > 0
```

we move left:

```text
high = 4
```

---

### Third iteration

```text
low = 4
high = 4

mid = 4
```

Value:

```text
nums[4] = 0
```

Since it is not positive:

```text
low = mid + 1
low = 5
```

Now:

```text
low = 5
high = 4
```

Loop ends.

Therefore:

```text
positive = len(nums) - low
         = 7 - 5
         = 2
```

---

# Final Result

We found:

```text
negative = 3
positive = 2
```

Therefore:

```python
max(positive, negative)
```

is:

```text
3
```

Final answer:

```text
3
```

---

# Binary Search Visualization

The first search finds the boundary:

```text
[-3,-2,-1 | 0,0,1,2]
             ↑
          first >= 0
```

So:

```text
negative = 3
```

The second search finds:

```text
[-3,-2,-1,0,0 | 1,2]
                ↑
             first > 0
```

So:

```text
positive = 2
```

The entire problem is essentially finding these **two boundaries**.

---

# Why Binary Search Works

The array is sorted in non-decreasing order.

Therefore, its structure is always:

```text
negative → zero → positive
```

There cannot be a positive number before a negative number, and there cannot be a negative number after a zero.

This means the transition points can be found using Binary Search.

We don't need to inspect every element.

---

# Algorithm

### Find Negative Count

1. Set `low = 0` and `high = n - 1`.
2. Binary search for the first element `>= 0`.
3. The resulting `low` is the number of negative elements.

### Find Positive Count

1. Reset `low = 0` and `high = n - 1`.
2. Binary search for the first element `> 0`.
3. The number of elements from this index to the end is the positive count.

### Final Step

Return:

```python
max(positive, negative)
```

---

# Complexity

Let:

```text
n = len(nums)
```

We perform two binary searches.

Each binary search takes:

```text
O(log n)
```

Therefore:

### Time Complexity

```text
O(log n) + O(log n)
= O(log n)
```

### Space Complexity

Only a few variables are used:

```text
O(1)
```

---

# Key Takeaways

- The array is sorted, so we can use **Binary Search**.
- The array has the structure:
  ```text
  negative → zero → positive
  ```
- First binary search finds the first element `>= 0`.
- Its index is the number of negative elements.
- Second binary search finds the first element `> 0`.
- `len(nums) - low` gives the number of positive elements.
- `0` is excluded from both counts.
- The two searches differ only in their boundary conditions:
  ```python
  nums[mid] >= 0
  ```
  for negatives, and:
  ```python
  nums[mid] > 0
  ```
  for positives.
- Return:
  ```python
  max(positive, negative)
  ```
- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
