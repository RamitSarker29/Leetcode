# 424. Longest Repeating Character Replacement

## Problem

You are given a string `s` consisting of uppercase English letters and an integer `k`.

You can replace **at most `k` characters** with any uppercase letter.

Return the **length of the longest substring** that can be made of the **same character** after performing at most `k` replacements.

---

## Examples

### Example 1

```text
Input:
s = "ABAB"
k = 2

Output:
4
```

**Explanation**

Replace the two `A`s with `B`s (or vice versa).

```
ABAB → BBBB
```

Length = **4**

---

### Example 2

```text
Input:
s = "AABABBA"
k = 1

Output:
4
```

**Explanation**

Replace one `A` with `B`.

```
AABABBA → AABBBBA
```

The longest substring with the same character is:

```
BBBB
```

Length = **4**

---

# Approach (Sliding Window)

We use the **Sliding Window** technique.

### Observation

For any window,

```
Replacements Needed =
Window Size − Frequency of Most Common Character
```

If the replacements needed are greater than `k`, the window is invalid and must be shrunk.

---

### Steps

1. Expand the window by moving `j`.
2. Store the frequency of every character in a hash map.
3. Maintain the highest frequency (`max_freq`) seen in the current traversal.
4. If

```text
(window size - max_freq) > k
```

shrink the window from the left.
5. Update the maximum valid window length.

---

## Why don't we decrease `max_freq`?

`max_freq` is allowed to become **stale**.

When shrinking the window, we **do not recompute** the maximum frequency.

Why?

* Recomputing every time would require scanning the hash map repeatedly.
* A stale `max_freq` may temporarily make an invalid window appear valid.
* As the window keeps expanding, the condition eventually becomes invalid and the left pointer catches up.
* This optimization keeps the algorithm **O(n)** while still producing the correct answer.

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

| Step  | Window  | Frequency | max_freq | Valid? | max_len |
| ----- | ------- | --------- | -------: | :----: | ------: |
| A     | A       | A:1       |        1 |    ✅   |       1 |
| AA    | AA      | A:2       |        2 |    ✅   |       2 |
| AAB   | AAB     | A:2 B:1   |        2 |    ✅   |       3 |
| AABA  | A:3 B:1 | 3         |        ✅ |    4   |         |
| AABAB | A:3 B:2 | 3         | ❌ Shrink |    4   |         |
| ABABB | A:2 B:3 | 3         |        ✅ |    4   |         |
| BABBA | A:2 B:3 | 3         |        ✅ |    4   |         |

Final Answer:

```text
4
```

---

# Time Complexity

* Each character enters the window once.
* Each character leaves the window once.

**Time Complexity:** `O(n)`

---

# Space Complexity

The hash map stores frequencies of uppercase English letters only.

Maximum distinct characters = **26**

**Space Complexity:** `O(1)`

---

# Concepts Used

* Sliding Window
* Hash Map (Dictionary)
* Two Pointers
* Frequency Counting
* Greedy Observation

---

# Python Features Used

* Dictionary
* `in`
* `del`
* `max()`
* `range()`

---

# Key Takeaways

* Expand the window one character at a time.
* Store character frequencies in a hash map.
* A window is valid when:

```text
(window size - max_freq) <= k
```

* Shrink only when the window becomes invalid.
* **Do not decrease `max_freq`** while shrinking; allowing it to be stale is the optimization that makes the solution linear.
* Update the answer only after the window is valid again.

---

## Author

**Ramit Sarker**
