# 217. Contains Duplicate

## Problem

Given an integer array `nums`, determine whether **any value appears at least twice**.

- Return `True` if a duplicate exists.
- Return `False` if every element is distinct.

---

# Examples

## Example 1

```text
Input:  nums = [1, 2, 3, 1]
Output: True
```

The number `1` appears twice:

```text
Index:  0  1  2  3
Value:  1  2  3  1
         ↑        ↑
```

Therefore, the answer is `True`.

---

## Example 2

```text
Input:  nums = [1, 2, 3, 4]
Output: False
```

Every element appears exactly once, so there is no duplicate.

---

## Example 3

```text
Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
```

There are multiple duplicate values, such as `1`, `3`, `4`, and `2`.

Therefore, the answer is `True`.

---

# Approach

The solution uses a **hash map (dictionary)** to keep track of the numbers that have already appeared.

The idea is simple:

1. Traverse the array from left to right.
2. For every number, check whether it already exists in the dictionary.
3. If it exists, we have found a duplicate → return `True`.
4. Otherwise, add it to the dictionary.
5. If the entire array is processed without finding a duplicate, return `False`.

### Main Idea

```text
Current number
      ↓
Already in hash_map?
   ↙           ↘
 Yes            No
  ↓              ↓
True       Add to hash_map
```

---

# Code

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] in hash_map:
                return True
            else:
                hash_map[nums[i]] = 1

        return False
```

---

# Code Explanation

## 1. Create a Hash Map

```python
hash_map = {}
```

The dictionary stores every number that we have already encountered.

Initially:

```text
hash_map = {}
```

---

## 2. Traverse the Array

```python
for i in range(len(nums)):
```

We visit every index one by one.

For:

```text
nums = [1, 2, 3, 1]
```

the indices are:

```text
0 → 1 → 2 → 3
```

---

## 3. Check Whether the Number Already Exists

```python
if nums[i] in hash_map:
```

This checks whether the current number has already been seen.

For example, if:

```text
hash_map = {1: 1, 2: 1, 3: 1}
```

and the current number is:

```text
nums[i] = 1
```

then:

```python
1 in hash_map
```

is `True`.

That means we have found a duplicate.

---

## 4. Return `True` Immediately

```python
return True
```

Once a duplicate is found, there is no need to examine the remaining elements.

For example:

```text
nums = [1, 2, 3, 1, 5, 6, 7]
```

As soon as the second `1` is encountered:

```text
1 → duplicate
```

we immediately return:

```text
True
```

This is called an **early return**.

---

## 5. Add New Numbers to the Hash Map

If the number hasn't appeared before:

```python
else:
    hash_map[nums[i]] = 1
```

The number is added to the dictionary.

For example:

```text
Current number = 5
```

and:

```text
5 not in hash_map
```

so we store:

```text
hash_map = {
    5: 1
}
```

The value `1` is not actually important here. We only care whether the key exists.

---

# Dry Run

Consider:

```python
nums = [1, 2, 3, 1]
```

### Initial State

```text
hash_map = {}
```

---

### Step 1 — `i = 0`

Current number:

```text
nums[0] = 1
```

Check:

```text
1 in hash_map?
```

No.

Add `1`:

```text
hash_map = {1: 1}
```

---

### Step 2 — `i = 1`

Current number:

```text
nums[1] = 2
```

Check:

```text
2 in hash_map?
```

No.

Add `2`:

```text
hash_map = {1: 1, 2: 1}
```

---

### Step 3 — `i = 2`

Current number:

```text
nums[2] = 3
```

Check:

```text
3 in hash_map?
```

No.

Add `3`:

```text
hash_map = {1: 1, 2: 1, 3: 1}
```

---

### Step 4 — `i = 3`

Current number:

```text
nums[3] = 1
```

Check:

```text
1 in hash_map?
```

Yes.

Therefore:

```python
return True
```

Final answer:

```text
True
```

---

# Dry Run — No Duplicate

Consider:

```python
nums = [1, 2, 3, 4]
```

Process:

```text
1 → not present → add
2 → not present → add
3 → not present → add
4 → not present → add
```

Final hash map:

```text
{
    1: 1,
    2: 1,
    3: 1,
    4: 1
}
```

The loop finishes without finding a duplicate.

Therefore:

```python
return False
```

---

# Why Does It Work?

At every index, the dictionary contains all the numbers that appeared **before** the current element.

Therefore, when we encounter a number:

```python
if nums[i] in hash_map:
```

there are only two possibilities:

### Number is not present

It is the first time we have encountered it.

So we add it to the dictionary.

### Number is already present

It appeared earlier in the array.

Therefore, it appears at least twice, meaning a duplicate exists.

So we can immediately return `True`.

If we reach the end of the array without finding such a number, every element was unique, so we return `False`.

---

# Why Use a Hash Map?

A naive approach would compare every element with every other element.

For example:

```text
1 ↔ 2
1 ↔ 3
1 ↔ 4
2 ↔ 3
2 ↔ 4
...
```

That would take:

```text
O(n²)
```

time.

With a hash map, we can check whether a number has appeared before in **average O(1)** time.

Therefore, the complete solution takes:

```text
O(n)
```

average time.

---

# Algorithm

1. Create an empty dictionary `hash_map`.
2. Traverse the array from left to right.
3. For each element:
   - If it already exists in `hash_map`, return `True`.
   - Otherwise, add it to `hash_map`.
4. If the loop finishes, return `False`.

---

# Complexity Analysis

Let `n` be the number of elements in `nums`.

### Time Complexity

We traverse the array once.

Dictionary membership checking:

```python
nums[i] in hash_map
```

takes **O(1) average time**.

Therefore:

```text
O(n)
```

average time complexity.

### Space Complexity

In the worst case, every element is unique, so all `n` elements are stored in the dictionary.

Therefore:

```text
O(n)
```

space complexity.

---

# Important Note About Complexity

The dictionary solution is **optimal in expected asymptotic time** for this approach:

```text
Time  → O(n) average
Space → O(n)
```

A Python `set` can also solve the problem in `O(n)` average time and `O(n)` space.

Sorting would generally take:

```text
O(n log n)
```

time, so it is slower asymptotically than the hash-based approach.

---

# Concepts Used

- Hashing
- Hash Map / Dictionary
- Array Traversal
- Membership Testing
- Early Return
- Average O(1) Hash Lookup
- Time-space tradeoff

---

# Python Features Used

### Dictionary

```python
hash_map = {}
```

Creates an empty dictionary.

---

### Dictionary Membership

```python
nums[i] in hash_map
```

Checks whether `nums[i]` exists as a key.

---

### Dictionary Insertion

```python
hash_map[nums[i]] = 1
```

Adds the current number as a key.

---

### `range()`

```python
range(len(nums))
```

Generates all valid indices of the array.

---

# Key Takeaways

- Use a hash map to remember elements that have already appeared.
- Before inserting a number, check whether it is already present.
- If it is already present, a duplicate has been found.
- Return immediately once a duplicate is detected.
- If the loop finishes, all elements are distinct.
- Hash-based lookup gives **O(n) average time**.
- The tradeoff is **O(n) extra space**.
- Your solution is an efficient and standard hash-map solution for this problem.

---

# Author

**Ramit Sarker**
