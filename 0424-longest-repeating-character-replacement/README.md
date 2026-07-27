# 424. Longest Repeating Character Replacement

## Problem

You are given a string `s` consisting of uppercase English letters and an integer `k`.

You can replace **at most `k` characters** with any uppercase English letter.

Return the **length of the longest substring** that can be made of the **same character** after performing at most `k` replacements.

---

## Examples

### Example 1

**Input:**
```text
s = "ABAB", k = 2
```

**Output:**
```text
4
```

**Explanation:**

Replace the two `A`s with `B`s (or vice versa).

```
ABAB → BBBB
```

The longest repeating substring has length **4**.

---

### Example 2

**Input:**
```text
s = "AABABBA", k = 1
```

**Output:**
```text
4
```

**Explanation:**

Replace one `A` with `B`.

```
AABABBA → AABBBBA
```

The longest repeating substring is:

```
BBBB
```

Length = **4**

---

# Approach

We solve this problem using the **Sliding Window** technique.

### Observation

For every window,

```
Replacements Needed = Window Size − Frequency of Most Frequent Character
```

If the replacements needed exceed `k`, the window is invalid and must be shrunk.

### Algorithm

1. Expand the window by moving the right pointer.
2. Store the frequency of every character in a hash map.
3. Maintain the highest frequency (`max_freq`) seen so far.
4. If

```
(window size - max_freq) > k
```

shrink the window from the left.
5. After the window becomes valid, update the maximum window length.

---

## Why don't we decrease `max_freq`?

Unlike most sliding window problems, we **never decrease** `max_freq`.

- Updating it after every shrink would require scanning the hash map repeatedly.
- A stale `max_freq` may temporarily treat an invalid window as valid.
- As the window expands, the condition eventually becomes invalid and the left pointer catches up.
- This optimization keeps the solution **O(n)** while still producing the correct answer.

---

# Code

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        hash_map = {}
        max_freq = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] += 1
            else:
                hash_map[s[j]] = 1

            max_freq = max(max_freq, hash_map[s[j]])

            while (j - i + 1 - max_freq) > k:
                hash_map[s[i]] -= 1
                if hash_map[s[i]] == 0:
                    del hash_map[s[i]]
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len
```

---

# Dry Run

### Input

```text
s = "AABABBA"
k = 1
```

| Step | Window | Frequency | max_freq | Action | max_len |
|------|--------|-----------|---------:|--------|---------:|
| 1 | A | A:1 | 1 | Valid | 1 |
| 2 | AA | A:2 | 2 | Valid | 2 |
| 3 | AAB | A:2, B:1 | 2 | Valid | 3 |
| 4 | AABA | A:3, B:1 | 3 | Valid | 4 |
| 5 | AABAB | A:3, B:2 | 3 | Shrink | 4 |
| 6 | ABABB | A:2, B:3 | 3 | Valid | 4 |
| 7 | BABBA | A:2, B:3 | 3 | Valid | 4 |

**Final Answer**

```text
4
```

---

# Time Complexity

- Each character enters the window once.
- Each character leaves the window once.

**Time Complexity:** `O(n)`

---

# Space Complexity

The hash map stores frequencies of at most **26 uppercase English letters**.

**Space Complexity:** `O(1)`

---

# Concepts Used

- Sliding Window
- Two Pointers
- Hash Map
- Frequency Counting
- Greedy

---

# Python Features Used

- Dictionary
- `in`
- `del`
- `max()`
- `range()`

---

# Key Takeaways

- Expand the window by moving the right pointer.
- Keep track of character frequencies.
- Maintain the highest frequency using `max_freq`.
- Shrink only when:

```
(window size - max_freq) > k
```

- **Never decrease `max_freq`.**
- Update the answer only after the window becomes valid again.

---

## Author

**Ramit Sarker**
