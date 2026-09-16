# Second Largest Element

## Problem

Given an array of integers `nums`, return the **second-largest element** in the array.

If a second-largest element does not exist, return:

```text
-1
```

### Important

The second-largest element must be **strictly smaller than the largest element**.

Duplicate occurrences of the largest value do **not** count as the second largest.

For example:

```text
[8, 8, 7, 6, 5]
```

The largest value is `8`.

Even though `8` appears twice, the second-largest **distinct** value is:

```text
7
```

---

# Examples

## Example 1

```text
Input:
nums = [8, 8, 7, 6, 5]

Output:
7
```

### Explanation

The largest value is:

```text
8
```

The next distinct largest value is:

```text
7
```

Therefore:

```text
Answer = 7
```

---

## Example 2

```text
Input:
nums = [10, 10, 10, 10, 10]

Output:
-1
```

### Explanation

There is only one distinct value:

```text
10
```

Therefore, a second-largest distinct value does not exist.

So:

```text
Answer = -1
```

---

## Example 3

```text
Input:
nums = [7, 7, 2, 2, 10, 10, 10]

Output:
7
```

The distinct values are:

```text
10, 7, 2
```

Largest:

```text
10
```

Second largest:

```text
7
```

Therefore:

```text
Answer = 7
```

---

# Approach

We solve this problem in **one traversal** of the array.

We maintain two variables:

```python
largest1
largest2
```

where:

- `largest1` = largest value found so far.
- `largest2` = second-largest distinct value found so far.

Initially:

```python
largest1 = nums[0]
largest2 = -1
```

Then we traverse the array.

For every element, there are two important situations.

---

# Case 1: Current Element Is Greater Than `largest1`

```python
if nums[i] > largest1:
```

This means we have found a **new largest value**.

The previous largest value now becomes the second largest:

```python
largest2 = largest1
```

Then:

```python
largest1 = nums[i]
```

So both values are updated.

For example:

```text
Before:

largest1 = 8
largest2 = 5

current = 10
```

Since:

```text
10 > 8
```

we do:

```text
largest2 = 8
largest1 = 10
```

Now:

```text
largest1 = 10
largest2 = 8
```

---

# Case 2: Current Element Is Between `largest1` and `largest2`

The second condition is:

```python
if nums[i] > largest2 and nums[i] < largest1:
```

This means the current element:

1. Is larger than the current second largest.
2. Is smaller than the largest.

Therefore, it is a possible new second-largest value.

We update:

```python
largest2 = nums[i]
```

---

# Why `nums[i] < largest1` Is Important

This condition is extremely important:

```python
nums[i] < largest1
```

It prevents a duplicate of the largest value from becoming the second largest.

For example:

```text
nums = [8, 8, 7]
```

When the second `8` is encountered:

```text
8 > largest2
```

might be true.

But:

```text
8 < largest1
```

is false because:

```text
8 < 8
```

is false.

Therefore, the duplicate `8` is ignored.

The second largest remains:

```text
7
```

---

# Code

```python
class Solution:
    def secondLargestElement(self, nums):
        largest1 = nums[0]
        largest2 = -1

        for i in range(len(nums)):
            if nums[i] > largest1:
                largest2 = largest1
                largest1 = nums[i]

            if nums[i] > largest2 and nums[i] < largest1:
                largest2 = nums[i]

        return largest2
```

---

# Explanation

## Step 1: Initialize `largest1`

```python
largest1 = nums[0]
```

We initially assume that the first element is the largest.

For:

```text
nums = [8, 8, 7, 6, 5]
```

we start with:

```text
largest1 = 8
```

---

## Step 2: Initialize `largest2`

```python
largest2 = -1
```

Initially, we haven't found a second-largest value.

So:

```text
largest2 = -1
```

is used to represent that no second-largest value has been found yet.

---

## Step 3: Traverse the Array

```python
for i in range(len(nums)):
```

We examine every element exactly once.

---

## Step 4: Find a New Largest

```python
if nums[i] > largest1:
    largest2 = largest1
    largest1 = nums[i]
```

If the current element is larger than `largest1`, then:

```text
Old largest → becomes second largest
Current value → becomes largest
```

---

## Step 5: Find a Better Second Largest

```python
if nums[i] > largest2 and nums[i] < largest1:
    largest2 = nums[i]
```

This checks whether the current value lies between the largest and second-largest values.

In other words:

```text
largest2 < nums[i] < largest1
```

If yes, it becomes the new second largest.

---

## Step 6: Return the Answer

```python
return largest2
```

After the entire array has been traversed, `largest2` contains the second-largest distinct value.

If no such value exists, it remains:

```text
-1
```

---

# Dry Run

Let's take:

```text
nums = [8, 8, 7, 6, 5]
```

Initially:

```text
largest1 = 8
largest2 = -1
```

---

## Iteration 1

Current:

```text
8
```

First condition:

```text
8 > 8
```

False.

Second condition:

```text
8 > -1 and 8 < 8
```

The second part is false.

So:

```text
largest1 = 8
largest2 = -1
```

---

## Iteration 2

Current:

```text
8
```

Again:

```text
8 > 8
```

False.

And:

```text
8 < 8
```

is also false.

So the duplicate largest value is ignored.

```text
largest1 = 8
largest2 = -1
```

---

## Iteration 3

Current:

```text
7
```

Check:

```text
7 > 8
```

False.

Now:

```text
7 > -1 and 7 < 8
```

Both are true.

Therefore:

```text
largest2 = 7
```

Now:

```text
largest1 = 8
largest2 = 7
```

---

## Iteration 4

Current:

```text
6
```

Check:

```text
6 > 8
```

False.

Second condition:

```text
6 > 7 and 6 < 8
```

The first part is false.

So nothing changes:

```text
largest1 = 8
largest2 = 7
```

---

## Iteration 5

Current:

```text
5
```

Check:

```text
5 > 8
```

False.

Second condition:

```text
5 > 7 and 5 < 8
```

False.

Therefore:

```text
largest1 = 8
largest2 = 7
```

Final answer:

```text
7
```

---

# Dry Run Table

| Current | `largest1` Before | `largest2` Before | Action | `largest1` After | `largest2` After |
|---:|---:|---:|---|---:|---:|
| 8 | 8 | -1 | Ignore | 8 | -1 |
| 8 | 8 | -1 | Duplicate, ignore | 8 | -1 |
| 7 | 8 | -1 | Update second largest | 8 | 7 |
| 6 | 8 | 7 | Ignore | 8 | 7 |
| 5 | 8 | 7 | Ignore | 8 | 7 |

Final:

```text
Answer = 7
```

---

# Dry Run: New Largest Appears

Consider:

```text
nums = [5, 2, 10, 8]
```

Initially:

```text
largest1 = 5
largest2 = -1
```

### Current = 2

```text
2 > 5 → False
2 > -1 and 2 < 5 → True
```

So:

```text
largest1 = 5
largest2 = 2
```

### Current = 10

Now:

```text
10 > 5
```

True.

Therefore:

```text
largest2 = 5
largest1 = 10
```

Now:

```text
largest1 = 10
largest2 = 5
```

### Current = 8

```text
8 > 5 and 8 < 10
```

True.

So:

```text
largest2 = 8
```

Final:

```text
largest1 = 10
largest2 = 8
```

Therefore:

```text
Answer = 8
```

---

# Why Does It Work?

At any point during the traversal:

```text
largest1
```

stores the largest value seen so far.

And:

```text
largest2
```

stores the largest value that is **strictly smaller than `largest1`** among the elements seen so far.

When a new largest value appears:

```python
if nums[i] > largest1:
```

the old largest automatically becomes the second largest:

```python
largest2 = largest1
```

When the current value is not the largest but is greater than the current second largest:

```python
if nums[i] > largest2 and nums[i] < largest1:
```

we update `largest2`.

Thus, after the complete traversal:

```text
largest1 = largest element
largest2 = second-largest distinct element
```

---

# Handling Duplicates

This problem specifically allows duplicate values.

Consider:

```text
nums = [10, 10, 10, 10, 10]
```

We start with:

```text
largest1 = 10
largest2 = -1
```

Every other element is also `10`.

The condition:

```python
nums[i] < largest1
```

becomes:

```text
10 < 10
```

which is false.

Therefore, none of the duplicate `10`s can become `largest2`.

At the end:

```text
largest2 = -1
```

which is the correct answer.

---

# Important Condition

The following condition:

```python
nums[i] > largest2 and nums[i] < largest1
```

can be understood as:

```text
largest2 < nums[i] < largest1
```

This means:

> The current element must be bigger than the second largest but smaller than the largest.

That is exactly what we need.

---

# Algorithm

```text
1. Set largest1 = nums[0].

2. Set largest2 = -1.

3. Traverse every element.

4. If current element > largest1:
       largest2 = largest1
       largest1 = current element

5. Otherwise, if:
       current element > largest2
       AND
       current element < largest1

       Update:
       largest2 = current element

6. Return largest2.
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

The array is traversed exactly once.

If there are `n` elements, the algorithm performs `n` iterations.

---

## Space Complexity

```text
O(1)
```

Only two main variables are used:

```text
largest1
largest2
```

No sorting or additional data structures are required.

---

# Why Not Sort?

A simple approach would be:

```python
nums.sort()
```

and then search backwards for a value different from the largest.

However, sorting takes:

```text
O(n log n)
```

time.

Our approach only needs:

```text
O(n)
```

time.

So a single traversal is more efficient.

---

# Concepts Used

- Arrays
- Linear Traversal
- Finding Maximum
- Finding Second Maximum
- One-Pass Algorithm
- Comparison
- Handling Duplicates

---

# Python Features Used

### `for` Loop

```python
for i in range(len(nums)):
```

Used to traverse the entire array.

### Comparison Operators

```python
nums[i] > largest1
```

and:

```python
nums[i] > largest2 and nums[i] < largest1
```

Used to determine where the current value belongs.

### Variable Updating

```python
largest2 = largest1
largest1 = nums[i]
```

Updates the largest and second-largest values when necessary.

---

# Key Takeaways

- `largest1` stores the largest value.
- `largest2` stores the second-largest **distinct** value.
- When a new largest value appears, the old largest becomes the second largest.
- The condition `nums[i] < largest1` prevents duplicate largest values from becoming the second largest.
- If all elements are identical, `largest2` remains `-1`.
- No sorting is required.
- The array is traversed only once.
- Time Complexity: **O(n)**.
- Space Complexity: **O(1)**.

---

## Author

**Ramit Sarker**
