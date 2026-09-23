# 14. Longest Common Prefix

## Problem

Given an array of strings, find the **longest common prefix** shared by all strings.

A **prefix** is a sequence of characters that appears at the beginning of a string.

If there is no common prefix, return an empty string `""`.

### Example 1

```text
Input:  strs = ["flower", "flow", "flight"]
Output: "fl"
```

### Example 2

```text
Input:  strs = ["dog", "racecar", "car"]
Output: ""
```

There is no common prefix among the strings.

---

# Approach

The idea is to start with the **first string as the current prefix**.

Then compare this prefix with every other string.

If the current string does **not** start with the current prefix, keep removing characters from the end of the prefix until it becomes a valid prefix of the current string.

### Main Idea

```text
current_prefix = first string

For every other string:
    If it doesn't start with current_prefix:
        Remove the last character from current_prefix
        Check again

Return current_prefix
```

For example:

```text
["flower", "flow", "flight"]

Start:
current_prefix = "flower"

Compare with "flow":

"flow".startswith("flower") → False

Remove characters:
"flowe"
"flow"
```

Now:

```text
"flow".startswith("flow") → True
```

So:

```text
current_prefix = "flow"
```

Next compare with `"flight"`:

```text
"flight".startswith("flow") → False
```

Keep shortening:

```text
"flo"  → False
"fl"   → True
```

Therefore:

```text
Answer = "fl"
```

---

# Code

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current_prefix = strs[0]
        j = len(current_prefix) - 1

        for i in range(1, len(strs)):
            while strs[i].startswith(current_prefix) != True:
                j -= 1
                current_prefix = current_prefix[: j + 1]

        return current_prefix
```

---

# Code Explanation

### 1. Start with the first string

```python
current_prefix = strs[0]
```

We initially assume that the entire first string is the common prefix.

For:

```python
["flower", "flow", "flight"]
```

we get:

```text
current_prefix = "flower"
```

---

### 2. Set the index `j`

```python
j = len(current_prefix) - 1
```

`j` represents the last index of the current prefix.

For `"flower"`:

```text
f l o w e r
0 1 2 3 4 5
          ↑
          j = 5
```

---

### 3. Compare with every other string

```python
for i in range(1, len(strs)):
```

We start from index `1` because `strs[0]` is already being used as the initial prefix.

For:

```python
["flower", "flow", "flight"]
```

the loop compares:

```text
"flower" → initial prefix
"flow"   → first comparison
"flight" → second comparison
```

---

### 4. Check whether the string starts with the prefix

```python
while strs[i].startswith(current_prefix) != True:
```

Python's `startswith()` checks whether a string begins with another string.

For example:

```python
"flow".startswith("flower")
```

returns:

```text
False
```

But:

```python
"flow".startswith("flow")
```

returns:

```text
True
```

---

### 5. Remove the last character

If the current prefix doesn't match:

```python
j -= 1
```

Then:

```python
current_prefix = current_prefix[: j + 1]
```

The slicing keeps everything from the beginning up to index `j`.

For example:

```text
current_prefix = "flower"
j = 5
```

After:

```python
j -= 1
```

we get:

```text
j = 4
```

Then:

```python
current_prefix[:5]
```

gives:

```text
"flowe"
```

So the prefix becomes shorter by one character.

---

# Dry Run

Consider:

```python
strs = ["flower", "flow", "flight"]
```

### Initial State

```text
current_prefix = "flower"
j = 5
```

---

### Compare `"flow"`

Check:

```text
"flow".startswith("flower")
```

Result:

```text
False
```

Shorten prefix:

```text
"flower" → "flowe"
```

Check:

```text
"flow".startswith("flowe")
```

Result:

```text
False
```

Shorten again:

```text
"flowe" → "flow"
```

Check:

```text
"flow".startswith("flow")
```

Result:

```text
True
```

So now:

```text
current_prefix = "flow"
```

---

### Compare `"flight"`

Check:

```text
"flight".startswith("flow")
```

Result:

```text
False
```

Shorten:

```text
"flow" → "flo"
```

Check:

```text
"flight".startswith("flo")
```

Result:

```text
False
```

Shorten:

```text
"flo" → "fl"
```

Check:

```text
"flight".startswith("fl")
```

Result:

```text
True
```

Therefore:

```text
current_prefix = "fl"
```

---

### Final Answer

```text
"fl"
```

---

# Another Dry Run

Consider:

```python
strs = ["dog", "racecar", "car"]
```

Initial:

```text
current_prefix = "dog"
```

Compare with `"racecar"`:

```text
"racecar".startswith("dog") → False
```

Shorten:

```text
"dog" → "do"
"do"  → "d"
"d"   → ""
```

Eventually:

```text
"racecar".startswith("") → True
```

So:

```text
current_prefix = ""
```

Once the common prefix becomes empty, there cannot be any common characters among all strings.

Final answer:

```text
""
```

---

# Why Does It Work?

The first string contains every possible character that could be part of the common prefix.

We start by assuming the entire first string is the prefix.

For every other string, we verify whether it begins with that prefix.

If it doesn't, the prefix is too long, so we remove characters from the end.

We continue until:

```python
strs[i].startswith(current_prefix)
```

becomes `True`.

After processing every string, `current_prefix` is a prefix shared by all strings.

Because we only remove characters from the end, we always preserve the prefix property.

Therefore, the final `current_prefix` is the **longest common prefix**.

---

# Algorithm

1. Set `current_prefix` to the first string.
2. Set `j` to the last index of the prefix.
3. Traverse every remaining string.
4. Check whether the current string starts with `current_prefix`.
5. If not:
   - Decrease `j`.
   - Shorten `current_prefix`.
   - Check again.
6. Continue until the current string starts with the prefix.
7. After all strings are processed, return `current_prefix`.

---

# Complexity Analysis

Let:

- `n` = number of strings
- `m` = length of the strings

### Time Complexity

```text
O(n × m)
```

In the worst case, we may compare and shorten the prefix across the strings.

### Space Complexity

```text
O(m)
```

because `current_prefix` is stored as a string.

The algorithm itself does not use any additional data structure.

---

# Important Python Concepts Used

### `startswith()`

```python
strs[i].startswith(current_prefix)
```

Checks whether a string begins with another string.

Example:

```python
"flower".startswith("flow")
```

Output:

```text
True
```

---

### String Slicing

```python
current_prefix[:j + 1]
```

Creates a substring from the beginning up to index `j`.

Example:

```python
s = "flower"

s[:4]
```

gives:

```text
"flow"
```

---

### `range()`

```python
range(1, len(strs))
```

Starts the loop from the second string because the first string is already being used as the initial prefix.

---

# Key Takeaways

- Start with the first string as the candidate prefix.
- Compare the candidate prefix with every other string.
- If it doesn't match, shorten it from the right.
- `startswith()` makes checking the prefix straightforward.
- String slicing is used to remove characters from the end.
- If the prefix becomes `""`, there is no common prefix.
- The final `current_prefix` is the longest prefix shared by every string.

---

# Author

**Ramit Sarker**
