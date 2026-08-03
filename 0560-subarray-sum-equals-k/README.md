# 560. Subarray Sum Equals K

## Problem

Given an integer array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum is exactly `k`.

A **subarray** is a contiguous non-empty sequence of elements within the array.

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

The valid subarrays are:

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

A brute-force approach checks every possible subarray and calculates its sum.

```text
Time Complexity = O(n²)
```

This is inefficient for large arrays.

Instead, we use a **Running Prefix Sum**.

At every index:

```text
Current Prefix Sum
=
Sum of all elements from index 0 to the current index.
```

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

If we've already seen prefix sum `6`, then we've found a subarray whose sum is `4`.

---

# Why HashMap?

The HashMap stores:

```text
Prefix Sum → Frequency
```

Example:

```python
{
    0: 1,
    3: 2,
    5: 1
}
```

This means:

- Prefix sum `0` has appeared once.
- Prefix sum `3` has appeared twice.
- Prefix sum `5` has appeared once.

Whenever we need a previous prefix sum,

```python
ans = prefix_sum - k
```

we simply check whether it exists in the HashMap.

---

# Why Store Frequency?

A prefix sum can occur multiple times.

Each occurrence represents a different starting point of a valid subarray.

So instead of

```python
res += 1
```

we do

```python
res += hash_map[ans]
```

to count **all** valid subarrays.

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

# Approach

1. Initialize:

```python
prefix_sum = 0
hash_map = {0:1}
res = 0
```

2. Traverse the array.

3. Update the running prefix sum.

```python
prefix_sum += i
```

4. Find the required previous prefix sum.

```python
ans = prefix_sum - k
```

5. If it exists, add its frequency.

```python
res += hash_map[ans]
```

6. Store the current prefix sum.

---

# Algorithm

1. Start with:

```python
prefix_sum = 0
hash_map = {0:1}
res = 0
```

2. Traverse the array.

3. Update:

```python
prefix_sum += i
```

4. Compute:

```python
ans = prefix_sum - k
```

5. If `ans` exists:

```python
res += hash_map[ans]
```

6. Store/update the current prefix sum frequency.

7. Return `res`.

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

| Current Number | Prefix Sum | `ans = prefix_sum-k` | Found? | Result |
|---------------:|-----------:|---------------------:|:------:|-------:|
| 1 | 1 | -1 | ❌ | 0 |
| 1 | 2 | 0 | ✅ (1 time) | 1 |
| 1 | 3 | 1 | ✅ (1 time) | 2 |

Final Answer:

```text
2
```

---

# Why Does This Work?

Suppose the current running sum is:

```text
Current Prefix Sum = 10
```

and

```text
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

If we've already seen prefix sum `6`, then a valid subarray exists.

The HashMap lets us find it in **O(1)** time.

---

# Time Complexity

```text
O(n)
```

Each element is visited exactly once.

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

### Find Required Prefix Sum

```python
ans = prefix_sum - k
```

---

### HashMap Lookup

```python
if ans in hash_map:
```

---

### Update Frequency

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
- Instead of searching for subarrays, search for a **previous prefix sum**.
- Use:

```text
Current Prefix Sum - Previous Prefix Sum = k
```

- Store **frequencies** of prefix sums in a HashMap.
- Initialize:

```python
hash_map = {0:1}
```

to count subarrays starting from index `0`.
- Prefix Sum + HashMap reduces the solution to **O(n)**.

---

## Author

**Ramit Sarker**
