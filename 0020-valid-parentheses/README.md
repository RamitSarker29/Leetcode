# 20. Valid Parentheses

## Problem

You are given a string `s` containing only the following characters:

```text
( ) { } [ ]
```

Determine whether the string is **valid**.

A string is valid if:

1. Every opening bracket has a matching closing bracket.
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

A **stack** is perfect for matching brackets because it follows the **Last In, First Out (LIFO)** principle.

- Whenever an opening bracket appears, push it onto the stack.
- Whenever a closing bracket appears, it must match the opening bracket at the top of the stack.
- If it matches, remove (pop) the opening bracket.
- Otherwise, the string is invalid.

At the end, if the stack is empty, every opening bracket has been matched.

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
for ch in s:
```

---

### Step 3

If the current character is an opening bracket,

push it onto the stack.

```python
if ch in "([{":
    stack.append(ch)
```

---

### Step 4

If the current character is a closing bracket,

first check whether the stack is empty.

```python
if not stack:
    return False
```

An empty stack means there is no matching opening bracket.

---

### Step 5

Compare the closing bracket with the top of the stack.

For example,

```python
if ch == ')' and stack[-1] != '(':
    return False
```

Do the same for `{}` and `[]`.

---

### Step 6

If they match,

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

If it is empty, the string is valid.

---

# Algorithm

1. Create an empty stack.
2. Traverse each character.
3. Push opening brackets onto the stack.
4. For every closing bracket:
   - If the stack is empty, return `False`.
   - If the top of the stack does not match, return `False`.
   - Otherwise, pop the stack.
5. Return `True` if the stack is empty, otherwise `False`.

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

Top of stack:

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

Top of stack:

```text
(
```

Matches `)`.

Pop.

```text
stack = []
```

End of string.

Stack is empty.

Return:

```text
True
```

---

# Why Does This Work?

The stack always stores unmatched opening brackets.

Whenever a closing bracket appears,

it must match the opening bracket on top of the stack.

If it does not,

the order is incorrect and the string is invalid.

If every opening bracket is matched,

the stack becomes empty.

Therefore, the string is valid.

---

# Time Complexity

Each character is processed exactly once.

Every bracket is:

- pushed at most once
- popped at most once

```text
O(n)
```

---

# Space Complexity

In the worst case,

every character is an opening bracket.

Example:

```text
"((([[{{"
```

The stack stores all characters.

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
if not stack:
```

---

### Membership Operator

```python
if ch in "([{":
```

Checks whether the character is an opening bracket.

---

# Key Takeaways

- Use a stack to store opening brackets.
- Push every opening bracket.
- Match every closing bracket with the top of the stack.
- Return `False` immediately if a mismatch occurs.
- At the end, the stack must be empty.
- The solution runs in **O(n)** time and **O(n)** space.
- This is the optimal solution.

---

## Author

**Ramit Sarker**
