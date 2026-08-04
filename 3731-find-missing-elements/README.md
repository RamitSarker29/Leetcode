# 4107. Find Missing Elements

## Problem

You are given an integer array `nums` containing **unique** integers.

Originally, the array contained **every integer within a certain range**, but some numbers are now missing.

The **smallest** and **largest** numbers of the original range are guaranteed to be present.

Return a **sorted list** of all the missing integers.

---

## Examples

### Example 1

**Input**

```text
nums = [1,4,2,5]
```

**Output**

```text
[3]
```

**Explanation**

The smallest and largest numbers are:

```text
1 and 5
```

The complete range should be:

```text
[1,2,3,4,5]
```

The missing number is:

```text
3
```

---

### Example 2

**Input**

```text
nums = [7,8,6,9]
```

**Output**

```text
[]
```

**Explanation**

The complete range is:

```text
[6,7,8,9]
```

No numbers are missing.

---

### Example 3

**Input**

```text
nums = [5,1]
```

**Output**

```text
[2,3,4]
```

**Explanation**

The complete range should be:

```text
[1,2,3,4,5]
```

The missing numbers are:

```text
2,3,4
```

---

# Intuition

A simple approach is to sort the array and check the gaps between consecutive numbers.

However, sorting takes:

```text
O(n log n)
```

We can do better.

Since we only need to check whether a number exists, we can store all numbers in a **HashSet**.

Then, iterate from the smallest number to the largest number and check which numbers are missing.

---

# Approach

1. Store every element in a HashSet.
2. Find the smallest and largest numbers.
3. Traverse every number between them.
4. If a number is not present in the HashSet, add it to the answer.
5. Return the result.

---

# Algorithm

### Step 1

Store all numbers in a HashSet.

```python
seen = set(nums)
```

---

### Step 2

Find the minimum and maximum values.

```python
min_num = min(nums)
max_num = max(nums)
```

---

### Step 3

Traverse the range.

```python
while min_num != max_num:
```

---

### Step 4

Check whether the next number exists.

```python
if min_num + 1 not in seen:
```

If not, add it to the answer.

```python
res.append(min_num + 1)
```

---

### Step 5

Move to the next number.

```python
min_num += 1
```

---

# Code

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        res = []

        min_num = min(nums)
        max_num = max(nums)

        while min_num != max_num:
            if min_num + 1 not in seen:
                res.append(min_num + 1)
            min_num += 1

        return res
```

---

# Dry Run

### Example

```text
nums = [1,4,2,5]
```

HashSet:

```text
{1,2,4,5}
```

Range:

```text
1 → 5
```

| Current | Check | Present? | Result |
|---------:|------:|:--------:|:------:|
| 1 | 2 | ✅ | [] |
| 2 | 3 | ❌ | [3] |
| 3 | 4 | ✅ | [3] |
| 4 | 5 | ✅ | [3] |

Final Answer:

```text
[3]
```

---

# Why HashSet?

Checking whether a value exists in a list takes:

```text
O(n)
```

Checking whether a value exists in a HashSet takes average:

```text
O(1)
```

This allows us to efficiently determine whether each number in the range is missing.

---

# Time Complexity

Creating the HashSet:

```text
O(n)
```

Finding the minimum and maximum:

```text
O(n)
```

Traversing the range:

```text
O(n)
```

Overall:

```text
O(n)
```

---

# Space Complexity

```text
O(n)
```

The HashSet stores all elements of the array.

---

# Concepts Used

- HashSet
- Arrays
- Linear Traversal

---

# Python Features Used

### Convert List to Set

```python
seen = set(nums)
```

---

### Find Minimum

```python
min_num = min(nums)
```

---

### Find Maximum

```python
max_num = max(nums)
```

---

### Membership Check

```python
if value not in seen:
```

---

# Key Takeaways

- Sorting solves the problem in **O(n log n)** time.
- A HashSet allows **O(1)** average lookup.
- Traverse the complete range from the minimum to the maximum value.
- Add every missing number to the answer.
- Overall complexity becomes **O(n)**.

---

## Author

**Ramit Sarker**
