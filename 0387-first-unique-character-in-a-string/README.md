# 387. First Unique Character in a String

## Problem

Given a string `s`, find the **first non-repeating character** in the string and return its index.

If there is no character that appears exactly once, return:

```text
-1
```

The important part is that we need the **first** unique character, not just any unique character.

---

## Examples

### Example 1

**Input**

```text
s = "leetcode"
```

**Output**

```text
0
```

**Explanation**

The character `'l'` occurs only once and is the first unique character.

```text
l e e t c o d e
↑
0
```

Therefore, the answer is `0`.

---

### Example 2

**Input**

```text
s = "loveleetcode"
```

**Output**

```text
2
```

**Explanation**

The characters are:

```text
l o v e l e e t c o d e
0 1 2 3 4 5 6 7 8 9 10 11
```

* `'l'` appears twice.
* `'o'` appears twice.
* `'v'` appears only once.

Therefore, the first unique character is `'v'` at index `2`.

---

### Example 3

**Input**

```text
s = "aabb"
```

**Output**

```text
-1
```

**Explanation**

Both `'a'` and `'b'` appear twice, so there is no unique character.

---

# Approach

We use a **hash map (dictionary)** to store the frequency of every character.

The solution requires **two traversals**.

### First Traversal

Count how many times every character occurs.

For example:

```text
s = "loveleetcode"
```

The frequency map becomes:

```text
{
    'l': 2,
    'o': 2,
    'v': 1,
    'e': 4,
    't': 1,
    'c': 1,
    'd': 1
}
```

### Second Traversal

Traverse the string from left to right again.

For each character, check:

```python
hash_map[s[j]] == 1
```

The **first** character whose frequency is `1` is the answer.

If we finish the traversal without finding one, return `-1`.

---

# Why Do We Need Two Traversals?

We cannot immediately know whether a character is unique just by looking at it once.

For example:

```text
s = "loveleetcode"
```

When we first encounter `'l'`, it looks unique.

But later, another `'l'` appears.

So we first need to know the **complete frequency** of every character.

Then we make another traversal to preserve the original order and find the first character with frequency `1`.

---

# Algorithm

1. Create an empty dictionary `hash_map`.
2. Traverse the string and count every character.
3. Traverse the string again from left to right.
4. If the frequency of the current character is `1`, return its index.
5. If no unique character is found, return `-1`.

---

# Code

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        # Count frequency of every character
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1

        # Find the first character with frequency 1
        for j in range(len(s)):
            if hash_map[s[j]] == 1:
                return j

        return -1
```

---

# Dry Run

Consider:

```text
s = "loveleetcode"
```

## First Traversal — Count Frequencies

Initially:

```text
hash_map = {}
```

After processing the string:

```text
{
    'l': 2,
    'o': 2,
    'v': 1,
    'e': 4,
    't': 1,
    'c': 1,
    'd': 1
}
```

---

## Second Traversal — Find First Unique

Start from index `0`.

### Index 0 → `'l'`

```text
hash_map['l'] = 2
```

Not unique.

---

### Index 1 → `'o'`

```text
hash_map['o'] = 2
```

Not unique.

---

### Index 2 → `'v'`

```text
hash_map['v'] = 1
```

This character occurs exactly once.

Therefore:

```text
return 2
```

---

# Another Example

Consider:

```text
s = "aabb"
```

Frequency map:

```text
{
    'a': 2,
    'b': 2
}
```

Second traversal:

```text
'a' → 2
'a' → 2
'b' → 2
'b' → 2
```

No character has frequency `1`.

Therefore:

```text
return -1
```

---

# Why Does It Work?

The first traversal tells us **how many times each character occurs**.

The second traversal maintains the original left-to-right order.

Therefore, when we find:

```python
hash_map[s[j]] == 1
```

we know:

1. The character appears exactly once.
2. We are checking characters from left to right.
3. Therefore, it is the **first unique character**.

---

# Complexity

Let:

```text
n = len(s)
```

### Time Complexity

We traverse the string twice.

First traversal:

```text
O(n)
```

Second traversal:

```text
O(n)
```

Therefore:

```text
O(n) + O(n) = O(n)
```

So the overall time complexity is:

```text
O(n)
```

### Space Complexity

The hash map stores the frequency of each distinct character.

Since the string contains only lowercase English letters, there can be at most `26` different characters.

Therefore, technically:

```text
O(26) = O(1)
```

If considering a general character set, the space would be `O(k)`, where `k` is the number of distinct characters.

---

# Key Takeaways

* Use a **hash map/dictionary** to count character frequencies.
* The first traversal calculates frequencies.
* The second traversal finds the first character with frequency `1`.
* Two traversals are still **O(n)**, not `O(n²)`.
* The second traversal is necessary to preserve the **first occurrence order**.
* Since there are only 26 lowercase English letters, auxiliary space is technically **O(1)**.
* If no unique character exists, return `-1`.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)` for the given constraints.

---

## Author

**Ramit Sarker**
