# 242. Valid Anagram

## Problem

Given two strings `s` and `t`, determine whether `t` is an **anagram** of `s`.

An anagram is a word or string formed by rearranging the characters of another string, using every character the same number of times.

For example:

```text
s = "anagram"
t = "nagaram"
```

Both strings contain the same characters with the same frequencies, so the answer is `True`.

If the character frequencies differ, return `False`.

---

# Examples

## Example 1

```text
Input:  s = "anagram", t = "nagaram"
Output: True
```

Both strings contain:

```text
a → 3 times
n → 1 time
g → 1 time
r → 1 time
m → 1 time
```

Therefore, `t` is an anagram of `s`.

## Example 2

```text
Input:  s = "rat", t = "car"
Output: False
```

The character frequencies are different:

```text
s = "rat"
t = "car"
```

- `s` contains `r`, `a`, and `t`.
- `t` contains `c`, `a`, and `r`.

The character `t` is missing from the second string, and `c` is an extra character.

Therefore, the answer is `False`.

---

# Approach

Your solution uses a **hash map (dictionary)** to count the frequency of each character.

The algorithm works in three stages:

1. Check whether both strings have the same length.
2. Count the characters in `s`.
3. Traverse `t` and decrease the corresponding character counts.

If a character from `t` does not exist in the dictionary, return `False`.

Whenever a character's frequency reaches zero, remove it from the dictionary.

At the end, if the dictionary is empty, both strings contain exactly the same characters with the same frequencies.

---

# Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hash_map:
                hash_map[t[i]] -= 1
                if hash_map[t[i]] == 0:
                    del hash_map[t[i]]
            else:
                return False

        if len(hash_map) == 0:
            return True
```

---

# Code Explanation

## 1. Check the Lengths

```python
if len(s) != len(t):
    return False
```

Two strings cannot be anagrams if they have different lengths.

For example:

```text
s = "cat"    → length = 3
t = "cats"   → length = 4
```

Since the lengths are different, the function immediately returns `False`.

This also avoids unnecessary work.

---

## 2. Create a Hash Map

```python
hash_map = {}
```

The dictionary stores each character as a key and its frequency as the value.

For example:

```text
s = "aabbc"
```

The dictionary will eventually become:

```python
{
    'a': 2,
    'b': 2,
    'c': 1
}
```

---

## 3. Count the Characters in `s`

```python
for i in range(len(s)):
    if s[i] in hash_map:
        hash_map[s[i]] += 1
    else:
        hash_map[s[i]] = 1
```

We traverse every character of `s`.

### If the character already exists

```python
if s[i] in hash_map:
    hash_map[s[i]] += 1
```

Increase its frequency by one.

For example, if:

```text
hash_map = {'a': 1}
```

and the next character is `'a'`, the dictionary becomes:

```text
hash_map = {'a': 2}
```

### If the character is new

```python
else:
    hash_map[s[i]] = 1
```

Add it to the dictionary with a frequency of `1`.

For example:

```text
hash_map = {}
```

After encountering `'a'`:

```text
hash_map = {'a': 1}
```

---

# 4. Traverse the Second String

```python
for i in range(len(t)):
```

Now we check whether the characters in `t` match the frequencies stored from `s`.

---

## 5. Check Whether the Character Exists

```python
if t[i] in hash_map:
```

If the character exists in the dictionary, it means that `s` still has an available occurrence of that character.

For example:

```text
hash_map = {'a': 2, 'n': 1}
```

If the current character is `'a'`, it exists in the dictionary, so we can use one occurrence.

But if the current character is `'z'`, it is absent, meaning `t` contains a character that cannot be matched with the remaining characters of `s`.

In that case:

```python
else:
    return False
```

---

## 6. Decrease the Character Frequency

```python
hash_map[t[i]] -= 1
```

Every time we encounter a character in `t`, we consume one occurrence of that character from the frequency count.

For example:

```text
Before:
hash_map = {'a': 3}

After encountering 'a':
hash_map = {'a': 2}
```

This ensures that each character in `t` is matched against a corresponding occurrence in `s`.

---

## 7. Delete Characters Whose Frequency Becomes Zero

```python
if hash_map[t[i]] == 0:
    del hash_map[t[i]]
```

Once a character has been used the required number of times, it no longer needs to remain in the dictionary.

For example:

```text
Before:
hash_map = {'a': 1, 'b': 2}
```

After processing `'a'`:

```text
hash_map = {'a': 0, 'b': 2}
```

Since the frequency of `'a'` is zero, it is deleted:

```text
hash_map = {'b': 2}
```

This means that all required occurrences of `'a'` have been matched.

---

## 8. Check Whether the Dictionary Is Empty

```python
if len(hash_map) == 0:
    return True
```

If the dictionary is empty, every character count from `s` has been matched by `t`.

Therefore, both strings are anagrams.

If the dictionary is not empty, some required character occurrences remain unmatched.

Under the equal-length check and the frequency logic in this solution, a non-empty dictionary at the end indicates that the strings are not anagrams.

---

# Dry Run

Consider:

```python
s = "anagram"
t = "nagaram"
```

## Step 1: Check Lengths

```text
len(s) = 7
len(t) = 7
```

The lengths are equal, so continue.

## Step 2: Build the Hash Map From `s`

Process each character of `"anagram"`:

| Character | Hash map after processing |
|---|---|
| `a` | `{'a': 1}` |
| `n` | `{'a': 1, 'n': 1}` |
| `a` | `{'a': 2, 'n': 1}` |
| `g` | `{'a': 2, 'n': 1, 'g': 1}` |
| `r` | `{'a': 2, 'n': 1, 'g': 1, 'r': 1}` |
| `a` | `{'a': 3, 'n': 1, 'g': 1, 'r': 1}` |
| `m` | `{'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}` |

Final dictionary:

```python
{
    'a': 3,
    'n': 1,
    'g': 1,
    'r': 1,
    'm': 1
}
```

## Step 3: Process `t = "nagaram"`

Now decrease the frequency of each character in `t`.

| Character | Operation | Remaining dictionary |
|---|---|---|
| `n` | `n: 1 → 0`, delete `n` | `{'a': 3, 'g': 1, 'r': 1, 'm': 1}` |
| `a` | `a: 3 → 2` | `{'a': 2, 'g': 1, 'r': 1, 'm': 1}` |
| `g` | `g: 1 → 0`, delete `g` | `{'a': 2, 'r': 1, 'm': 1}` |
| `a` | `a: 2 → 1` | `{'a': 1, 'r': 1, 'm': 1}` |
| `r` | `r: 1 → 0`, delete `r` | `{'a': 1, 'm': 1}` |
| `a` | `a: 1 → 0`, delete `a` | `{'m': 1}` |
| `m` | `m: 1 → 0`, delete `m` | `{}` |

The dictionary is empty.

Therefore:

```text
Output: True
```

---

# Another Dry Run

Consider:

```python
s = "rat"
t = "car"
```

### Step 1: Check Lengths

```text
len(s) = 3
len(t) = 3
```

Continue.

### Step 2: Build the Hash Map

After processing `"rat"`:

```python
{
    'r': 1,
    'a': 1,
    't': 1
}
```

### Step 3: Process `"car"`

The first character is `'c'`.

```python
if 'c' in hash_map:
```

This condition is `False` because `'c'` is not in the dictionary.

The function executes:

```python
return False
```

Final answer:

```text
Output: False
```

The algorithm stops immediately without processing the remaining characters.

---

# Why Does It Work?

The dictionary represents the remaining character frequencies needed to match `s`.

Initially, every character in `s` contributes to its frequency count.

As we process `t`, each matching character decreases its count by one.

- If a character in `t` is not present in the dictionary, `t` contains an unmatched character, so the strings cannot be anagrams.
- If a character's count becomes zero, all its required occurrences have been matched, so the key is removed.
- If all characters are matched, the dictionary becomes empty.

The initial length check ensures both strings contain the same total number of characters.

Thus, the algorithm correctly determines whether the two strings are anagrams.

---

# Algorithm

1. Compare the lengths of `s` and `t`.
2. If the lengths differ, return `False`.
3. Create an empty dictionary `hash_map`.
4. Traverse `s` and count the frequency of each character.
5. Traverse `t`:
   - If the character does not exist in `hash_map`, return `False`.
   - Otherwise, decrease its frequency.
   - If the frequency becomes zero, delete the character from the dictionary.
6. If the dictionary is empty, return `True`.

---

# Complexity Analysis

Let `n` be the length of `s` and `t`.

### Time Complexity

The first loop traverses `s` once:

```text
O(n)
```

The second loop traverses `t` once:

```text
O(n)
```

Dictionary lookup, insertion, and deletion take average `O(1)` time per operation.

Therefore:

```text
O(n) + O(n) = O(n)
```

**Time Complexity: `O(n)` average**

### Space Complexity

In the worst case, the dictionary stores every distinct character in `s`.

Therefore, for an alphabet of size \(k\), the auxiliary space is:

```text
O(k)
```

Since the problem restricts the strings to lowercase English letters, there are at most 26 distinct characters.

**Space Complexity: `O(1)`** under the given constraints.

For arbitrary Unicode input, the dictionary could contain up to \(O(n)\) distinct characters, giving `O(n)` auxiliary space.

---

# Follow-Up: What If the Strings Contain Unicode Characters?

Your dictionary approach can already handle Unicode characters because Python strings and dictionaries support Unicode.

For example:

```python
s = "café"
t = "éfac"
```

The same frequency-counting logic can work without restricting characters to lowercase English letters.

If the strings contain canonically equivalent Unicode characters represented differently, such as a precomposed accented character versus a base character followed by a combining accent, normalize both strings first using Python's `unicodedata.normalize()`.

For example:

```python
import unicodedata

s = unicodedata.normalize("NFC", s)
t = unicodedata.normalize("NFC", t)
```

Then apply the frequency-counting algorithm.

---

# Concepts Used

- Hash maps / dictionaries
- Character frequency counting
- String traversal
- Membership testing
- Conditional statements
- Dictionary insertion and deletion
- Early return
- Time-space complexity

---

# Python Features Used

### `len()`

```python
if len(s) != len(t):
```

Checks whether both strings have the same length.

### Dictionary Membership

```python
if s[i] in hash_map:
```

Checks whether a character already exists as a key.

### Frequency Counting

```python
hash_map[s[i]] += 1
```

Increases the count of a character.

### Decrementing Counts

```python
hash_map[t[i]] -= 1
```

Consumes one occurrence of a character.

### Dictionary Deletion

```python
del hash_map[t[i]]
```

Removes a character once its required frequency reaches zero.

---

# Key Takeaways

- Anagrams must have the same characters with the same frequencies.
- Equal string lengths are necessary but not sufficient.
- A dictionary efficiently tracks character frequencies.
- The first pass counts characters in `s`.
- The second pass consumes those counts using `t`.
- An unexpected character causes an immediate `False`.
- An empty dictionary at the end means every character has been matched.
- The solution runs in **O(n) average time** and uses **O(1) auxiliary space** for lowercase English letters.

---

# Author

**Ramit Sarker**
