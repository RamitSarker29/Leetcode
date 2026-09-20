# 3498 - Reverse Degree of a String

## Problem

Given a string `s`, calculate its **reverse degree**.

The reverse degree is calculated in two steps:

1. Assign each lowercase letter a value according to its position in the **reversed alphabet**:
   ```text
   a = 26
   b = 25
   c = 24
   ...
   y = 2
   z = 1
   ```

2. For every character, multiply its reversed-alphabet value by its **position in the string** (1-indexed).

Finally, add all these products together.

---

# Examples

## Example 1

```text
Input:
s = "abc"

Output:
148
```

The calculation is:

```text
'a' → 26 × 1 = 26
'b' → 25 × 2 = 50
'c' → 24 × 3 = 72
```

Therefore:

```text
26 + 50 + 72 = 148
```

---

## Example 2

```text
Input:
s = "zaza"

Output:
160
```

The calculation is:

```text
'z' → 1 × 1 = 1
'a' → 26 × 2 = 52
'z' → 1 × 3 = 3
'a' → 26 × 4 = 104
```

Therefore:

```text
1 + 52 + 3 + 104 = 160
```

---

# Approach

The easiest way to handle the reversed alphabet values is to create a **dictionary (hash map)**.

For example:

```python
hash_map = {
    'a': 26,
    'b': 25,
    'c': 24,
    ...
    'z': 1
}
```

Then we traverse the string from left to right.

For every character:

```text
Reverse alphabet value × position in string
```

is added to `ans`.

The position is **1-indexed**, while Python's `range()` gives us a **0-indexed** index.

Therefore, we use:

```python
i + 1
```

instead of `i`.

---

# Code

```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        hash_map = {
            'a': 26,
            'b': 25,
            'c': 24,
            'd': 23,
            'e': 22,
            'f': 21,
            'g': 20,
            'h': 19,
            'i': 18,
            'j': 17,
            'k': 16,
            'l': 15,
            'm': 14,
            'n': 13,
            'o': 12,
            'p': 11,
            'q': 10,
            'r': 9,
            's': 8,
            't': 7,
            'u': 6,
            'v': 5,
            'w': 4,
            'x': 3,
            'y': 2,
            'z': 1
        }

        ans = 0

        for i in range(len(s)):
            ans += hash_map[s[i]] * (i + 1)

        return ans
```

---

# Explanation

## Step 1: Create the Hash Map

```python
hash_map = {
    'a': 26,
    'b': 25,
    'c': 24,
    ...
    'z': 1
}
```

The dictionary directly stores the reverse-alphabet value of every letter.

For example:

```text
'a' → 26
'm' → 14
'z' → 1
```

This allows us to get the value of any character quickly.

For example:

```python
hash_map['c']
```

returns:

```text
24
```

---

# Step 2: Initialize the Answer

```python
ans = 0
```

`ans` stores the total reverse degree.

Every character contributes one product to this value.

---

# Step 3: Traverse the String

```python
for i in range(len(s)):
```

We visit every character of the string.

For:

```text
s = "abc"
```

the indices are:

```text
i = 0 → 'a'
i = 1 → 'b'
i = 2 → 'c'
```

---

# Step 4: Get the Reverse-Alphabet Value

```python
hash_map[s[i]]
```

This looks up the value of the current character.

For example, if:

```text
s[i] = 'b'
```

then:

```python
hash_map['b']
```

gives:

```text
25
```

---

# Step 5: Convert the Index to 1-Based Position

Python uses zero-based indexing.

For:

```text
s = "abc"
```

Python sees:

```text
'a' → index 0
'b' → index 1
'c' → index 2
```

But the problem wants:

```text
'a' → position 1
'b' → position 2
'c' → position 3
```

Therefore we use:

```python
i + 1
```

---

# Step 6: Calculate the Contribution

The main line is:

```python
ans += hash_map[s[i]] * (i + 1)
```

This means:

```text
reverse-alphabet value × string position
```

and adds the result to `ans`.

For example:

```text
s[i] = 'b'
i = 1
```

Then:

```text
hash_map['b'] = 25
i + 1 = 2
```

So:

```text
25 × 2 = 50
```

and:

```text
ans += 50
```

---

# Dry Run

Let's take:

```text
s = "abc"
```

Initially:

```text
ans = 0
```

---

## Iteration 1

```text
i = 0
s[i] = 'a'
```

Reverse-alphabet value:

```text
hash_map['a'] = 26
```

Position:

```text
i + 1 = 1
```

Contribution:

```text
26 × 1 = 26
```

So:

```text
ans = 26
```

---

## Iteration 2

```text
i = 1
s[i] = 'b'
```

Reverse-alphabet value:

```text
hash_map['b'] = 25
```

Position:

```text
i + 1 = 2
```

Contribution:

```text
25 × 2 = 50
```

Update:

```text
ans = 26 + 50
    = 76
```

---

## Iteration 3

```text
i = 2
s[i] = 'c'
```

Reverse-alphabet value:

```text
hash_map['c'] = 24
```

Position:

```text
i + 1 = 3
```

Contribution:

```text
24 × 3 = 72
```

Update:

```text
ans = 76 + 72
    = 148
```

Final:

```text
Answer = 148
```

---

# Dry Run Table

| `i` | Character | Reverse Value | Position `i + 1` | Product | `ans` |
|---:|---|---:|---:|---:|---:|
| 0 | `a` | 26 | 1 | 26 | 26 |
| 1 | `b` | 25 | 2 | 50 | 76 |
| 2 | `c` | 24 | 3 | 72 | 148 |

Final answer:

```text
148
```

---

# Dry Run 2

Let's take:

```text
s = "zaza"
```

Initially:

```text
ans = 0
```

### Character 1

```text
'z' → 1
position = 1
```

Contribution:

```text
1 × 1 = 1
```

```text
ans = 1
```

### Character 2

```text
'a' → 26
position = 2
```

Contribution:

```text
26 × 2 = 52
```

```text
ans = 1 + 52
    = 53
```

### Character 3

```text
'z' → 1
position = 3
```

Contribution:

```text
1 × 3 = 3
```

```text
ans = 53 + 3
    = 56
```

### Character 4

```text
'a' → 26
position = 4
```

Contribution:

```text
26 × 4 = 104
```

Final:

```text
ans = 56 + 104
    = 160
```

Therefore:

```text
Answer = 160
```

---

# Dry Run Table

| `i` | Character | Reverse Value | Position | Product | `ans` |
|---:|---|---:|---:|---:|---:|
| 0 | `z` | 1 | 1 | 1 | 1 |
| 1 | `a` | 26 | 2 | 52 | 53 |
| 2 | `z` | 1 | 3 | 3 | 56 |
| 3 | `a` | 26 | 4 | 104 | 160 |

---

# Understanding the Formula

For every character at position `i`:

```text
Contribution =
Reverse Alphabet Value × (i + 1)
```

Therefore, the complete answer is:

```text
Reverse Degree =
Σ [reverse_value(character) × position]
```

For example, for `"abc"`:

```text
(26 × 1) + (25 × 2) + (24 × 3)
```

which gives:

```text
26 + 50 + 72 = 148
```

---

# Why Use a Hash Map?

Instead of writing many conditions such as:

```python
if s[i] == 'a':
    value = 26
elif s[i] == 'b':
    value = 25
...
```

we store all mappings in a dictionary.

Then:

```python
hash_map[s[i]]
```

directly gives the required value.

This makes the calculation simple:

```python
ans += hash_map[s[i]] * (i + 1)
```

---

# Why `i + 1`?

This is one of the most important details.

Python indexing starts at `0`:

```text
String:    a   b   c
Index:     0   1   2
```

But the problem uses **1-indexed positions**:

```text
Position:  1   2   3
```

Therefore:

```python
i + 1
```

converts the Python index into the required position.

If we used only `i`, the first character would be multiplied by `0`, which would be incorrect.

---

# Algorithm

```text
1. Create a dictionary containing the reverse-alphabet
   value of every lowercase letter.

2. Initialize ans = 0.

3. Traverse every character in the string.

4. For each character:
   
   a. Get its reverse-alphabet value from the dictionary.
   
   b. Get its 1-based position using i + 1.
   
   c. Multiply them.
   
   d. Add the product to ans.

5. Return ans.
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

where `n` is the length of the string.

We traverse the string exactly once.

Each dictionary lookup takes `O(1)` average time.

Therefore:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

The hash map always contains exactly **26 letters**, regardless of the length of the string.

The answer variable uses constant extra space.

Therefore, the auxiliary space is:

```text
O(1)
```

---

# Concepts Used

- Strings
- Hash Maps / Dictionaries
- One-Pass Traversal
- Character Mapping
- 0-Based vs 1-Based Indexing
- Arithmetic
- Accumulation

---

# Python Features Used

### Dictionary

```python
hash_map = {
    'a': 26,
    ...
    'z': 1
}
```

Stores the reverse-alphabet mapping.

### String Indexing

```python
s[i]
```

Gets the character at index `i`.

### `range()`

```python
range(len(s))
```

Generates all valid string indices.

### `i + 1`

Converts the zero-based Python index into the required one-based position.

### `+=`

```python
ans += ...
```

Adds each character's contribution to the running total.

---

# Key Takeaways

- The reversed alphabet maps `a → 26` and `z → 1`.
- A dictionary is used to store this mapping.
- Every character contributes:

```text
reverse-alphabet value × 1-based position
```

- Python uses zero-based indexing, so we use `i + 1`.
- The answer is accumulated in `ans`.
- The string is traversed only once.
- Time Complexity: **O(n)**.
- Space Complexity: **O(1)** because the dictionary always contains only 26 letters.

---

## Author

**Ramit Sarker**
