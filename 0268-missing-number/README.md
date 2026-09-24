# 268. Missing Number

## Problem

You are given an array `nums` containing `n` **distinct numbers** from the range:

```text
[0, n]
```

There are exactly `n` numbers in the array, but the range contains `n + 1` numbers.

Therefore, **exactly one number is missing**.

Return that missing number.

---

# Examples

## Example 1

```text
Input:  nums = [3, 0, 1]
Output: 2
```

There are `3` numbers in the array, so:

```text
n = 3
```

The complete range is:

```text
[0, 1, 2, 3]
```

The number `2` is missing.

---

## Example 2

```text
Input:  nums = [0, 1]
Output: 2
```

Here:

```text
n = 2
```

Complete range:

```text
[0, 1, 2]
```

The missing number is:

```text
2
```

---

## Example 3

```text
Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
```

There are `9` numbers, so the complete range is:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The only missing number is:

```text
8
```

---

# Approach

The main idea is to use the **sum of numbers**.

If:

```text
nums = [3, 0, 1]
```

then:

```text
n = 3
```

The complete range should be:

```text
0 + 1 + 2 + 3 = 6
```

But the actual array contains:

```text
3 + 0 + 1 = 4
```

Therefore:

```text
missing number = total sum - current sum

                = 6 - 4

                = 2
```

So the missing number can be found simply by subtracting the sum of the array from the expected sum of the complete range.

---

# Code

```python
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        current_sum = 0

        for i in range(n + 1):
            total_sum += i

        for j in nums:
            current_sum += j

        return total_sum - current_sum
```

---

# Code Explanation

## 1. Find `n`

```python
n = len(nums)
```

The problem states:

```text
n == nums.length
```

So the length of the array gives us `n`.

For:

```text
nums = [3, 0, 1]
```

we have:

```text
n = 3
```

Therefore, the complete range is:

```text
0 to 3
```

---

# 2. Initialize the Sums

```python
total_sum = 0
current_sum = 0
```

We maintain two sums:

### `total_sum`

The sum of all numbers that **should exist**:

```text
0 + 1 + 2 + ... + n
```

### `current_sum`

The sum of all numbers that **actually exist** in `nums`.

---

# 3. Calculate the Expected Sum

```python
for i in range(n + 1):
    total_sum += i
```

We use:

```python
range(n + 1)
```

because the range must include `n`.

For:

```text
n = 3
```

the loop produces:

```text
0, 1, 2, 3
```

So:

```text
total_sum = 0 + 1 + 2 + 3
           = 6
```

---

# 4. Calculate the Actual Sum

```python
for j in nums:
    current_sum += j
```

This traverses every number in the array.

For:

```text
nums = [3, 0, 1]
```

the calculation is:

```text
current_sum = 3 + 0 + 1
            = 4
```

---

# 5. Find the Missing Number

```python
return total_sum - current_sum
```

The complete range contains exactly one number that is absent from the array.

Therefore:

```text
total sum - actual sum
```

leaves exactly the missing number.

For our example:

```text
6 - 4 = 2
```

So:

```text
return 2
```

---

# Dry Run

Consider:

```python
nums = [3, 0, 1]
```

### Step 1: Find `n`

```text
n = len(nums)
n = 3
```

---

### Step 2: Calculate `total_sum`

Loop:

```text
i = 0 → total_sum = 0
i = 1 → total_sum = 1
i = 2 → total_sum = 3
i = 3 → total_sum = 6
```

Therefore:

```text
total_sum = 6
```

---

### Step 3: Calculate `current_sum`

Traverse the array:

```text
j = 3 → current_sum = 3
j = 0 → current_sum = 3
j = 1 → current_sum = 4
```

Therefore:

```text
current_sum = 4
```

---

### Step 4: Subtract

```text
missing = total_sum - current_sum

        = 6 - 4

        = 2
```

Final answer:

```text
2
```

---

# Another Dry Run

Consider:

```text
nums = [0, 1]
```

### `n`

```text
n = 2
```

Complete range:

```text
0, 1, 2
```

Expected sum:

```text
0 + 1 + 2 = 3
```

Actual sum:

```text
0 + 1 = 1
```

Therefore:

```text
missing = 3 - 1
        = 2
```

Answer:

```text
2
```

---

# Why Does It Work?

The problem guarantees that:

- The array contains `n` numbers.
- The valid range contains `n + 1` numbers: `0` through `n`.
- All numbers in the array are unique.
- Exactly one number is missing.

Suppose the complete range is:

```text
0 + 1 + 2 + ... + n
```

and its sum is `total_sum`.

The array contains every number from that range except one.

Therefore:

```text
total_sum = current_sum + missing
```

Rearranging:

```text
missing = total_sum - current_sum
```

That is exactly what the solution calculates.

---

# Algorithm

1. Find `n` using `len(nums)`.
2. Initialize `total_sum = 0`.
3. Add every number from `0` to `n` into `total_sum`.
4. Initialize `current_sum = 0`.
5. Traverse `nums` and add every element to `current_sum`.
6. Return:

```text
total_sum - current_sum
```

---

# Complexity Analysis

Let `n` be the number of elements in `nums`.

### Time Complexity

The solution uses two loops:

```python
for i in range(n + 1):
```

and:

```python
for j in nums:
```

The first loop takes `O(n)` time.

The second loop also takes `O(n)` time.

Therefore:

```text
O(n) + O(n) = O(n)
```

### Time Complexity

```text
O(n)
```

---

### Space Complexity

Only a few variables are used:

```text
n
total_sum
current_sum
i
j
```

No additional array, set, or dictionary is created.

### Space Complexity

```text
O(1)
```

This satisfies the follow-up requirement of **O(1) extra space** and **O(n) runtime**.

---

# Concepts Used

- Array traversal
- Array length
- Summation
- Difference between expected and actual values
- `for` loops
- `range()`
- `O(n)` traversal
- Constant extra space

---

# Python Features Used

### `len()`

```python
n = len(nums)
```

Gets the number of elements in the array.

---

### `range()`

```python
range(n + 1)
```

Generates all numbers from `0` through `n`.

---

### For-each Loop

```python
for j in nums:
```

Directly iterates over every element of the array.

---

# Key Takeaways

- The complete range is always `[0, n]`.
- The array contains exactly one number less than the complete range.
- The difference between the expected sum and actual sum gives the missing number.
- No sorting is required.
- No hash set is required.
- The solution uses **O(n) time**.
- The solution uses **O(1) extra space**.
- The approach directly satisfies the follow-up requirement.

---

# Author

**Ramit Sarker**
