# 1456. Maximum Number of Vowels in a Substring of Given Length

## Problem

Given a string `s` and an integer `k`, return the **maximum number of vowels** in any substring of **length exactly `k`**.

The vowels are:

```text
a, e, i, o, u
```

---

## Examples

### Example 1

**Input**

```text
s = "abciiidef"
k = 3
```

**Output**

```text
3
```

**Explanation**

Possible substrings of length `3`:

```text
abc → 1 vowel
bci → 1 vowel
cii → 2 vowels
iii → 3 vowels ✅
iid → 2 vowels
ide → 2 vowels
def → 1 vowel
```

Maximum number of vowels:

```text
3
```

---

### Example 2

**Input**

```text
s = "aeiou"
k = 2
```

**Output**

```text
2
```

---

### Example 3

**Input**

```text
s = "leetcode"
k = 3
```

**Output**

```text
2
```

---

# Intuition

The substring length is **fixed** (`k`).

Instead of counting vowels from scratch for every substring, maintain a **Sliding Window**.

When the window moves:

- One character leaves the window.
- One character enters the window.

Update the vowel count accordingly.

---

# Approach

1. Count the vowels in the first window of length `k`.
2. Store this as the current maximum.
3. Slide the window one position at a time.
4. For every slide:
   - Add the new character if it is a vowel.
   - Remove the old character if it is a vowel.
   - Update the maximum vowel count.
5. Return the maximum count.

---

# Algorithm

### Step 1

Create a set of vowels.

```python
vowels = {'a','e','i','o','u'}
```

---

### Step 2

Count vowels in the first window.

```python
count = 0

for i in range(k):
    if s[i] in vowels:
        count += 1
```

---

### Step 3

Initialize the answer.

```python
max_count = count
```

---

### Step 4

Slide the window.

```python
for i in range(k, len(s)):
```

If the new character is a vowel:

```python
count += 1
```

If the old character leaving the window is a vowel:

```python
count -= 1
```

Update the answer.

---

# Code

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i-k] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count
```

---

# Dry Run

### Example

```text
s = "abciiidef"
k = 3
```

### First Window

```text
abc
```

```text
Vowels = 1
```

```text
count = 1
max_count = 1
```

---

### Slide 1

Remove:

```text
a
```

Add:

```text
i
```

Window:

```text
bci
```

```text
count = 1
```

---

### Slide 2

Remove:

```text
b
```

Add:

```text
i
```

Window:

```text
cii
```

```text
count = 2
max_count = 2
```

---

### Slide 3

Remove:

```text
c
```

Add:

```text
i
```

Window:

```text
iii
```

```text
count = 3
max_count = 3
```

Continue sliding until the end.

Final Answer:

```text
3
```

---

# Why Does This Work?

Every slide changes only **two characters**:

```text
Old Window

[a b c]

↓

New Window

[b c i]
```

Instead of recounting every vowel:

- Remove the character leaving the window.
- Add the character entering the window.

Thus, each slide takes **O(1)** time.

---

# Time Complexity

```text
O(n)
```

- First window: `O(k)`
- Sliding: `O(n-k)`

Overall:

```text
O(n)
```

---

# Space Complexity

```text
O(1)
```

The vowel set contains only five characters.

---

# Concepts Used

- Sliding Window
- Strings
- Hash Set

---

# Python Features Used

### Set Lookup

```python
if s[i] in vowels:
```

Set membership checking is **O(1)** on average.

---

### Sliding the Window

```python
if s[i] in vowels:
    count += 1

if s[i-k] in vowels:
    count -= 1
```

---

### Update Maximum

```python
max_count = max(max_count, count)
```

---

# Key Takeaways

- This is a **Fixed Size Sliding Window** problem.
- The window size is always exactly `k`.
- Count vowels in the first window.
- For every slide:
  - Add the new character.
  - Remove the old character.
- Never recount the entire window.
- Runs in **O(n)** time with **O(1)** extra space.

---

## Author

**Ramit Sarker**
