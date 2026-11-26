# 76. Minimum Window Substring

## Problem

Given two strings `s` and `t`, find the **smallest substring of `s` that contains every character of `t`, including duplicate characters**.

If no such substring exists, return an empty string `""`.

An important point: character frequency matters.

For example, if:

```python
s = "ADOBECODEBANC"
t = "ABC"
```

The answer is `"BANC"` because it contains all three required characters.

If:

```python
s = "a"
t = "aa"
```

The answer is `""` because `t` requires two occurrences of `a`, but `s` contains only one.

## Examples

**Example 1:**

```python
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2:**

```python
Input: s = "a", t = "a"
Output: "a"
```

**Example 3:**

```python
Input: s = "a", t = "aa"
Output: ""
```

## Approach: Variable-Size Sliding Window + Hash Maps

This problem uses a **variable-size sliding window**.

Unlike fixed-size sliding window problems, where the window length stays constant, here we expand and shrink the window depending on whether it contains all the required characters.

We use two hash maps:

- `tHashMap`: Stores the frequency of every character required from `t`.
- `sHashMap`: Stores the frequency of characters currently inside our window in `s`.

We also use four important variables:

| Variable | Purpose |
|---|---|
| `have` | Number of required characters whose frequency is currently satisfied |
| `required` | Number of distinct characters required from `t` |
| `minLen` | Length of the smallest valid window found |
| `start` | Starting index of the smallest valid window |

### 1. Initialize the variables

```python
tHashMap = {}
sHashMap = {}
have = 0
required = len(set(t))
minLen = float('inf')
start = 0
```

Let's understand the important variables.

**`required = len(set(t))`**

We use `set(t)` to find the number of distinct characters in `t`.

For example:

```python
t = "AABC"

set(t) = {'A', 'B', 'C'}

required = 3
```

Even though `A` appears twice, it is counted as one distinct character.

**`have = 0`**

Initially, we haven't satisfied the frequency requirement of any character.

**`minLen = float('inf')`**

We initialize the minimum length with infinity so that the first valid window will always be smaller.

**`start = 0`**

This stores the starting index of the best window.

### 2. Build the frequency map of t

```python
for i in range(len(t)):
    if t[i] in tHashMap:
        tHashMap[t[i]] += 1
    else:
        tHashMap[t[i]] = 1
```

We count how many times each character appears in `t`.

For:

```python
t = "ABC"
```

The frequency map becomes:

```python
tHashMap = {
    'A': 1,
    'B': 1,
    'C': 1
}
```

For a string containing duplicates:

```python
t = "AABC"
```

The frequency map would be:

```python
tHashMap = {
    'A': 2,
    'B': 1,
    'C': 1
}
```

This is important because the problem requires us to include duplicate characters too.

### 3. Initialize the two pointers

```python
i, j = 0, 0
```

We use two pointers to represent the current window.

- `i` represents the starting index.
- `j` represents the ending boundary of the window.

Our window is represented by:

```python
s[i:j]
```

Notice that `j` is exclusive, meaning the character at index `j` is not yet included.

### 4. Expand the window

```python
while j < len(s):
    sHashMap[s[j]] = sHashMap.get(s[j], 0) + 1
```

We expand the window by adding the character at index `j`.

The expression:

```python
sHashMap.get(s[j], 0) + 1
```

means:
- If the character already exists, get its current frequency.
- Otherwise, use `0`.
- Increase the frequency by one.

Now we check whether the newly added character satisfies its required frequency.

```python
if s[j] in tHashMap and sHashMap[s[j]] == tHashMap[s[j]]:
    have += 1
```

This is the most important condition in the solution.

We increase `have` only when:

1. The character exists in `tHashMap`.
2. Its frequency in the current window becomes exactly equal to its required frequency.

For example:

```python
tHashMap = {'A': 1, 'B': 1, 'C': 1}
```

If the current window gets its first `A`:

```python
sHashMap['A'] = 1
```

Since the required frequency is also `1`, we increment `have`.

But if another `A` enters:

```python
sHashMap['A'] = 2
```

We do not increment `have` again.

This is because `A` was already satisfied.

After processing the character, we move the right pointer:

```python
j += 1
```

### 5. Shrink the window

```python
while have == required:
```

This condition means that every distinct character required from `t` has reached its required frequency.

We now have a valid window.

But we don't stop here.

Our goal is to find the **minimum-length valid window**, so we try to shrink it from the left.

First, update the minimum window:

```python
if j - i < minLen:
    minLen = j - i
    start = i
```

Since `j` is exclusive, the current window length is:

```python
j - i
```

If the current window is smaller than the previously recorded minimum, we update:
- `minLen` with the new window length.
- `start` with the current starting index.

### 6. Remove the leftmost character

```python
if s[i] in tHashMap and sHashMap[s[i]] == tHashMap[s[i]]:
    have -= 1
```

Before removing the character, we check whether its current frequency is exactly equal to its required frequency.

If it is, removing that character will make its frequency insufficient.

Therefore, we decrease `have`.

For example:

```python
tHashMap = {'A': 1}
sHashMap = {'A': 1}
```

If we remove `A`, its frequency becomes zero.

Now the window no longer satisfies the requirement for `A`, so `have` must decrease.

Next:

```python
sHashMap[s[i]] -= 1
i += 1
```

We decrease the frequency of the outgoing character and move the left pointer forward.

The inner loop continues shrinking the window until it is no longer valid.

### 7. Return the minimum window

```python
return '' if minLen == float('inf') else s[start : start + minLen]
```

There are two possibilities:

- If `minLen` is still infinity, we never found a valid window, so return `""`.
- Otherwise, return the substring using the saved starting index and minimum length.

## Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tHashMap = {}
        sHashMap = {}
        have = 0
        required = len(set(t))
        minLen = float('inf')
        start = 0

        for i in range(len(t)):
            if t[i] in tHashMap:
                tHashMap[t[i]] += 1
            else:
                tHashMap[t[i]] = 1

        i, j = 0, 0

        while j < len(s):
            sHashMap[s[j]] = sHashMap.get(s[j], 0) + 1

            if s[j] in tHashMap and sHashMap[s[j]] == tHashMap[s[j]]:
                have += 1

            j += 1

            while have == required:
                if j - i < minLen:
                    minLen = j - i
                    start = i

                if s[i] in tHashMap and sHashMap[s[i]] == tHashMap[s[i]]:
                    have -= 1

                sHashMap[s[i]] -= 1
                i += 1

        return '' if minLen == float('inf') else s[start : start + minLen]
```

## Dry Run

Consider:

```python
s = "ADOBECODEBANC"
t = "ABC"
```

### Step 1: Build tHashMap

```python
tHashMap = {
    'A': 1,
    'B': 1,
    'C': 1
}
```

Therefore:

```python
required = 3
have = 0
```

### Step 2: Expand the window

We move `j` from left to right, adding characters to the window.

| Character added | Current window | `have` | Valid? |
|---|---|---:|---|
| A | `A` | 1 | No |
| D | `AD` | 1 | No |
| O | `ADO` | 1 | No |
| B | `ADOB` | 2 | No |
| E | `ADOBE` | 2 | No |
| C | `ADOBEC` | 3 | Yes |

Now all three required characters are present.

Our first valid window is:

```python
"ADOBEC"
```

Its length is `6`.

```python
minLen = 6
start = 0
```

### Step 3: Shrink the window

Now `have == required`, so we start moving `i` forward.

- Remove `A`: its frequency becomes insufficient, so `have` decreases to `2`.
- The window becomes invalid.

The current minimum remains:

```python
"ADOBEC"
```

### Step 4: Expand again

We continue moving `j` forward.

The characters `O`, `D`, `E`, `B`, `A` enter the window.

When `A` enters, all required characters are present again.

The current valid window is:

```python
"CODEBA"
```

Its length is `6`.

It is not smaller than our current minimum, so we don't update `minLen`.

### Step 5: Shrink again

We remove characters from the left:

- Remove `C`: the window becomes invalid.
- Continue expanding until another `C` enters.

The new valid window becomes:

```python
"BANC"
```

Its length is `4`.

Since:

```python
4 < 6
```

We update:

```python
minLen = 4
start = 9
```

There is no shorter valid window after this.

### Final Output

```python
s[start : start + minLen]

s[9:13]

"BANC"
```

```python
Output: "BANC"
```

## Why Does It Work?

The algorithm maintains two important conditions.

**1. The `have == required` condition guarantees validity.**

`required` counts the number of distinct characters in `t`.

`have` counts how many of those characters currently have at least their required frequency.

We increase `have` when a character's frequency reaches the required count.

We decrease it when removing a character makes its frequency insufficient.

Therefore, when:

```python
have == required
```

the current window contains every required character, including duplicates.

**2. Shrinking the window helps find the minimum length.**

Once a window becomes valid, we record its length and remove characters from the left.

We continue until the window becomes invalid.

This ensures that we explore smaller valid windows instead of checking only the first valid one.

By expanding and shrinking the window, we find the smallest valid substring without checking every possible substring.

## Algorithm

1. Create two dictionaries to store character frequencies.
2. Count the frequency of every character in `t`.
3. Initialize:
   - `have = 0`
   - `required = len(set(t))`
   - `minLen = infinity`
   - `start = 0`
4. Initialize two pointers `i = 0` and `j = 0`.
5. Expand the window by adding `s[j]`.
6. If the character's frequency reaches its required frequency, increment `have`.
7. Move `j` forward.
8. While `have == required`:
   - Update the minimum window if the current one is smaller.
   - Check whether removing `s[i]` will make the window invalid.
   - If so, decrease `have`.
   - Decrease the frequency of `s[i]`.
   - Move `i` forward.
9. If no valid window was found, return `""`.
10. Otherwise, return the smallest recorded substring.

## Complexity Analysis

Let:
- `m` = length of `s`
- `n` = length of `t`

**Time Complexity: O(m + n)**

- Building `tHashMap` takes O(n).
- The right pointer `j` traverses `s` once, taking O(m).
- The left pointer `i` also traverses `s` at most once, taking O(m).
- Each dictionary operation takes O(1) average time.

Therefore:

\[
O(n + m + m) = O(m+n)
\]

**Space Complexity: O(m + n)**

- `tHashMap` can store at most `n` distinct characters.
- `sHashMap` can store at most `m` distinct characters.

Therefore, the general auxiliary space bound is O(m + n).

Since the problem restricts the strings to uppercase and lowercase English letters, each dictionary can contain at most 52 distinct characters. Under these constraints, auxiliary space is **O(1)**.

## Concepts Used

- Variable-Size Sliding Window
- Two Pointers
- Hash Maps / Dictionaries
- Character Frequency Counting
- Greedy Window Shrinking

## Python Features Used

- `dict` for storing character frequencies.
- `set()` for counting distinct characters.
- `.get()` for retrieving a dictionary value with a default.
- `float('inf')` for initializing the minimum length.
- String slicing to extract the final substring.
- Nested `while` loops for expanding and shrinking the window.

## Key Takeaways

- Minimum Window Substring is a classic variable-size sliding window problem.
- Frequency counting is necessary because duplicate characters matter.
- `required` represents the number of distinct characters needed.
- `have` tracks how many distinct character requirements are currently satisfied.
- Expand the right pointer until the window becomes valid.
- Shrink the left pointer while the window remains valid.
- Always update the minimum window before removing the outgoing character.
- Each pointer moves only forward, giving an O(m + n) time complexity.

## Author

**Ramit Sarker**
