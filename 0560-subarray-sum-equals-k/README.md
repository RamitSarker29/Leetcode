# 560. Subarray Sum Equals K

## Problem

Given an integer array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum is exactly `k`.

A **subarray** is a contiguous sequence of elements within the array.

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,1]
k = 2
```

**Output**

```text
2
```

**Explanation**

The subarrays are:

```text
[1,1]   (index 0 → 1)

[1,1]   (index 1 → 2)
```

---

### Example 2

**Input**

```text
nums = [1,2,3]
k = 3
```

**Output**

```text
2
```

**Explanation**

The valid subarrays are:

```text
[1,2]

[3]
```

---

# Intuition

A brute-force solution checks every possible subarray and calculates its sum.

This takes:

```text
O(n²)
```

Instead, we use a **running prefix sum**.

At every index:

```text
Current Prefix Sum
```

stores the sum from the beginning of the array up to the current index.

If

```text
Current Prefix Sum - Previous Prefix Sum = k
```

then the elements between those two prefix sums form a valid subarray.

So instead of searching for subarrays, we search for a **previous prefix sum**.

---

# Key Observation

Suppose:

```text
Current Prefix Sum = 10

k = 4
```

Then we need a previous prefix sum of:

```text
10 - 4 = 6
```

because

```text
10 - 6 = 4
```

If we've already seen prefix sum `6`, then we've found a valid subarray.

---

# Approach

Maintain:

- A running prefix sum.
- A HashMap storing the **frequency** of every prefix sum.

For every element:

1. Update the running prefix sum.
2. Compute:

```text
needed = prefix_sum - k
```

3. If `needed` exists in the HashMap, add its frequency to the answer.
4. Store the current prefix sum in the HashMap.

---

# Why Frequency?

The same prefix sum can appear multiple times.

Each occurrence represents a different starting point for a valid subarray.

Therefore,

```python
res += hash_map[needed]
```

instead of

```python
res += 1
```

---

# Why Initialize

```python
hash_map = {0:1}
```

Before processing any element,

```text
Prefix Sum = 0
```

This helps count subarrays that begin from **index 0**.

---

# Algorithm

### Step 1

Initialize:

```python
prefix_sum = 0
hash_map = {0:1}
res = 0
```

---

### Step 2

Traverse the array.

```python
for num in nums:
```

---

### Step 3

Update the running prefix sum.

```python
prefix_sum += num
```

---

### Step 4

Find the required previous prefix sum.

```python
ans = prefix_sum - k
```

---

### Step 5

If it exists, add its frequency.

```python
if ans in hash_map:
    res += hash_map[ans]
```

---

### Step 6

Store the current prefix sum.

```python
if prefix_sum in hash_map:
    hash_map[prefix_sum] += 1
else:
    hash_map[prefix_sum] = 1
```

---

# Code

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hash_map = {0:1}
        res = 0

        for i in nums:
            prefix_sum += i

            ans = prefix_sum - k

            if ans in hash_map:
                res += hash_map[ans]

            if prefix_sum in hash_map:
                hash_map[prefix_sum] += 1
            else:
                hash_map[prefix_sum] = 1

        return res
```

---

# Dry Run

### Example

```text
nums = [1,1,1]
k = 2
```

Initially

```text
prefix_sum = 0

hash_map = {0:1}

res = 0
```

| Current Number | Prefix Sum | Needed (`prefix_sum-k`) | HashMap | Result |
|---------------:|-----------:|------------------------:|:-------:|-------:|
| 1 | 1 | -1 | Not Found | 0 |
| 1 | 2 | 0 | Found (1 time) | 1 |
| 1 | 3 | 1 | Found (1 time) | 2 |

Final Answer:

```text
2
```

---

# Why Does This Work?

At every index,

```text
Current Prefix Sum
```

contains the sum from the beginning.

If

```text
Current Prefix Sum - Previous Prefix Sum = k
```

then the elements between those two prefix sums form a valid subarray.

The HashMap lets us quickly check whether the required previous prefix sum has already appeared.

---

# Time Complexity

```text
O(n)
```

Each element is processed exactly once.

HashMap lookup and insertion take average **O(1)** time.

---

# Space Complexity

```text
O(n)
```

In the worst case, every prefix sum is unique and stored in the HashMap.

---

# Concepts Used

- Prefix Sum
- Running Prefix Sum
- HashMap
- Arrays

---

# Python Features Used

### Running Prefix Sum

```python
prefix_sum += i
```

---

### Dictionary Lookup

```python
if ans in hash_map:
```

---

### Frequency Update

```python
if prefix_sum in hash_map:
    hash_map[prefix_sum] += 1
else:
    hash_map[prefix_sum] = 1
```

---

# Key Takeaways

- Brute force takes **O(n²)**.
- Maintain a **running prefix sum**.
- Use the relation:

```text
Current Prefix Sum - Previous Prefix Sum = k
```

- Store **frequencies** of prefix sums, not just their existence.
- Initialize:

```python
hash_map = {0:1}
```

to count subarrays starting from index `0`.
- Prefix Sum + HashMap reduces the solution to **O(n)**.

---

## Author

**Ramit Sarker**
