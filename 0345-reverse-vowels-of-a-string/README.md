# LeetCode 345 - Reverse Vowels of a String

## Problem

Given a string `s`, reverse **only the vowels** in the string and return the resulting string.

The vowels are:

```text
a, e, i, o, u
A, E, I, O, U
```

All consonants must remain in their original positions.

---

## Examples

### Example 1

**Input**

```text
s = "IceCreAm"
```

**Output**

```text
"AceCreIm"
```

**Explanation**

Vowels in the string:

```text
I  e  e  A
```

Reversing them gives:

```text
A  e  e  I
```

Final string:

```text
AceCreIm
```

---

### Example 2

**Input**

```text
s = "leetcode"
```

**Output**

```text
"leotcede"
```

---

## Approach

This problem can be solved efficiently using the **Two Pointer** technique.

We place:

- One pointer (`i`) at the beginning.
- One pointer (`j`) at the end.

The idea is:

- Move the left pointer until it finds a vowel.
- Move the right pointer until it finds a vowel.
- Once both pointers point to vowels, swap them.
- Move both pointers inward.
- Continue until the pointers meet.

Since each character is visited at most once, the solution is linear.

---

## Code

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] not in "aeiouAEIOU":
                i += 1
            elif s[j] not in "aeiouAEIOU":
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
```

---

## Explanation

### Step 1

Convert the string into a list.

```python
s = list(s)
```

Strings in Python are **immutable**, so they cannot be modified directly.

Converting to a list allows swapping characters.

---

### Step 2

Initialize two pointers.

```text
i → Beginning
j → End
```

Example:

```text
I c e C r e A m
↑             ↑
i             j
```

---

### Step 3

Move the left pointer.

If the current character is **not** a vowel,

```python
i += 1
```

because consonants should remain unchanged.

---

### Step 4

Move the right pointer.

If the current character is **not** a vowel,

```python
j -= 1
```

Continue searching until a vowel is found.

---

### Step 5

When both pointers point to vowels,

swap them.

```python
s[i], s[j] = s[j], s[i]
```

Then move both pointers.

```python
i += 1
j -= 1
```

Repeat until

```text
i >= j
```

---

### Step 6

Convert the list back into a string.

```python
"".join(s)
```

---

## Dry Run

### Input

```text
s = "IceCreAm"
```

Initial

```text
I c e C r e A m
↑             ↑
i             j
```

`m` is not a vowel.

Move `j`.

```text
I c e C r e A m
↑           ↑
i           j
```

Both are vowels.

Swap.

```text
A c e C r e I m
```

Move both pointers.

```text
A c e C r e I m
  ↑       ↑
  i       j
```

Both are vowels.

Swap.

```text
A c e C r e I m
```

(No visible change because both are `e`.)

Move again.

Pointers cross.

Final answer:

```text
AceCreIm
```

---

## Time Complexity

```text
O(n)
```

Each pointer moves through the string only once.

---

## Space Complexity

```text
O(n)
```

The string is converted into a list before modification.

---

## Concepts Used

- Two Pointers
- String Traversal
- In-place Swapping (on a list)

---

## Python Features Used

### Convert string to list

```python
list(s)
```

### Membership checking

```python
ch in "aeiouAEIOU"
```

### Multiple Assignment (Swapping)

```python
s[i], s[j] = s[j], s[i]
```

### Convert list back to string

```python
"".join(s)
```

---

## Key Takeaways

- Strings in Python are immutable, so convert them to a list before modifying.
- Two pointers help solve the problem in one traversal.
- Move the left pointer until it reaches a vowel.
- Move the right pointer until it reaches a vowel.
- Swap the vowels and continue searching.
- Each character is processed at most once, giving an **O(n)** solution.

---

**Author:** Ramit Sarker
