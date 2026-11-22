# 567. Permutation in String

## Problem

Given two strings `s1` and `s2`, determine whether `s2` contains any permutation of `s1` as a substring.

A **permutation** is a rearrangement of characters.

For example:

```text
s1 = "ab"

Possible permutations:
"ab"
"ba"
```

If any of these permutations appears as a continuous substring inside `s2`, return `True`.

Otherwise, return `False`.

---

# Examples

## Example 1

```text
Input:
s1 = "ab"
s2 = "eidbaooo"

Output: True
```

Explanation:

The substring `"ba"` exists inside `s2`.

```text
s2 = "eidbaooo"
          ↑↑
          ba
```

Since `"ba"` is a permutation of `"ab"`, return `True`.

## Example 2

```text
Input:
s1 = "ab"
s2 = "eidboaoo"

Output: False
```

Neither `"ab"` nor `"ba"` appears as a substring in `s2`.

Therefore, return `False`.

---

# Approach

Your solution uses **Sliding Window + Character Frequency Arrays**.

Instead of generating every possible permutation of `s1`, we compare character frequencies.

Why?

Because two strings are permutations of each other if they contain exactly the same characters with the same frequencies.

For example:

```text
"ab" → a: 1, b: 1
"ba" → a: 1, b: 1
```

Both have identical frequency arrays.

### Main Idea

1. If `s1` is longer than `s2`, return `False`.
2. Create two arrays of size `26`:
   - `s1Array` stores character frequencies of `s1`.
   - `s2Array` stores character frequencies of the current window in `s2`.
3. First, build the frequency array for `s1`.
4. Build the frequency array for the first window of `s2`, whose size is equal to `len(s1)`.
5. Compare both arrays.
6. Slide the window one position to the right:
   - Remove the outgoing character.
   - Add the incoming character.
7. Compare the frequency arrays after every movement.
8. If they match, return `True`.
9. If no window matches, return `False`.

---

# Code

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Array = [0] * 26
        s2Array = [0] * 26

        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            s1Array[index] += 1

        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            s2Array[index] += 1

            if s1Array == s2Array:
                return True

        i = 0
        j = len(s1)

        while j < len(s2):
            index = ord(s2[i]) - ord('a')
            s2Array[index] -= 1

            index = ord(s2[j]) - ord('a')
            s2Array[index] += 1

            if s1Array == s2Array:
                return True

            i += 1
            j += 1

        return False
```

---

# Code Explanation

## 1. Check the Lengths

```python
if len(s1) > len(s2):
    return False
```

A permutation of `s1` must have exactly the same length as `s1`.

If `s1` is longer than `s2`, it is impossible for `s2` to contain such a substring.

For example:

```text
s1 = "abcd"  → length = 4
s2 = "abc"   → length = 3
```

Therefore, return `False`.

---

## 2. Create Two Frequency Arrays

```python
s1Array = [0] * 26
s2Array = [0] * 26
```

Since the problem contains only lowercase English letters, we need an array of size `26`.

Each index represents a letter:

| Index | Character |
|---:|:---|
| 0 | a |
| 1 | b |
| 2 | c |
| 3 | d |
| ... | ... |
| 25 | z |

- `s1Array` stores the frequency of characters in `s1`.
- `s2Array` stores the frequency of characters in the current window of `s2`.

Initially, both arrays contain zeros.

---

## 3. Calculate Character Frequencies of `s1`

```python
for i in range(len(s1)):
    index = ord(s1[i]) - ord('a')
    s1Array[index] += 1
```

We traverse every character in `s1`.

### Understanding `ord()`

Python's `ord()` returns the Unicode code point of a character.

For lowercase English letters:

```text
ord('a') = 97
ord('b') = 98
ord('c') = 99
```

Therefore:

```python
ord(s1[i]) - ord('a')
```

converts a character into an index between `0` and `25`.

For example:

```text
s1[i] = 'a'

ord('a') - ord('a')
= 97 - 97
= 0
```

So index `0` represents `'a'`.

The frequency is then increased:

```python
s1Array[index] += 1
```

### Example

```text
s1 = "ab"
```

Initially:

```text
s1Array = [0, 0, 0, ..., 0]
```

After processing `'a'`:

```text
s1Array[0] = 1
```

After processing `'b'`:

```text
s1Array[1] = 1
```

Final frequency:

```text
a → 1
b → 1
all other characters → 0
```

---

## 4. Build the First Window of `s2`

```python
for i in range(len(s1)):
    index = ord(s2[i]) - ord('a')
    s2Array[index] += 1

    if s1Array == s2Array:
        return True
```

This loop builds the frequency array for the first window.

**Important:** The window size is always equal to `len(s1)`.

For example:

```text
s1 = "ab"
s2 = "eidbaooo"
```

Since `len(s1) = 2`, the first window contains:

```text
"ei"
```

The loop processes:

```text
i = 0 → 'e'
i = 1 → 'i'
```

The frequency array represents `"ei"`.

After each addition, your code compares the arrays.

```python
if s1Array == s2Array:
    return True
```

If both arrays match, the current window is a permutation of `s1`.

If they do not match, we move to the sliding-window part.

---

# 5. Initialize the Sliding Window

```python
i = 0
j = len(s1)
```

These two pointers represent the outgoing and incoming positions.

- `i` points to the character that will leave the current window.
- `j` points to the next character that will enter the window.

For:

```text
s1 = "ab"
s2 = "eidbaooo"
```

Initially:

```text
i = 0
j = 2
```

The current window is:

```text
e i d
↑   ↑
i   j
```

The current window is `"ei"`.

When we move the window, `e` leaves and `d` enters.

---

# 6. Slide the Window

```python
while j < len(s2):
```

The loop continues while there is another character available to enter the window.

Every iteration moves the window one position to the right.

---

## 7. Remove the Outgoing Character

```python
index = ord(s2[i]) - ord('a')
s2Array[index] -= 1
```

The character at index `i` is leaving the current window.

Therefore, we decrease its frequency by one.

For example:

```text
Current window = "ei"
```

The outgoing character is:

```text
'e'
```

Its frequency is reduced:

```text
e → 1 - 1 = 0
```

This removes `'e'` from the current window's frequency count.

---

## 8. Add the Incoming Character

```python
index = ord(s2[j]) - ord('a')
s2Array[index] += 1
```

The character at index `j` enters the window.

So we increase its frequency by one.

For example:

```text
Current window = "ei"
Incoming character = 'd'
```

After removing `'e'` and adding `'d'`:

```text
Old window = "ei"
New window = "id"
```

The frequency array now represents `"id"`.

---

## 9. Compare Both Frequency Arrays

```python
if s1Array == s2Array:
    return True
```

After every window movement, we compare the frequency arrays.

If they are equal, the current substring contains exactly the same characters as `s1`.

Therefore, it is a permutation.

Return `True` immediately.

---

## 10. Move Both Pointers

```python
i += 1
j += 1
```

Both pointers move one position forward.

This shifts the window to the right by one character.

For example:

```text
Previous window = "ei"
New window      = "id"
```

The window size remains unchanged.

---

## 11. Return False

```python
return False
```

If every possible window has been checked and none matches the frequency array of `s1`, no permutation exists in `s2`.

Therefore, return `False`.

---

# Understanding the Sliding Window

Consider:

```text
s1 = "ab"
s2 = "eidbaooo"
```

The window size is `2`.

The possible windows are:

<box border radius="lg" padding={3} gap={3}>
  {#each [{w:"ei",status:"Initial window",active:false},{w:"id",status:"Slide 1",active:false},{w:"db",status:"Slide 2",active:false},{w:"ba",status:"Slide 3 — Match!",active:true},{w:"ao",status:"Slide 4",active:false},{w:"oo",status:"Slide 5",active:false}] as item}
    <row align="center" justify="between">
      <box gap={1}>
        **{item.status}**
        <row gap={1}>
          {#each item.w.split("") as c}
            <box size="36px" radius="md" background={item.active ? "rgba(22,163,74,0.16)" : "surface-secondary"} align="center" justify="center">
              <title size="lg" color={item.active ? "success" : "default"}>{c}</title>
            </box>
          {/each}
        </row>
      </box>
      {#if item.active}
        <badge color="success">Match</badge>
      {/if}
    </row>
  {/each}
</box>

The window `"ba"` has the same character frequencies as `"ab"`.

Therefore, the answer is `True`.

---

# Dry Run

Consider:

```python
s1 = "ab"
s2 = "eidbaooo"
```

## Step 1: Build `s1Array`

```text
s1 = "ab"

a → 1
b → 1
```

So:

```text
s1Array = [1, 1, 0, 0, ..., 0]
```

## Step 2: Build the First Window

The first window is:

```text
"ei"
```

Its frequency array contains:

```text
e → 1
i → 1
```

Therefore:

```text
s2Array != s1Array
```

No match.

## Step 3: Initialize Pointers

```text
i = 0
j = 2
```

Current window:

```text
"ei"
```

## Step 4: First Window Movement

Remove:

```text
s2[i] = 'e'
```

Add:

```text
s2[j] = 'd'
```

New window:

```text
"id"
```

Frequency comparison:

```text
s1Array != s2Array
```

No match.

Move pointers:

```text
i = 1
j = 3
```

## Step 5: Second Window Movement

Remove:

```text
s2[1] = 'i'
```

Add:

```text
s2[3] = 'b'
```

New window:

```text
"db"
```

No match.

Move pointers:

```text
i = 2
j = 4
```

## Step 6: Third Window Movement

Remove:

```text
s2[2] = 'd'
```

Add:

```text
s2[4] = 'a'
```

New window:

```text
"ba"
```

Now:

```text
s1 = "ab"
window = "ba"
```

Both have:

```text
a → 1
b → 1
```

Therefore:

```python
s1Array == s2Array
```

The condition is `True`.

The function returns:

```text
True
```

---

# Why Does It Work?

A permutation must contain exactly the same characters with exactly the same frequencies.

Your solution maintains two frequency arrays:

- One for the entire string `s1`.
- One for the current window in `s2`.

Initially, the second array represents the first window of size `len(s1)`.

When the window moves:

- The outgoing character's frequency is decreased.
- The incoming character's frequency is increased.

This keeps `s2Array` synchronized with the current window without recounting all its characters.

Whenever both frequency arrays are equal, the current window is a permutation of `s1`.

Since every possible window of the required size is checked, the algorithm finds a permutation if one exists.

---

# Algorithm

1. If `len(s1) > len(s2)`, return `False`.
2. Create two frequency arrays of size `26`.
3. Calculate the character frequencies of `s1`.
4. Build the first window of `s2`, whose size is `len(s1)`.
5. Compare both frequency arrays after every character is added.
6. Initialize:
   - `i = 0`
   - `j = len(s1)`
7. While `j < len(s2)`:
   - Decrease the frequency of the outgoing character `s2[i]`.
   - Increase the frequency of the incoming character `s2[j]`.
   - Compare the frequency arrays.
   - If they match, return `True`.
   - Increment both pointers.
8. If no match is found, return `False`.

---

# Complexity Analysis

Let:

- `n` = length of `s1`
- `m` = length of `s2`

### Time Complexity

Building the frequency array for `s1`:

```text
O(n)
```

Building the initial window:

```text
O(n)
```

Sliding the window:

```text
O(m - n)
```

Each comparison of the two frequency arrays takes `O(26)` time.

Since the alphabet contains exactly 26 lowercase English letters, this comparison takes constant time.

Therefore:

```text
O(n + n + 26 × (m - n))
```

Simplifying:

```text
O(n + m)
```

**Time Complexity: O(n + m)**

### Space Complexity

We create two arrays:

```python
s1Array = [0] * 26
s2Array = [0] * 26
```

Each contains exactly 26 elements.

Therefore:

```text
O(26) = O(1)
```

**Space Complexity: O(1)**

---

# Concepts Used

- Sliding Window
- Two Pointers
- Character Frequency Counting
- Fixed-size Arrays
- Hashing through character indexing
- Frequency Comparison
- Early Return

---

# Python Features Used

### `ord()`

```python
ord(s1[i]) - ord('a')
```

Converts a lowercase character into an array index from `0` to `25`.

### List Initialization

```python
[0] * 26
```

Creates a frequency array containing 26 zeros.

### Incrementing Frequency

```python
s1Array[index] += 1
```

Increases the frequency of a character.

### Decrementing Frequency

```python
s2Array[index] -= 1
```

Removes one occurrence of the outgoing character from the current window.

### List Comparison

```python
s1Array == s2Array
```

Checks whether both frequency arrays contain exactly the same values.

### Two Pointers

```python
i = 0
j = len(s1)
```

Track the outgoing and incoming positions of the sliding window.

---

# Key Takeaways

- A permutation has the same character frequencies, regardless of character order.
- There is no need to generate actual permutations.
- A fixed-size frequency array efficiently represents lowercase character counts.
- The sliding window always has a size equal to `len(s1)`.
- Remove the outgoing character and add the incoming character when moving the window.
- Comparing two arrays of 26 elements takes constant time.
- The solution achieves **O(n + m) time** and **O(1) extra space**.
- This is a classic example of combining the **Sliding Window and Two Pointers patterns**.

---

# Author

**Ramit Sarker**
