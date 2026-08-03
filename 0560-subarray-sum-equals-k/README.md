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

The subarrays with sum `2` are:

```text
[1,1]   (index 0 → 1)

[1,1]   (index 1 → 2)
```

So the answer is:

```text
2
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

A brute-force approach checks every possible subarray.

For each starting index, calculate every possible ending index.

This requires:

```text
O(n²)
```

Instead, use the concept of **Prefix Sum**.

At every index, maintain the **running sum** from the beginning of the array.

If:

```text
Current Prefix Sum - Previous Prefix Sum = k
```

then the elements between those two prefix sums form a valid subarray.

So instead of searching for subarrays, we search for a **previous prefix sum**.

---

# Key Observation

Suppose the current running sum is:

```text
10
```

and

```text
k = 4
```

We need a previous prefix sum of:

```text
10 - 4 = 6
```

because

```text
10 - 6 = 4
```

If we've already seen a prefix sum of `6`, then we have found a subarray with sum `4`.

---

# Approach

Maintain:

- A running prefix sum.
- A HashMap storing the frequency of every prefix sum.

For every element:

1. Update the running sum.
2. Compute:

```text
needed = prefix_sum - k
```

3. If `needed` exists in the HashMap,
   add its frequency to the answer.
4. Store the current prefix sum in the HashMap.

---

# Why Do We Store Frequencies?

The same prefix sum may appear multiple times.

Each occurrence represents a different starting point for a valid subarray.

Example:

```text
Prefix Sum = 3
```

appears:

```text
2 times
```

If later we need:

```text
3
```

then both occurrences produce valid subarrays.

Therefore,

```python
count += hash_map[prefix_sum - k]
```

instead of

```python
count += 1
```

---

# Why Initialize

```python
hash_map = {0:1}
```

Before traversing the array, the running sum is:

```text
0
```

This allows subarrays that start from **index 0** to be counted correctly.

---

# Algorithm

### Step 1

Initialize:

```python
prefix_sum = 0
count = 0
hash_map = {0:1}
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
needed = prefix_sum - k
```

---

### Step 5

If it exists, add its frequency.

```python
count += hash_map[needed]
```

---

### Step 6

Store the current prefix sum.

```python
hash_map[prefix_sum] += 1
```

---

# Code

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hash_map = {0: 1}
        res = 0

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k

            if needed in hash_map:
                res += hash_map[needed]

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

Initially:

```text
prefix_sum = 0

hash_map = {0:1}

count = 0
```

| Current Number | Prefix Sum | Needed (`prefix_sum-k`) | Found? | Count |
|---------------:|-----------:|------------------------:|:------:|------:|
| 1 | 1 | -1 | ❌ | 0 |
| 1 | 2 | 0 | ✅ | 1 |
| 1 | 3 | 1 | ✅ | 2 |

Final Answer:

```text
2
```

---

# Why Does This Work?

Suppose:

```text
Current Prefix Sum = 10

k = 4
```

We need:

```text
Previous Prefix Sum = 6
```

because

```text
10 - 6 = 4
```

Every previous occurrence of prefix sum `6` forms a valid subarray ending at the current index.

The HashMap lets us find these in **O(1)** time.

---

# Time Complexity

```text
O(n)
```

Each element is processed exactly once.

HashMap operations take average **O(1)** time.

---

# Space Complexity

```text
O(n)
```

In the worst case, every prefix sum is different and stored in the HashMap.

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
prefix_sum += num
```

---

### HashMap Lookup

```python
if needed in hash_map:
```

---

### Frequency Update

```python
hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
```

---

# Key Takeaways

- Brute force takes **O(n²)**.
- Maintain a **running prefix sum**.
- A subarray sum can be found using:

```text
Current Prefix Sum - Previous Prefix Sum = k
```

- Store **prefix sum frequencies**, not just their existence.
- Initialize:

```python
hash_map = {0:1}
```

to handle subarrays starting from index `0`.
- Prefix Sum + HashMap reduces the complexity to **O(n)**.

---

## Author

**Ramit Sarker**
