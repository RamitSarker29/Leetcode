# LeetCode 4264 - First Matching Character From Both Ends

## Problem

You are given a string `s` of length `n`.

Return the smallest index `i` such that:

```python
s[i] == s[n - i - 1]
```

If no such index exists, return `-1`.

---

## Examples

### Example 1

**Input**

```python
s = "abcacbd"
```

**Output**

```python
1
```

**Explanation**

```
Index 1 → 'b'
Mirror index 5 → 'b'
```

They are equal, so the answer is `1`.

---

### Example 2

**Input**

```python
s = "abc"
```

**Output**

```python
1
```

**Explanation**

```
Index 1 is the middle character.
```

It matches itself.

---

### Example 3

**Input**

```python
s = "abcdab"
```

**Output**

```python
-1
```

No matching pair exists.

---

# Approach

1. Initialize two pointers:
   - `i` at the beginning.
   - `j` at the end.
2. Compare `s[i]` and `s[j]`.
3. If they match, return `i`.
4. Otherwise, move:
   - `i` one step forward.
   - `j` one step backward.
5. If no match is found, return `-1`.

---

# Code

```python
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] == s[j]:
                return i
            else:
                i += 1
                j -= 1

        return -1
```

---

# Explanation

### Step 1: Initialize two pointers

```python
i = 0
j = len(s) - 1
```

```
i                 j
↓                 ↓

a b c a c b d
```

---

### Step 2: Compare both characters

```python
if s[i] == s[j]:
```

If they are equal, we've found the smallest valid index.

Return:

```python
return i
```

---

### Step 3: Move both pointers

If they are different:

```python
i += 1
j -= 1
```

```
Before

i                 j
↓                 ↓

a b c a c b d

After

  i           j
  ↓           ↓

a b c a c b d
```

Continue checking.

---

### Step 4: No match found

If the pointers cross:

```python
return -1
```

---

# Dry Run

Input

```python
s = "abcacbd"
```

Initially

```
i = 0
j = 6
```

Compare

```
a vs d
```

Not equal.

Move pointers.

```
i = 1
j = 5
```

Compare

```
b vs b
```

Equal.

Return

```python
1
```

---

# Time Complexity

Each character is checked at most once.

**Time Complexity:** `O(n)`

---

# Space Complexity

No extra data structures are used.

**Space Complexity:** `O(1)`

---

# Concepts Used

- Strings
- Two Pointers

---

# Python Features Used

- `len()`
- `while`
- String Indexing
- `return`

---

# Key Takeaways

- Two pointers efficiently compare characters from both ends.
- The first matching pair gives the smallest valid index.
- No extra memory is required.
- Runs in linear time.

---

# Author

**Ramit Sarker**
