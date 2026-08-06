# 20. Valid Parentheses

## Problem

You are given a string `s` containing only the following brackets:

```text
( ) { } [ ]
```

Determine whether the string is valid.

A string is considered valid if:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket matches the most recent unmatched opening bracket.

Return `True` if the string is valid, otherwise return `False`.

---

## Examples

### Example 1

**Input**

```text
s = "()"
```

**Output**

```text
True
```

---

### Example 2

**Input**

```text
s = "()[]{}"
```

**Output**

```text
True
```

---

### Example 3

**Input**

```text
s = "(]"
```

**Output**

```text
False
```

---

### Example 4

**Input**

```text
s = "([])"
```

**Output**

```text
True
```

---

### Example 5

**Input**

```text
s = "([)]"
```

**Output**

```text
False
```

---

# Intuition

Since brackets must be closed in the reverse order in which they are opened, a **stack** is the ideal data structure.

- Push every opening bracket.
- When a closing bracket appears, compare it with the top of the stack.
- If they match, remove the opening bracket.
- Otherwise, the string is invalid.

At the end, the stack should be empty.

---

# Approach

### Step 1

Create an empty stack.

```python
stack = []
```

---

### Step 2

Traverse every character in the string.

```python
for i in s:
```

---

### Step 3

If the current character is an opening bracket,

push it onto the stack.

```python
if i in "([{":
    stack.append(i)
```

---

### Step 4

If the current character is a closing bracket,

first check whether the stack is empty.

```python
if not stack:
    return False
```

If the stack is empty, there is no opening bracket to match.

---

### Step 5

Check whether the current closing bracket matches the opening bracket on top of the stack.

For `)`

```python
if i == ')' and stack[-1] != '(':
    return False
```

For `}`

```python
if i == '}' and stack[-1] != '{':
    return False
```

For `]`

```python
if i == ']' and stack[-1] != '[':
    return False
```

---

### Step 6

If the brackets match,

remove the opening bracket.

```python
stack.pop()
```

---

### Step 7

After processing every character,

the stack should be empty.

```python
return not stack
```

If the stack is empty, every opening bracket has been matched.

---

# Algorithm

1. Create an empty stack.
2. Traverse every character.
3. Push opening brackets.
4. If a closing bracket is found:
   - Check if the stack is empty.
   - Verify that it matches the top of the stack.
   - Pop the matching opening bracket.
5. Return whether the stack is empty.

---

# Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False

                if i == ')' and stack[-1] != '(':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False

                stack.pop()

        return not stack
```

---

# Dry Run

### Example

```text
s = "([])"
```

Initially

```text
stack = []
```

Read `'('`

```text
stack = ['(']
```

---

Read `'['`

```text
stack = ['(', '[']
```

---

Read `']'`

Top of the stack:

```text
[
```

Matches `]`.

Pop.

```text
stack = ['(']
```

---

Read `')'`

Top of the stack:

```text
(
```

Matches `)`.

Pop.

```text
stack = []
```

The stack is empty.

Return:

```text
True
```

---

# Why Does This Work?

The stack always stores unmatched opening brackets.

Whenever a closing bracket is encountered, it must match the opening bracket at the top of the stack.

If it does not match, the string is invalid.

If every opening bracket is matched correctly, the stack becomes empty by the end of the traversal.

Therefore, the string is valid.

---

# Time Complexity

Each character is processed once.

Each bracket is:

- pushed at most once
- popped at most once

Overall:

```text
O(n)
```

---

# Space Complexity

In the worst case, every character is an opening bracket.

Example:

```text
"((([[{{"
```

The stack stores all brackets.

Overall:

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
stack.append(i)
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
if not stack:
```

---

### Membership Operator

```python
if i in "([{":
```

Checks whether the current character is an opening bracket.

---

# Key Takeaways

- Use a stack to store opening brackets.
- Push every opening bracket.
- Match every closing bracket with the top of the stack.
- Return `False` immediately if a mismatch is found.
- At the end, the stack must be empty.
- The solution runs in **O(n)** time and **O(n)** space.
- This is the optimal solution.

---

## Author

**Ramit Sarker**
