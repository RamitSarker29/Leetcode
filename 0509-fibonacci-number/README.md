# 1013. Fibonacci Number

## Problem

The **Fibonacci numbers** form a sequence where each number is the sum of the two preceding numbers.

The sequence starts with:

```text
F(0) = 0
F(1) = 1
```

For `n > 1`:

```text
F(n) = F(n - 1) + F(n - 2)
```

Given an integer `n`, return `F(n)`.

---

## Fibonacci Sequence

The sequence looks like:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

For example:

```text
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
```

---

## Examples

### Example 1

**Input**

```text
n = 2
```

**Output**

```text
1
```

**Explanation**

```text
F(2) = F(1) + F(0)
     = 1 + 0
     = 1
```

---

### Example 2

**Input**

```text
n = 3
```

**Output**

```text
2
```

**Explanation**

```text
F(3) = F(2) + F(1)
     = 1 + 1
     = 2
```

---

### Example 3

**Input**

```text
n = 4
```

**Output**

```text
3
```

**Explanation**

```text
F(4) = F(3) + F(2)
     = 2 + 1
     = 3
```

---

# Approach

We can calculate Fibonacci numbers **iteratively** using only two variables.

We don't need to store the entire Fibonacci sequence.

At any point, we only need:

```text
previous two Fibonacci numbers
```

We use:

```python
a = 0
b = 1
```

where:

```text
a = current Fibonacci number
b = next Fibonacci number
```

Initially:

```text
a = F(0) = 0
b = F(1) = 1
```

---

# Updating the Values

The important line is:

```python
a, b = b, a + b
```

Suppose:

```text
a = 2
b = 3
```

Then:

```text
a, b = b, a + b
```

becomes:

```text
a = 3
b = 5
```

So we move forward in the Fibonacci sequence:

```text
2 → 3 → 5
```

---

# Why Use Two Variables?

A simple approach might create an entire array:

```text
[0,1,1,2,3,5,8,...]
```

But we don't need all previous values.

To calculate the next Fibonacci number, we only need:

```text
F(n-2)
F(n-1)
```

Therefore, two variables are enough.

This reduces the space complexity from:

```text
O(n)
```

to:

```text
O(1)
```

---

# Algorithm

1. Initialize:

```python
a = 0
b = 1
```

2. Repeat `n` times.
3. During each iteration:

   * Move `b` into `a`.
   * Calculate the new `b` as `a + b` using the old values.
4. Return `a`.

---

# Code

```python
class Solution:

    def fib(self, n: int) -> int:

        a = 0
        b = 1

        for i in range(n):
            a, b = b, a + b

        return a
```

---

# Dry Run

Consider:

```text
n = 5
```

We want:

```text
F(5) = 5
```

Initial:

```text
a = 0
b = 1
```

---

### Iteration 1

```python
a, b = b, a + b
```

Becomes:

```text
a = 1
b = 1
```

---

### Iteration 2

```text
a = 1
b = 2
```

---

### Iteration 3

```text
a = 2
b = 3
```

---

### Iteration 4

```text
a = 3
b = 5
```

---

### Iteration 5

```text
a = 5
b = 8
```

Now:

```text
a = F(5)
```

Therefore:

```text
return a
```

returns:

```text
5
```

---

# Understanding `a, b = b, a + b`

This line can initially look confusing:

```python
a, b = b, a + b
```

Python evaluates the **right side first**.

Suppose:

```text
a = 2
b = 3
```

It first calculates:

```text
b       → 3
a + b   → 5
```

Then assigns:

```text
a = 3
b = 5
```

So it is equivalent to:

```python
old_a = a
old_b = b

a = old_b
b = old_a + old_b
```

but Python's multiple assignment lets us write it more cleanly.

---

# Why Does the Loop Run `n` Times?

Initially:

```text
a = F(0)
```

After one iteration:

```text
a = F(1)
```

After two:

```text
a = F(2)
```

After three:

```text
a = F(3)
```

Therefore, after `n` iterations:

```text
a = F(n)
```

which is why we use:

```python
for i in range(n):
```

---

# Edge Cases

### `n = 0`

Initial:

```text
a = 0
b = 1
```

The loop runs zero times.

Return:

```text
0
```

Correct:

```text
F(0) = 0
```

---

### `n = 1`

One iteration:

```text
a = 1
b = 1
```

Return:

```text
1
```

Correct:

```text
F(1) = 1
```

---

# Why Not Use Recursion?

The mathematical definition is recursive:

```python
F(n) = F(n - 1) + F(n - 2)
```

So we could write:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

But this creates many repeated calculations.

For example:

```text
F(5)
├── F(4)
│   ├── F(3)
│   └── F(2)
└── F(3)
    ├── F(2)
    └── F(1)
```

`F(3)`, `F(2)`, etc. are calculated repeatedly.

The simple recursive approach therefore has:

```text
O(2^n)
```

time complexity.

The iterative solution avoids this completely.

---

# Iterative vs Recursive

| Approach         |     Time |  Space |
| ---------------- | -------: | -----: |
| Simple Recursion | `O(2^n)` | `O(n)` |
| Iterative        |   `O(n)` | `O(1)` |

For this problem, the **iterative solution is the better approach**.

---

# Complexity

Let:

```text
n = input
```

### Time Complexity

The loop runs exactly `n` times:

```text
O(n)
```

### Space Complexity

Only two variables are used:

```text
a
b
```

Therefore:

```text
O(1)
```

---

# Key Takeaways

* Fibonacci starts with:

  ```text
  F(0) = 0
  F(1) = 1
  ```
* Each next number is:

  ```text
  F(n) = F(n-1) + F(n-2)
  ```
* We only need the **previous two values**.
* Use two variables:

  ```python
  a = 0
  b = 1
  ```
* Update them with:

  ```python
  a, b = b, a + b
  ```
* The iterative approach avoids the repeated calculations of simple recursion.
* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
