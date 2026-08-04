# 974. Subarray Sums Divisible by K

## Problem

Given an integer array `nums` and an integer `k`, return the **number of non-empty subarrays** whose sum is divisible by `k`.

A **subarray** is a contiguous sequence of elements within the array.

---

## Examples

### Example 1

**Input**

```text
nums = [4,5,0,-2,-3,1]
k = 5
```

**Output**

```text
7
```

**Explanation**

The valid subarrays are:

```text
[4,5,0,-2,-3,1]

[5]

[5,0]

[5,0,-2,-3]

[0]

[0,-2,-3]

[-2,-3]
```

---

### Example 2

**Input**

```text
nums = [5]
k = 9
```

**Output**

```text
0
```

---

# Intuition

A brute-force solution checks every possible subarray and calculates its sum.

```text
Time Complexity = O(n²)
```

This is inefficient.

Instead, use the concept of **Running Prefix Sum**.

If two prefix sums leave the **same remainder** when divided by `k`, then the difference between them is divisible by `k`.

Therefore,

instead of searching for subarrays,

we search for a **previous prefix sum having the same remainder**.

---

# Key Observation

Suppose:

```text
Current Prefix Sum = 17

k = 5
```

Current remainder:

```text
17 % 5 = 2
```

Now suppose an earlier prefix sum was:

```text
12
```

Its remainder is also:

```text
12 % 5 = 2
```

Subtract them:

```text
17 - 12 = 5
```

Since

```text
5 % 5 = 0
```

the subarray between these two prefix sums has a sum divisible by `5`.

Therefore,

if two prefix sums have the **same remainder**, they form a valid subarray.

---

# Why HashMap?

The HashMap stores:

```text
Remainder → Frequency
```

Example:

```python
{
    0:1,
    2:3,
    4:1
}
```

Meaning:

- Remainder `0` appeared once.
- Remainder `2` appeared three times.
- Remainder `4` appeared once.

Whenever we encounter a remainder we've already seen,

every previous occurrence forms another valid subarray.

---

# Why Initialize

```python
hash_map = {0:1}
```

Before processing any element,

```text
Prefix Sum = 0
```

whose remainder is

```text
0
```

This allows subarrays starting from **index 0** to be counted.

---

# Approach

1. Maintain a running prefix sum.
2. Compute its remainder with `k`.
3. If the remainder has appeared before, add its frequency to the answer.
4. Update the frequency of the current remainder.

---

# Algorithm

### Step 1

Initialize:

```python
sum = 0
hash_map = {0:1}
count = 0
```

---

### Step 2

Traverse the array.

```python
for i in nums:
```

---

### Step 3

Update the running prefix sum.

```python
sum += i
```

---

### Step 4

Find the current remainder.

```python
need = sum % k
```

If the remainder is negative,

convert it to a positive remainder.

```python
if need < 0:
    need += k
```

---

### Step 5

If this remainder already exists,

all previous occurrences form valid subarrays.

```python
count += hash_map[need]
```

---

### Step 6

Store the current remainder.

```python
hash_map[need] += 1
```

---

# Code

```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        hash_map = {0:1}
        count = 0

        for i in nums:
            sum += i

            need = sum % k

            if need < 0:
                need += k

            if need in hash_map:
                count += hash_map[need]
                hash_map[need] += 1
            else:
                hash_map[need] = 1

        return count
```

---

# Dry Run

### Example

```text
nums = [4,5,0,-2,-3,1]

k = 5
```

Initially:

```text
sum = 0

hash_map = {0:1}

count = 0
```

| Current Number | Prefix Sum | Remainder | Seen Before? | Count |
|---------------:|-----------:|----------:|:------------:|------:|
| 4 | 4 | 4 | ❌ | 0 |
| 5 | 9 | 4 | ✅ | 1 |
| 0 | 9 | 4 | ✅ | 3 |
| -2 | 7 | 2 | ❌ | 3 |
| -3 | 4 | 4 | ✅ | 6 |
| 1 | 5 | 0 | ✅ | 7 |

Final Answer:

```text
7
```

---

# Why Does This Work?

Suppose:

```text
Prefix Sum 1 = 17

Prefix Sum 2 = 12
```

Both have remainder:

```text
2
```

Their difference is:

```text
17 - 12 = 5
```

Since

```text
5 % 5 = 0
```

the subarray between them is divisible by `k`.

Therefore, every repeated remainder produces one or more valid subarrays.

---

# Time Complexity

```text
O(n)
```

Each element is processed once.

HashMap operations take average **O(1)** time.

---

# Space Complexity

```text
O(k)
```

At most `k` different remainders (`0` to `k-1`) can exist in the HashMap.

---

# Concepts Used

- Prefix Sum
- Running Prefix Sum
- HashMap
- Modulo Arithmetic

---

# Python Features Used

### Running Prefix Sum

```python
sum += i
```

---

### Modulo

```python
need = sum % k
```

---

### Dictionary Lookup

```python
if need in hash_map:
```

---

### Frequency Update

```python
hash_map[need] += 1
```

---

# Key Takeaways

- Brute force takes **O(n²)**.
- Maintain a **running prefix sum**.
- Compare **remainders**, not prefix sums.
- If two prefix sums have the same remainder, their difference is divisible by `k`.
- Store:

```text
Remainder → Frequency
```

instead of

```text
Prefix Sum → Frequency
```

- Initialize:

```python
hash_map = {0:1}
```

to count subarrays starting from index `0`.
- Using Prefix Sum + HashMap reduces the complexity to **O(n)**.

---

## Author

**Ramit Sarker**
