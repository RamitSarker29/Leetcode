# 125. Valid Palindrome

## Problem

A phrase is considered a **palindrome** if, after:

- Converting all uppercase letters to lowercase.
- Removing all non-alphanumeric characters.

it reads the same forwards and backwards.

Return `true` if the given string is a palindrome, otherwise return `false`.

---

## Examples

### Example 1

**Input**

```text
s = "A man, a plan, a canal: Panama"
```

**Output**

```text
true
```

**Explanation**

After removing non-alphanumeric characters and converting to lowercase:

```text
amanaplanacanalpanama
```

It reads the same from both directions.

---

### Example 2

**Input**

```text
s = "race a car"
```

**Output**

```text
false
```

**Explanation**

After preprocessing:

```text
raceacar
```

which is not a palindrome.

---

### Example 3

**Input**

```text
s = " "
```

**Output**

```text
true
```

**Explanation**

After removing non-alphanumeric characters:

```text
""
```

An empty string is considered a palindrome.

---

# Intuition

A palindrome reads the same from both directions.

We can use **two pointers**:

- One starting from the beginning.
- One starting from the end.

However, before comparing characters:

- Skip spaces.
- Skip punctuation.
- Convert uppercase letters to lowercase.

If every valid character matches, the string is a palindrome.

---

# Approach

1. Place one pointer at the beginning.
2. Place another pointer at the end.
3. Skip non-alphanumeric characters.
4. Convert both characters to lowercase.
5. Compare them.
6. If they differ, return `False`.
7. Otherwise move both pointers.
8. Continue until the pointers cross.

---

# Algorithm

1. Initialize two pointers.

```python
left = 0
right = len(s) - 1
```

2. While `left < right`:

- Skip invalid characters from the left.
- Skip invalid characters from the right.
- Compare lowercase characters.
- If different, return `False`.
- Otherwise move both pointers.

3. Return `True`.

---

# Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j:

            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
```

---

# Dry Run

### Example

```text
s = "A man, a plan, a canal: Panama"
```

| Left | Right | Characters | Action |
|------|-------|------------|--------|
| A | a | Match after lowercase | Move both |
| Space | m | Skip space | Move left |
| m | m | Match | Move both |
| a | a | Match | Move both |
| n | n | Match | Move both |
| , | a | Skip comma | Move left |
| ... | ... | Continue comparing | |
| P | p | Match after lowercase | Move both |

Pointers eventually cross.

Return:

```text
True
```

---

# Time Complexity

```text
O(n)
```

Each pointer moves at most `n` times.

---

# Space Complexity

```text
O(1)
```

No extra string or array is created.

---

# Concepts Used

- Two Pointers
- Strings
- Character Processing

---

# Python Features Used

### Check if character is alphanumeric

```python
s[i].isalnum()
```

Examples

```python
"A".isalnum()    # True
"7".isalnum()    # True
" ".isalnum()    # False
",".isalnum()    # False
```

---

### Convert to lowercase

```python
s[i].lower()
```

Examples

```python
"A".lower()      # "a"
"Z".lower()      # "z"
```

---

# Key Takeaways

- Use two pointers from both ends.
- Skip spaces and punctuation using `isalnum()`.
- Compare characters after converting them to lowercase.
- No extra string is required.
- Runs in **O(n)** time with **O(1)** extra space.

---

## Author

**Ramit Sarker**
