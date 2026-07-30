# 3090. Maximum Length Substring With Two Occurrences

## Problem

Given a string `s`, return the **maximum length** of a substring such that **each character appears at most two times**.

A substring is a **continuous** sequence of characters.

---

## Examples

### Example 1

**Input**

```text
s = "bcbbbcba"
```

**Output**

```text
4
```

**Explanation**

One valid substring is:

```text
"bcba"
```

Character frequencies:

```text
b → 2
c → 1
a → 1
```

Every character appears **at most two times**, so the substring is valid.

Length:

```text
4
```

---

### Example 2

**Input**

```text
s = "aaaa"
```

**Output**

```text
2
```

**Explanation**

The longest valid substring is:

```text
"aa"
```

Character frequency:

```text
a → 2
```

Length:

```text
2
```

---

# Approach (Sliding Window)

We use the **Sliding Window** technique.

Maintain:

- A left pointer `i`
- A right pointer `j`
- A hash map storing the frequency of characters inside the current window.

### Idea

Expand the window by moving `j`.

Whenever a character appears **more than two times**, the window becomes invalid.

Shrink the window from the left until every character appears at most twice.

After every valid window, update the maximum length.

---

# Code

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash_map = {}
        i, j = 0, 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] += 1
            else:
                hash_map[s[j]] = 1

            while hash_map[s[j]] > 2:
                hash_map[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len
```

---

# Explanation

Create a frequency map.

```python
hash_map = {}
```

Initialize both pointers.

```python
i = j = 0
```

Expand the window.

```python
for j in range(len(s)):
```

Increase the frequency of the current character.

```python
hash_map[s[j]] += 1
```

If the current character appears more than twice, shrink the window.

```python
while hash_map[s[j]] > 2:
```

Remove the leftmost character.

```python
hash_map[s[i]] -= 1
i += 1
```

Once the window becomes valid, update the answer.

```python
max_len = max(max_len, j - i + 1)
```

---

# Dry Run

### Example

```text
s = "bcbbbcba"
```

| Step | Window | Frequencies | Valid | Max Length |
|------|--------|-------------|:-----:|:----------:|
| b | b | b=1 | ✅ | 1 |
| bc | bc | b=1,c=1 | ✅ | 2 |
| bcb | bcb | b=2,c=1 | ✅ | 3 |
| bcbb | bcbb | b=3,c=1 | ❌ | 3 |
| shrink | cbb | b=2,c=1 | ✅ | 3 |
| cbbb | cbbb | b=3,c=1 | ❌ | 3 |
| shrink | bb | b=2 | ✅ | 3 |
| bbc | bbc | b=2,c=1 | ✅ | 3 |
| bbcb | bbcb | b=3,c=1 | ❌ | 3 |
| shrink | bcba | b=2,c=1,a=1 | ✅ | **4** |

Longest valid substring:

```text
"bcba"
```

Answer:

```text
4
```

---

### Example

```text
s = "aaaa"
```

| Step | Window | Frequency of a | Valid | Max Length |
|------|--------|----------------|:-----:|:----------:|
| a | a | 1 | ✅ | 1 |
| aa | aa | 2 | ✅ | 2 |
| aaa | aaa | 3 | ❌ | 2 |
| shrink | aa | 2 | ✅ | 2 |
| aaa | aaa | 3 | ❌ | 2 |
| shrink | aa | 2 | ✅ | 2 |

Answer:

```text
2
```

---

# Time Complexity

```text
O(n)
```

Each character enters and leaves the sliding window at most once.

---

# Space Complexity

```text
O(k)
```

Where `k` is the number of distinct characters in the window.

Since the string contains only lowercase English letters:

```text
k ≤ 26
```

So the extra space is effectively **O(1)**.

---

# Concepts Used

- Sliding Window
- Two Pointers
- Hash Map
- Frequency Counting

---

# Python Features Used

### Dictionary

```python
hash_map = {}
```

### Membership Check

```python
if s[j] in hash_map:
```

### For Loop

```python
for j in range(len(s)):
```

### While Loop

```python
while hash_map[s[j]] > 2:
```

### Maximum Function

```python
max(max_len, j - i + 1)
```

---

# Key Takeaways

- Expand the window by moving the right pointer.
- Maintain the frequency of each character using a hash map.
- If any character appears more than two times, shrink the window from the left.
- Update the answer whenever the current window is valid.
- This is a classic **variable-size sliding window** problem where the window is **invalid when a character frequency becomes greater than 2**.

---

## Author

**Ramit Sarker**
```
