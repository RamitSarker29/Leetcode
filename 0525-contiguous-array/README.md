# 525. Contiguous Array

## Problem

Given a binary array `nums`, return the **maximum length** of a contiguous subarray containing an **equal number of `0`s and `1`s**.

---

## Examples

### Example 1

**Input**

```text
nums = [0,1]
```

**Output**

```text
2
```

**Explanation**

The entire array contains one `0` and one `1`.

---

### Example 2

**Input**

```text
nums = [0,1,0]
```

**Output**

```text
2
```

**Explanation**

Possible longest subarrays are:

```text
[0,1]

[1,0]
```

Both have equal numbers of `0`s and `1`s.

---

### Example 3

**Input**

```text
nums = [0,1,1,1,1,1,0,0,0]
```

**Output**

```text
6
```

**Explanation**

The longest valid subarray is:

```text
[1,1,1,0,0,0]
```

---

# Intuition

A brute-force solution checks every possible subarray and counts the number of `0`s and `1`s.

```text
Time Complexity = O(n²)
```

This is too slow.

Instead, observe that whenever

```text
Number of 1s - Number of 0s
```

becomes the **same value again**, the subarray between those two indices contains an equal number of `0`s and `1`s.

Therefore, instead of storing frequencies, we store the **first index** where each difference appears.

---

# Key Observation

Suppose during traversal:

| Index | Zeros | Ones | Difference (Ones - Zeros) |
|------:|------:|-----:|--------------------------:|
| 2 | 2 | 3 | 1 |
| 7 | 5 | 6 | 1 |

The difference is the same.

Between index `2` and index `7`:

- Extra `1`s and `0`s cancel each other.
- Therefore, the subarray has an equal number of `0`s and `1`s.

Length:

```text
7 - 2 = 5
```

---

# Why HashMap?

The HashMap stores:

```text
Difference → First Index
```

Example:

```python
{
    1: 2,
    -2: 5,
    3: 8
}
```

This means:

- Difference `1` first appeared at index `2`.
- Difference `-2` first appeared at index `5`.

When the same difference appears again,

the subarray between those two indices has equal numbers of `0`s and `1`s.

---

# Why Store the First Index?

We want the **longest** subarray.

Suppose:

```text
Difference = 2
```

appears at

```text
Index 3
```

and later again at

```text
Index 10
```

Length:

```text
10 - 3 = 7
```

If we overwrite the first index,

we would get a shorter length.

Therefore, we only store the **first occurrence**.

---

# Approach

1. Count the number of `0`s and `1`s.
2. Compute:

```text
Difference = Ones - Zeros
```

3. If the difference becomes `0`, then the entire array from index `0` to the current index is valid.
4. If the difference has appeared before,
   compute the subarray length.
5. Otherwise, store its first occurrence.

---

# Algorithm

### Step 1

Initialize:

```python
zero = 0
one = 0
hash_map = {}
res = 0
```

---

### Step 2

Traverse the array.

```python
for i in range(len(nums)):
```

---

### Step 3

Update the counts.

```python
if nums[i] == 0:
    zero += 1
else:
    one += 1
```

---

### Step 4

Find the difference.

```python
diff = one - zero
```

---

### Step 5

If the difference becomes `0`,

the whole array till the current index is valid.

```python
res = max(res, i + 1)
```

---

### Step 6

If the difference has appeared before,

update the maximum length.

```python
res = max(res, i - hash_map[diff])
```

---

### Step 7

Otherwise,

store its first occurrence.

```python
hash_map[diff] = i
```

---

# Code

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = 0
        one = 0
        hash_map = {}
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = one - zero

            if diff == 0:
                res = max(res, i + 1)
                continue

            if diff in hash_map:
                res = max(res, i - hash_map[diff])
            else:
                hash_map[diff] = i

        return res
```

---

# Dry Run

### Example

```text
nums = [0,1,0]
```

Initially:

```text
zero = 0
one = 0
hash_map = {}
res = 0
```

| Index | Number | Zero | One | Difference | HashMap | Maximum Length |
|------:|-------:|-----:|----:|-----------:|:-------:|---------------:|
| 0 | 0 | 1 | 0 | -1 | {-1:0} | 0 |
| 1 | 1 | 1 | 1 | 0 | — | 2 |
| 2 | 0 | 2 | 1 | -1 | Found | 2 |

Final Answer:

```text
2
```

---

# Why Does This Work?

Whenever

```text
Difference = Ones - Zeros
```

becomes the same again,

the increase in `0`s and `1`s between those two indices is equal.

Therefore,

the subarray contains the same number of `0`s and `1`s.

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

In the worst case, every difference is unique.

---

# Concepts Used

- Prefix Sum
- HashMap
- Arrays

---

# Python Features Used

### Dictionary Lookup

```python
if diff in hash_map:
```

---

### Maximum Length

```python
res = max(res, i - hash_map[diff])
```

---

### Store First Occurrence

```python
hash_map[diff] = i
```

---

# Key Takeaways

- Brute force takes **O(n²)**.
- Maintain the running difference:

```text
Ones - Zeros
```

- If the same difference appears again, the subarray between them has equal numbers of `0`s and `1`s.
- Store the **first occurrence** of each difference.
- Unlike Problems **560** and **974**, this problem stores:

```text
Difference → First Index
```

instead of frequency.
- The solution runs in **O(n)** time using a HashMap.

---

## Author

**Ramit Sarker**
