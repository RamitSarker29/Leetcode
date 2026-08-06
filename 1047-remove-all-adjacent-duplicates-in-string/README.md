# 1047. Remove All Adjacent Duplicates In String

## Problem

You are given a string `s` consisting of lowercase English letters.

A **duplicate removal** consists of removing two **adjacent** and **equal** characters.

Keep removing adjacent duplicates until no more duplicate pairs remain.

Return the final string.

It is guaranteed that the answer is unique.

---

## Examples

### Example 1

**Input**

```text
s = "abbaca"
```

**Output**

```text
"ca"
```

**Explanation**

```text
abbaca

Remove "bb"

↓

aaca

Remove "aa"

↓

ca
```

No more adjacent duplicates remain.

---

### Example 2

**Input**

```text
s = "azxxzy"
```

**Output**

```text
"ay"
```

**Explanation**

```text
azxxzy

Remove "xx"

↓

azzy

Remove "zz"

↓

ay
```

---

# Intuition

Whenever we encounter two adjacent equal characters,

they cancel each other.

A **stack** naturally simulates this process.

- If the current character is different from the top of the stack, push it.
- If it is the same as the top, remove the top (pop).

After processing every character, the stack contains the final string.

---

# Approach

### Step 1

Create an empty stack.

```python
stack = []
```

---

### Step 2

Traverse every character of the string.

```python
for i in range(len(s)):
```

---

### Step 3

If the stack is not empty and the current character is equal to the top of the stack,

remove the duplicate.

```python
if stack and stack[-1] == s[i]:
    stack.pop()
```

---

### Step 4

Otherwise,

push the current character onto the stack.

```python
stack.append(s[i])
```

---

### Step 5

The stack stores the remaining characters.

Convert it back into a string.

```python
"".join(stack)
```

Return the result.

---

# Algorithm

1. Create an empty stack.
2. Traverse each character of the string.
3. If the top of the stack matches the current character, pop it.
4. Otherwise, push the current character.
5. Convert the stack into a string and return it.

---

# Code

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
```

---

# Dry Run

### Example

```text
s = "abbaca"
```

Initially

```text
stack = []
```

Read `'a'`

```text
[a]
```

Read `'b'`

```text
[a, b]
```

Read `'b'`

Top is also `'b'`.

Pop it.

```text
[a]
```

Read `'a'`

Top is also `'a'`.

Pop it.

```text
[]
```

Read `'c'`

```text
[c]
```

Read `'a'`

```text
[c, a]
```

Final answer:

```text
"ca"
```

---

# Why Does This Work?

The stack always stores the characters that have not been removed.

Whenever two adjacent equal characters appear,

the top of the stack already contains the previous character.

If they are equal,

removing the top effectively removes the adjacent duplicate pair.

Since every character is processed exactly once,

all duplicate removals happen automatically in the correct order.

---

# Time Complexity

Each character is:

- pushed at most once
- popped at most once

Traversal:

```text
O(n)
```

Joining the stack into a string:

```text
O(n)
```

Overall:

```text
O(n)
```

---

# Space Complexity

The stack may contain every character.

Example:

```text
abcdef
```

No duplicates are removed.

Therefore:

```text
O(n)
```

---

# Concepts Used

- Stack
- Strings
- Simulation

---

# Python Features Used

### Create Stack

```python
stack = []
```

---

### Push

```python
stack.append(ch)
```

---

### Pop

```python
stack.pop()
```

---

### Peek (Top Element)

```python
stack[-1]
```

---

### Empty Stack Check

```python
if stack:
```

Equivalent to:

```python
if len(stack) > 0:
```

---

### Join List into String

```python
"".join(stack)
```

---

# Key Takeaways

- Use a stack to simulate removing adjacent duplicates.
- Push characters when they don't match the stack's top.
- Pop the top when a duplicate is found.
- Each character is pushed and popped at most once.
- The algorithm runs in **O(n)** time with **O(n)** space.
- This is the optimal solution.

---

## Author

**Ramit Sarker**
