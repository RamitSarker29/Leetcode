# 438. Find All Anagrams in a String

## Problem

Given two strings `s` and `p`, return all starting indices in `s` where a substring is an anagram of `p`.

An **anagram** is a rearrangement of characters that contains exactly the same characters with the same frequencies.

For example:
- `"abc"` and `"cba"` are anagrams.
- `"ab"` and `"ba"` are anagrams.
- `"aab"` and `"abb"` are not anagrams because their character frequencies differ.

We need to find every substring of `s` whose length is equal to `len(p)` and whose character frequencies match `p`.

## Examples

**Example 1:**

```python
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
```

Explanation:
- `"cba"` starting at index `0` is an anagram of `"abc"`.
- `"bac"` starting at index `6` is an anagram of `"abc"`.

**Example 2:**

```python
Input: s = "abab", p = "ab"
Output: [0, 1, 2]
```

Explanation:
- `"ab"` starting at index `0`.
- `"ba"` starting at index `1`.
- `"ab"` starting at index `2`.

All three substrings are anagrams of `"ab"`.

## Approach: Fixed-Size Sliding Window + Frequency Arrays

Instead of using dictionaries to store character frequencies, we use two arrays of size `26`.

Why 26?

Because the problem guarantees that both strings contain only lowercase English letters (`a` to `z`).

We can directly map each character to an array index using:

```python
index = ord(character) - ord('a')
```

For example:

| Character | Array Index |
|---|---:|
| `a` | 0 |
| `b` | 1 |
| `c` | 2 |
| `d` | 3 |
| `z` | 25 |

We use:
- `pHashMap` to store the frequency of characters in `p`.
- `sHashMap` to store the frequency of characters in the current window of `s`.
- `res` to store the starting indices of anagrams.

### 1. Handle the edge case

```python
if len(s) < len(p):
    return []
```

If `s` is shorter than `p`, it is impossible to find an anagram.

### 2. Initialize the frequency arrays

```python
pHashMap = [0] * 26
sHashMap = [0] * 26
res = []
```

Both arrays contain 26 zeros initially.

Each position represents one lowercase English letter.

### 3. Build the frequency array of p

```python
for i in range(len(p)):
    index = ord(p[i]) - ord('a')
    pHashMap[index] += 1
```

We traverse `p` and calculate the corresponding index for each character.

For example, if:

```python
p = "abc"
```

The frequency array becomes:

```python
pHashMap = [1, 1, 1, 0, 0, ..., 0]
```

This means:
- `a` appears once.
- `b` appears once.
- `c` appears once.
- All other characters appear zero times.

### 4. Build the initial window

```python
for i in range(len(p)):
    index = ord(s[i]) - ord('a')
    sHashMap[index] += 1
```

We take the first `len(p)` characters of `s` and calculate their frequencies.

For:

```python
s = "cbaebabacd"
p = "abc"
```

The initial window is:

```python
"cba"
```

Its frequency array is:

```python
sHashMap = [1, 1, 1, 0, 0, ..., 0]
```

Now compare both arrays:

```python
if sHashMap == pHashMap:
    res.append(0)
```

If both arrays are equal, the initial window is an anagram.

Since this window starts at index `0`, we add `0` to the result.

### 5. Initialize the two pointers

```python
i = 0
j = len(p)
```

Here:
- `i` points to the character leaving the current window.
- `j` points to the next character entering the window.

For our example:

```python
s = "cbaebabacd"
p = "abc"
```

Initially:

```text
Window: cba
        ^
        i = 0

Next character: e
                ^
                j = 3
```

The window size is always equal to `len(p)`.

### 6. Slide the window

```python
while j < len(s):
```

We continue while `j` is a valid index in `s`.

**Remove the outgoing character:**

```python
index = ord(s[i]) - ord('a')
sHashMap[index] -= 1
```

We calculate the index of the character at position `i` and decrease its frequency because it is leaving the window.

**Add the incoming character:**

```python
index = ord(s[j]) - ord('a')
sHashMap[index] += 1
```

We calculate the index of the next character and increase its frequency because it is entering the window.

**Move both pointers:**

```python
i += 1
j += 1
```

Both pointers move one position forward.

The window has now shifted one position to the right.

**Compare the frequency arrays:**

```python
if sHashMap == pHashMap:
    res.append(i)
```

If both arrays match, the current window is an anagram.

We append `i` because it now represents the starting index of the current window.

## Code

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        pHashMap = [0] * 26
        sHashMap = [0] * 26
        res = []

        for i in range(len(p)):
            index = ord(p[i]) - ord('a')
            pHashMap[index] += 1

        for i in range(len(p)):
            index = ord(s[i]) - ord('a')
            sHashMap[index] += 1

        if sHashMap == pHashMap:
            res.append(0)

        i = 0
        j = len(p)

        while j < len(s):
            index = ord(s[i]) - ord('a')
            sHashMap[index] -= 1

            index = ord(s[j]) - ord('a')
            sHashMap[index] += 1

            i += 1
            j += 1

            if sHashMap == pHashMap:
                res.append(i)

        return res
```

## Dry Run

Consider:

```python
s = "cbaebabacd"
p = "abc"
```

### Step 1: Build pHashMap

```python
pHashMap = [1, 1, 1, 0, ..., 0]
```

The characters `a`, `b`, and `c` each appear once.

### Step 2: Build the initial window

The first three characters of `s` are `"cba"`.

```python
sHashMap = [1, 1, 1, 0, ..., 0]
```

Both arrays are equal.

```python
res = [0]
```

### Step 3: Start sliding the window

Initially:

```python
i = 0
j = 3
```

The current window is `"cba"`.

| Iteration | Outgoing character | Incoming character | New window | Anagram? |
|---|---|---|---|---|
| Initial | — | — | `cba` | Yes |
| 1 | `c` | `e` | `bae` | No |
| 2 | `b` | `b` | `aeb` | No |
| 3 | `a` | `a` | `eba` | No |
| 4 | `e` | `b` | `bab` | No |
| 5 | `b` | `a` | `aba` | No |
| 6 | `a` | `c` | `bac` | Yes |
| 7 | `b` | `d` | `acd` | No |

When the window becomes `"bac"`, its frequency array matches `pHashMap`.

Its starting index is `6`, so:

```python
res = [0, 6]
```

**Final Output:**

```python
[0, 6]
```

## Why Does It Work?

Anagrams contain exactly the same characters with exactly the same frequencies.

Our algorithm uses two frequency arrays to compare the characters of `p` with each window of `s`.

The important part is that we do not rebuild the frequency array for every substring.

Instead, we update the existing array:
1. Decrease the frequency of the outgoing character.
2. Increase the frequency of the incoming character.
3. Move the window forward.
4. Compare the updated frequency array with `pHashMap`.

Since the window always has the same length as `p`, every possible candidate substring is checked.

Whenever the arrays match, we know that the current window is an anagram.

## Algorithm

1. If `len(s) < len(p)`, return an empty list.
2. Create two arrays of size 26, initialized with zeros.
3. Build the frequency array of `p`.
4. Build the frequency array of the first window of `s`.
5. Compare both arrays. If they match, add index `0`.
6. Initialize `i = 0` and `j = len(p)`.
7. While `j` is less than `len(s)`:
   - Decrease the frequency of `s[i]`.
   - Increase the frequency of `s[j]`.
   - Increment both pointers.
   - Compare the frequency arrays.
   - If they match, add `i` to the result.
8. Return the result.

## Complexity Analysis

Let:
- `n` = length of `s`
- `m` = length of `p`

**Time Complexity: O(n + m)**

- Building the frequency array of `p` takes O(m).
- Building the initial window takes O(m).
- Sliding the window takes O(n - m) iterations.
- Comparing two arrays takes O(26), which is constant.

Therefore, the overall time complexity is **O(n + m)**.

**Space Complexity: O(1)**

We use two arrays of fixed size 26.

Their sizes do not depend on the input length, so the auxiliary space complexity is O(1).

The result list is excluded from auxiliary space complexity.

## Concepts Used

- Fixed-Size Sliding Window
- Two Pointers
- Frequency Counting
- Arrays
- Character-to-Index Mapping

## Python Features Used

- `ord()` to convert a character into its Unicode code point.
- `[0] * 26` to initialize a frequency array.
- `range()` to iterate over string indices.
- List equality (`==`) to compare character frequencies.

## Key Takeaways

- Anagrams can be identified using character frequencies.
- Since the input contains only lowercase English letters, a 26-element array is sufficient.
- `ord(char) - ord('a')` maps each lowercase letter to an index from `0` to `25`.
- A sliding window lets us update frequencies without recounting the entire substring.
- Removing the outgoing character and adding the incoming character keeps the window size fixed.
- This approach achieves O(n + m) time and O(1) auxiliary space.

## Author

**Ramit Sarker**
