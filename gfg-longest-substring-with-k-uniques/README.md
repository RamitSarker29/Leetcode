# Longest Substring with Exactly K Unique Characters 

## Problem

Given a string `s` consisting of lowercase English letters and an integer `k`, find the length of the **longest substring** that contains **exactly `k` distinct characters**.

If no such substring exists, return `-1`.

---

## Examples

### Example 1

**Input**

```text
s = "aabacbebebe"
k = 3
```

**Output**

```text
7
```

**Explanation**

The longest valid substring is:

```text
cbebebe
```

Distinct characters:

```text
c, b, e
```

Length:

```text
7
```

---

### Example 2

**Input**

```text
s = "aaaa"
k = 2
```

**Output**

```text
-1
```

**Explanation**

There is only one distinct character (`a`), so no substring contains exactly two distinct characters.

---

### Example 3

**Input**

```text
s = "aabaaab"
k = 2
```

**Output**

```text
7
```

**Explanation**

The entire string contains exactly two distinct characters (`a` and `b`).

---

## Approach

This problem is solved using the **Sliding Window** technique.

Maintain a window using two pointers:

- `i` → Left boundary of the window.
- `j` → Right boundary of the window.

Use a hash map to store the frequency of each character inside the current window.

### Algorithm

1. Expand the window by moving `j`.
2. Add the current character to the hash map.
3. If the window contains more than `k` distinct characters, shrink it from the left until it becomes valid.
4. Whenever the window contains exactly `k` distinct characters, update the maximum length.
5. If no valid substring is found, return `-1`.

---

## Code

```python
class Solution:
    def longestKSubstr(self, s, k):
        i = 0
        hash_map = {}
        max_len = 0

        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] += 1
            else:
                hash_map[s[j]] = 1

            if len(hash_map) == k:
                max_len = max(max_len, j - i + 1)

            while len(hash_map) > k:
                hash_map[s[i]] -= 1

                if hash_map[s[i]] == 0:
                    del hash_map[s[i]]

                i += 1

        return -1 if len(hash_map) < k else max_len
```

---

## Explanation

### Step 1

Initialize:

```python
i = 0
hash_map = {}
max_len = 0
```

- `i` is the left pointer.
- `hash_map` stores the frequency of characters.
- `max_len` stores the longest valid substring.

---

### Step 2

Traverse the string.

```python
for j in range(len(s)):
```

`j` acts as the right pointer.

The window keeps expanding.

---

### Step 3

Include the current character.

```python
if s[j] in hash_map:
    hash_map[s[j]] += 1
else:
    hash_map[s[j]] = 1
```

The hash map stores:

```text
Character → Frequency
```

Example:

```text
Window = "aabc"

{
'a':2,
'b':1,
'c':1
}
```

---

### Step 4

If the window has exactly `k` distinct characters,

```python
if len(hash_map) == k:
```

update the answer.

```python
max_len = max(max_len, j - i + 1)
```

---

### Step 5

If the window contains more than `k` distinct characters,

```python
while len(hash_map) > k:
```

shrink the window.

Decrease the frequency of the left character.

```python
hash_map[s[i]] -= 1
```

If its frequency becomes zero,

```python
del hash_map[s[i]]
```

remove it from the hash map because it no longer exists in the window.

Move the left pointer.

```python
i += 1
```

Repeat until the window becomes valid again.

---

### Step 6

If no valid substring exists,

return

```python
-1
```

Otherwise,

return the maximum length found.

---

## Dry Run

### Input

```text
s = "aabaaab"
k = 2
```

| Window | Distinct Characters | Length | Max Length |
|--------|----------------------|--------|-----------:|
| a | 1 | - | 0 |
| aa | 1 | - | 0 |
| aab | 2 | 3 | 3 |
| aaba | 2 | 4 | 4 |
| aabaa | 2 | 5 | 5 |
| aabaaa | 2 | 6 | 6 |
| aabaaab | 2 | 7 | 7 |

Answer:

```text
7
```

---

## Time Complexity

```text
O(n)
```

Each character enters and leaves the sliding window at most once.

---

## Space Complexity

```text
O(1)
```

The string contains only lowercase English letters.

The hash map stores at most **26** distinct characters.

Therefore,

```text
O(26) = O(1)
```

---

## Concepts Used

- Sliding Window
- Two Pointers
- Hash Map
- Frequency Counting
- Variable Size Sliding Window

---

## Python Features Used

### Dictionary

```python
hash_map = {}
```

Stores character frequencies.

---

### Membership Operator

```python
if s[j] in hash_map
```

Checks whether a character already exists.

---

### Delete from Dictionary

```python
del hash_map[s[i]]
```

Removes a character whose frequency becomes zero.

---

### Built-in Function

```python
max()
```

Used to maintain the maximum substring length.

---

## Key Takeaways

- Use a **variable-size sliding window** for substring problems.
- The hash map stores **character frequencies**, not indices.
- Expand the window using the right pointer.
- Shrink the window whenever the number of distinct characters exceeds `k`.
- Update the answer **only when the window contains exactly `k` distinct characters**.
- Since there are only 26 lowercase letters, the auxiliary space is **O(1)**.

---

**Author:** Ramit Sarker
