# Remove All Occurrences of a Character in a String

## Problem

Given a string `s` and a character `c`, remove **all occurrences** of `c` from the string.

Return the resulting string.

---

## Examples

### Example 1

**Input**

```text
s = "geeksforgeeks"
c = 'e'
```

**Output**

```text
"gksforgks"
```

**Explanation**

Remove every `e`:

```text
g e e k s f o r g e e k s
  ✗ ✗             ✗ ✗
```

Result:

```text
"gksforgks"
```

---

### Example 2

**Input**

```text
s = "geeksforgeeks"
c = 'g'
```

**Output**

```text
"eeksforeeks"
```

All `g` characters are removed.

---

# Approach

We use the **Two Pointer technique**.

We convert the string into a list because Python strings are immutable:

```python
s = list(s)
```

Then we use two pointers:

```text
i → position where the next valid character should be placed
j → position currently being checked
```

Initially:

```python
i = 0
j = 0
```

---

# What Does `j` Do?

`j` moves through the entire string.

It checks every character:

```text
s[j]
```

So:

```text
j = 0
1
2
3
...
```

`j` never moves backward.

---

# What Does `i` Do?

`i` tells us where to place the characters that **should not be removed**.

If:

```python
s[j] != c
```

then the current character is valid.

We copy it to:

```python
s[i] = s[j]
```

and move `i` forward:

```python
i += 1
```

If:

```python
s[j] == c
```

we don't copy it.

We simply move `j` forward.

---

# The Important Idea

Think of the array as having two sections:

```text
[processed part | unprocessed part]
        ↑                ↑
        i                j
```

`j` searches for characters.

`i` builds the final answer.

So:

```text
j → reads
i → writes
```

This is the core idea behind the Two Pointer approach.

---

# Code

```python
class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here

        i = 0
        j = 0

        s = list(s)

        while j < len(s):

            if s[j] != c:
                s[i] = s[j]
                i += 1

            j += 1

        return ''.join(s[:i])
```

---

# Dry Run

Consider:

```text
s = "geeksforgeeks"
c = 'e'
```

Convert the string to a list:

```text
[g,e,e,k,s,f,o,r,g,e,e,k,s]
```

Initially:

```text
i = 0
j = 0
```

---

### `j = 0`

Current character:

```text
s[j] = 'g'
```

`g` is not `e`.

So copy:

```text
s[i] = s[j]
```

The beginning becomes:

```text
[g, ...]
 ↑
 i
```

Then:

```text
i = 1
j = 1
```

---

### `j = 1`

Current:

```text
s[j] = 'e'
```

But:

```text
e == c
```

So we **do not copy it**.

Only:

```text
j += 1
```

Now:

```text
i = 1
j = 2
```

---

### `j = 2`

Again:

```text
s[j] = 'e'
```

It should be removed.

So:

```text
i = 1
j = 3
```

Notice that `i` did not move.

That's because we haven't found the next character that belongs in the result yet.

---

### `j = 3`

Current:

```text
s[j] = 'k'
```

`k` should stay.

So:

```text
s[i] = s[j]
```

That means:

```text
s[1] = s[3]
```

Now the beginning of the list is:

```text
[g,k,...]
```

Then:

```text
i = 2
j = 4
```

---

The same process continues.

Eventually, the valid characters are placed at the beginning:

```text
[g,k,s,f,o,r,g,k,s,...]
```

So:

```text
i = 9
```

The first `9` positions contain the answer:

```text
[g,k,s,f,o,r,g,k,s]
```

Therefore:

```python
s[:i]
```

gives:

```text
"gksforgks"
```

---

# Why Do We Use `s[:i]`?

This is an important part.

We are modifying the existing list **in place**.

Suppose:

```text
s = "a b c d"
```

and we remove `b`.

After moving the valid characters, the list might look like:

```text
[a,c,d,d]
```

The extra `d` at the end is leftover data.

But we only want:

```text
[a,c,d]
```

The variable `i` tells us exactly where the valid portion ends.

Therefore:

```python
s[:i]
```

selects only the valid part.

Then:

```python
''.join(s[:i])
```

converts it back into a string.

---

# Why Not Delete Characters Directly?

We could try something like:

```python
while c in s:
    s.remove(c)
```

But repeatedly removing elements from a string/list can require shifting many elements.

That can make the solution inefficient.

Instead, we simply **overwrite unwanted characters** using `i`.

This gives us a linear solution.

---

# Two Pointer Visualization

Suppose:

```text
s = "abac"
c = 'a'
```

Initially:

```text
i
↓
a b a c
↑
j
```

`j` sees `a`:

```text
a → remove
```

So:

```text
i = 0
j = 1
```

Now `j` sees `b`.

Copy it:

```text
b
```

So:

```text
b ...
↑
i
```

Then `j` sees another `a`:

```text
a → remove
```

Finally `j` sees `c`.

Copy it:

```text
b c
↑ ↑
i
```

Result:

```text
"bc"
```

---

# Why Does It Work?

For every character:

### If it equals `c`

We skip it:

```python
if s[j] != c:
```

The character is never copied to the valid portion.

### If it does not equal `c`

We copy it to the next available position:

```python
s[i] = s[j]
```

Therefore, after processing the entire string:

```text
s[0:i]
```

contains **exactly all characters that are not equal to `c`**, in their original order.

So returning:

```python
''.join(s[:i])
```

gives the required answer.

---

# Algorithm

1. Convert `s` into a list.
2. Set:

   ```python
   i = 0
   j = 0
   ```
3. Move `j` through the entire list.
4. If `s[j] != c`:

   * Copy `s[j]` to `s[i]`.
   * Increment `i`.
5. Always increment `j`.
6. Return the first `i` elements joined into a string.

---

# Complexity

Let:

```text
n = len(s)
```

### Time Complexity

`j` visits every character exactly once:

```text
O(n)
```

### Auxiliary Space

Apart from the modified list and the returned string, the algorithm uses only two pointers:

```text
O(1)
```

The GFG constraint describes the auxiliary working space as `O(1)`.

---

# Key Takeaways

* This is a **Two Pointer** problem.
* `j` is the **reader**.
* `i` is the **writer**.
* `j` checks every character.
* `i` keeps track of where the next valid character should go.
* If:

  ```python
  s[j] == c
  ```

  skip it.
* If:

  ```python
  s[j] != c
  ```

  copy it to `s[i]`.
* `s[:i]` contains the final valid portion.
* **Time Complexity:** `O(n)`
* **Auxiliary Space:** `O(1)`

---

## Author

**Ramit Sarker**
