# 128. Longest Consecutive Sequence

## Problem

Given an unsorted array of integers `nums`, return the **length of the longest consecutive elements sequence**.

A consecutive sequence contains numbers where each number is exactly `1` greater than the previous number.

The algorithm must run in **O(n)** time.

---

## Examples

### Example 1

**Input**

```text
nums = [100,4,200,1,3,2]
```

**Output**

```text
4
```

**Explanation**

The longest consecutive sequence is:

```text
[1,2,3,4]
```

Therefore, its length is:

```text
4
```

---

### Example 2

**Input**

```text
nums = [0,3,7,2,5,8,4,6,0,1]
```

**Output**

```text
9
```

The longest consecutive sequence is:

```text
[0,1,2,3,4,5,6,7,8]
```

---

### Example 3

**Input**

```text
nums = [1,0,1,2]
```

**Output**

```text
3
```

The longest consecutive sequence is:

```text
[0,1,2]
```

Duplicate values do not increase the sequence length.

---

# Intuition

The main idea is to use a **set**.

A set allows us to quickly check whether a particular number exists.

For example:

```text
nums = [100,4,200,1,3,2]
```

After converting it to a set:

```text
{100,4,200,1,3,2}
```

Suppose we encounter `1`.

We can check:

```text
2 exists?
```

Then:

```text
3 exists?
```

Then:

```text
4 exists?
```

Then:

```text
5 exists?
```

When `5` does not exist, the sequence ends.

So we found:

```text
1 → 2 → 3 → 4
```

with length `4`.

---

# Important Observation

We should **only start a sequence from its first number**.

A number `x` is the beginning of a sequence if:

```python
x - 1 not in nums
```

For example:

```text
1 → 2 → 3 → 4
```

For `1`:

```text
0 is not present
```

So `1` is the beginning.

For `2`:

```text
1 is present
```

Therefore, `2` is not the beginning.

This prevents us from repeatedly checking the same sequence.

---

# Approach

### Step 1

Convert the array into a set.

```python
nums = set(nums)
```

This also automatically removes duplicates.

---

### Step 2

Keep track of the longest sequence found.

```python
max_count = 0
```

---

### Step 3

Traverse every number in the set.

```python
for i in nums:
```

---

### Step 4

Check whether the current number is the beginning of a sequence.

```python
if i - 1 not in nums:
```

If `i - 1` exists, then `i` is already part of a sequence that started earlier.

---

### Step 5

Save the starting number.

```python
first = i
```

Then keep moving forward while the next number exists.

```python
while i + 1 in nums:
    i += 1
```

---

### Step 6

After the loop ends, `i` is the last number in the sequence.

```python
last = i
```

The length of the sequence is:

```text
last - first + 1
```

For example:

```text
1,2,3,4

4 - 1 + 1 = 4
```

---

### Step 7

Update the longest sequence.

```python
max_count = max(max_count, last - first + 1)
```

Finally, return `max_count`.

---

# Algorithm

1. Convert `nums` into a set.
2. Initialize `max_count = 0`.
3. For every number `i`:
   - Check if `i - 1` is absent.
   - If absent, `i` is the start of a sequence.
   - Keep increasing `i` while `i + 1` exists.
   - Calculate the sequence length.
   - Update the maximum length.
4. Return `max_count`.

---

# Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_count = 0

        for i in nums:
            if i - 1 not in nums:
                first = i

                while i + 1 in nums:
                    i += 1

                last = i

                max_count = max(max_count, last - first + 1)

        return max_count
```

---

# Dry Run

### Example

```text
nums = [100,4,200,1,3,2]
```

Convert to set:

```text
{100,4,200,1,3,2}
```

Suppose we reach `1`.

Check:

```text
1 - 1 = 0
```

`0` is not present.

So `1` is the beginning of a sequence.

Now check forward:

```text
2 exists → yes
3 exists → yes
4 exists → yes
5 exists → no
```

Therefore:

```text
first = 1
last = 4
```

Length:

```text
4 - 1 + 1 = 4
```

So:

```text
max_count = 4
```

The other numbers do not produce a longer sequence.

Return:

```text
4
```

---

# Why Does This Work?

The condition:

```python
if i - 1 not in nums:
```

ensures that we only begin counting from the **start** of a consecutive sequence.

For:

```text
1,2,3,4
```

we start at `1`.

We don't start again at `2`, `3`, or `4` because each of them has a predecessor in the set.

This avoids repeatedly traversing the same sequence.

---

# Time Complexity

Converting the list to a set:

```text
O(n)
```

The outer loop processes every unique number.

The inner `while` traverses each consecutive number as part of its sequence.

Because we only start a sequence when `i - 1` is absent, the same sequence is not repeatedly traversed.

Overall:

```text
O(n)
```

which satisfies the problem's requirement.

---

# Space Complexity

The set stores the unique elements of `nums`.

Therefore:

```text
O(n)
```

---

# Concepts Used

- Hash Set
- Greedy-style traversal
- Arrays
- Sequence Detection

---

# Python Features Used

### Convert List to Set

```python
nums = set(nums)
```

---

### Check Membership

```python
i - 1 not in nums
```

and

```python
i + 1 in nums
```

Set membership is average:

```text
O(1)
```

---

### Maximum

```python
max(max_count, length)
```

---

# Key Takeaways

- Use a **set** for fast membership checking.
- A number is the start of a sequence when `i - 1` is not present.
- Once a sequence starts, keep checking `i + 1`.
- Calculate its length using:

```text
last - first + 1
```

- Track the longest sequence found.
- The solution runs in **O(n)** time and uses **O(n)** extra space.

---

## Author

**Ramit Sarker**
