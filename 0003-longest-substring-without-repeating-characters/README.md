# LeetCode 3 - Longest Substring Without Repeating Characters

## Problem

Given a string `s`, return the length of the **longest substring** that contains **no repeating characters**.

A **substring** is a contiguous sequence of characters.

---

## Examples

### Example 1

**Input**

```text
s = "abcabcbb"
```

**Output**

```text
3
```

**Explanation**

The longest substring without repeating characters is:

```text
abc
```

Length = **3**

---

### Example 2

**Input**

```text
s = "bbbbb"
```

**Output**

```text
1
```

**Explanation**

The longest substring is:

```text
b
```

Length = **1**

---

### Example 3

**Input**

```text
s = "pwwkew"
```

**Output**

```text
3
```

**Explanation**

The longest substring is:

```text
wke
```

Length = **3**

---

## Approach

This is a **Variable Size Sliding Window** problem.

The goal is to find the **longest substring without duplicate characters**.

Use:

- Two pointers (`i` and `j`) to represent the current window.
- A hash map to store the frequency of each character.

### Algorithm

1. Expand the window by moving the right pointer.
2. Add the current character to the hash map.
3. If the current character appears more than once, shrink the window from the left until every character appears only once.
4. Once the window becomes valid, update the maximum length.
5. Continue until the end of the string.

---

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        max_len = 0
        hash_map = {}

        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] += 1
            else:
                hash_map[s[j]] = 1

            while hash_map[s[j]] > 1:
                hash_map[s[i]] -= 1

                if hash_map[s[i]] == 0:
                    del hash_map[s[i]]

                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len
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

- `i` → Left pointer
- `j` → Right pointer
- `hash_map` → Stores the frequency of characters in the current window
- `max_len` → Stores the length of the longest valid substring

---

### Step 2

Expand the window.

```python
for j in range(len(s)):
```

Move the right pointer one character at a time.

---

### Step 3

Insert the current character into the hash map.

```python
if s[j] in hash_map:
    hash_map[s[j]] += 1
else:
    hash_map[s[j]] = 1
```

Example:

```text
Window

a b c

Hash Map

{
'a':1,
'b':1,
'c':1
}
```

---

### Step 4

If the current character appears more than once,

```python
while hash_map[s[j]] > 1:
```

the window becomes invalid.

Shrink the window from the left.

Decrease the frequency of the left character.

```python
hash_map[s[i]] -= 1
```

If its frequency becomes zero,

```python
del hash_map[s[i]]
```

remove it from the hash map.

Move the left pointer.

```python
i += 1
```

Repeat until every character appears only once.

---

### Step 5

Now the window is valid.

Update the answer.

```python
max_len = max(max_len, j - i + 1)
```

---

## Dry Run

### Input

```text
s = "abcabcbb"
```

| Window | Valid | Longest |
|--------|:-----:|---------:|
| a | ✅ | 1 |
| ab | ✅ | 2 |
| abc | ✅ | 3 |
| abca | ❌ | Shrink |
| bca | ✅ | 3 |
| bcab | ❌ | Shrink |
| cab | ✅ | 3 |
| abc | ✅ | 3 |
| bcbb | ❌ | Shrink |
| b | ✅ | 3 |

Final Answer:

```text
3
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
O(min(n, m))
```

where:

- `n` = length of the string
- `m` = number of unique characters possible

The hash map stores only the characters present in the current window.

For ASCII characters, `m` is at most **128 (or 256 depending on the character set)**, so the space can be considered **O(1)**.

---

## Concepts Used

- Sliding Window
- Variable Size Window
- Two Pointers
- Hash Map
- Frequency Counting

---

## Python Features Used

### Dictionary

```python
hash_map = {}
```

Stores the frequency of characters.

---

### Membership Operator

```python
if s[j] in hash_map
```

Checks whether the character already exists.

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

Keeps track of the longest valid substring.

---

## Key Takeaways

- The window must contain **only unique characters**.
- Expand the window by moving the right pointer.
- Shrink the window whenever a duplicate character appears.
- Update the answer **only after the window becomes valid**.
- A hash map efficiently tracks character frequencies.
- This is a classic **variable-size sliding window** problem.

---

**Author:** Ramit Sarker
