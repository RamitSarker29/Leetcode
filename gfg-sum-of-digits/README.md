# Sum Of Digits

## Problem

Given a positive number `n`, find the **sum of all the digits** of `n`.

---

## Examples

### Example 1

**Input**

```text
n = 687
```

**Output**

```text
21
```

**Explanation**

```text
6 + 8 + 7 = 21
```

---

### Example 2

**Input**

```text
n = 12
```

**Output**

```text
3
```

**Explanation**

```text
1 + 2 = 3
```

---

# Approach

We solve this problem using **Recursion**.

The main idea is to separate the **last digit** from the rest of the number.

For a number:

```text
687
```

we can get the last digit using:

```python
n % 10
```

So:

```text
687 % 10 = 7
```

Then we remove the last digit using:

```python
n // 10
```

So:

```text
687 // 10 = 68
```

Therefore, the problem:

```text
sum of digits of 687
```

becomes:

```text
7 + sum of digits of 68
```

Then:

```text
68
↓
8 + sum of digits of 6
```

And finally:

```text
6
↓
6 + sum of digits of 0
```

---

# Base Case

The most important part of the recursion is:

```python
if n == 0:
    return 0
```

Why `0`?

When `n` becomes `0`, there are no digits left to process.

So the recursion stops and returns:

```text
0
```

This is the **base case**.

---

# Recursive Case

For every other number:

```python
d = n % 10
n = n // 10
ans = fun(n)
return d + ans
```

We:

1. Take the last digit.
2. Remove the last digit.
3. Recursively calculate the sum of the remaining digits.
4. Add the last digit to that result.

---

# Code

```python
class Solution:
    def sumOfDigits(self, n):
        # code here

        def fun(n):

            if n == 0:
                return 0

            d = n % 10
            n = n // 10

            ans = fun(n)

            return d + ans

        return fun(n)
```

---

# Dry Run

Consider:

```text
n = 687
```

We call:

```text
fun(687)
```

---

### Call 1

```text
n = 687
```

Last digit:

```text
d = 687 % 10
d = 7
```

Remove last digit:

```text
n = 687 // 10
n = 68
```

Now:

```text
fun(68)
```

But we don't immediately add `7`.

We first wait for:

```python
ans = fun(68)
```

---

### Call 2

```text
n = 68
```

Last digit:

```text
d = 68 % 10
d = 8
```

Remaining number:

```text
n = 68 // 10
n = 6
```

Call:

```text
fun(6)
```

---

### Call 3

```text
n = 6
```

Last digit:

```text
d = 6 % 10
d = 6
```

Remaining:

```text
n = 6 // 10
n = 0
```

Call:

```text
fun(0)
```

---

### Call 4 — Base Case

```text
n = 0
```

So:

```python
return 0
```

Now the recursion starts **returning back upward**.

---

# Returning From Recursion

This is the part that is important to understand.

We had:

```text
fun(687)
    ↓
fun(68)
    ↓
fun(6)
    ↓
fun(0)
```

`fun(0)` returns:

```text
0
```

Now we go back to:

```text
fun(6)
```

It had:

```text
d = 6
ans = 0
```

Therefore:

```text
return d + ans
     = 6 + 0
     = 6
```

So:

```text
fun(6) → 6
```

---

Now we return to:

```text
fun(68)
```

It had:

```text
d = 8
ans = 6
```

Therefore:

```text
return 8 + 6
     = 14
```

So:

```text
fun(68) → 14
```

---

Finally, we return to:

```text
fun(687)
```

It had:

```text
d = 7
ans = 14
```

Therefore:

```text
return 7 + 14
     = 21
```

Final answer:

```text
21
```

---

# Recursion Visualization

The **calling phase** looks like:

```text
fun(687)
   |
   | d = 7
   ↓
fun(68)
   |
   | d = 8
   ↓
fun(6)
   |
   | d = 6
   ↓
fun(0)
```

At `fun(0)`, we hit the base case.

Then the **returning phase** happens:

```text
fun(0) → 0
   ↑
fun(6) → 6 + 0 = 6
   ↑
fun(68) → 8 + 6 = 14
   ↑
fun(687) → 7 + 14 = 21
```

This is the important pattern:

```text
GO DOWN → reach base case → COME BACK UP
```

---

# Understanding `d`

This line:

```python
d = n % 10
```

extracts the **last digit**.

For example:

```text
687 % 10 = 7
68  % 10 = 8
6   % 10 = 6
```

So recursion processes the digits from **right to left**:

```text
7 → 8 → 6
```

---

# Understanding `n // 10`

This line:

```python
n = n // 10
```

removes the last digit.

For example:

```text
687 // 10 = 68
68  // 10 = 6
6   // 10 = 0
```

So together:

```python
d = n % 10
n = n // 10
```

means:

```text
Take the last digit
        ↓
Remove the last digit
        ↓
Solve the smaller number
```

---

# Why Is `n == 0` the Base Case?

Consider:

```text
687
```

Every recursive call removes one digit:

```text
687
 ↓
68
 ↓
6
 ↓
0
```

Once we reach `0`, there are no digits remaining.

Therefore:

```python
if n == 0:
    return 0
```

tells the recursion:

> There is nothing left to add, so stop.

---

# Why Do We Return `d + ans`?

Suppose:

```text
n = 68
```

We separate it into:

```text
8 + 6
```

The current function knows only the last digit:

```text
d = 8
```

The recursive call calculates the sum of the remaining digits:

```text
ans = fun(6)
```

So the complete answer is:

```text
d + ans
```

which is:

```text
8 + 6 = 14
```

That's why:

```python
return d + ans
```

is the heart of the recursive solution.

---

# Algorithm

1. If `n == 0`, return `0`.
2. Extract the last digit:

   ```python
   d = n % 10
   ```
3. Remove the last digit:

   ```python
   n = n // 10
   ```
4. Recursively calculate the sum of the remaining digits.
5. Add the current digit to the recursive result.
6. Return the final sum.

---

# Complexity

Let:

```text
d = number of digits in n
```

We make one recursive call for each digit.

### Time Complexity

```text
O(d)
```

Since the number of digits is approximately `log₁₀(n)`:

```text
O(log n)
```

### Space Complexity

Each recursive call is stored on the recursion call stack.

There is one call per digit:

```text
O(d)
```

or:

```text
O(log n)
```

---

# Key Takeaways

* Use `% 10` to get the **last digit**.
* Use `// 10` to **remove the last digit**.
* The base case is:

  ```python
  if n == 0:
      return 0
  ```
* Each recursive call solves a smaller version of the same problem.
* `d` stores the current digit.
* `ans` stores the sum returned by the recursive call.
* The final result is:

  ```python
  return d + ans
  ```
* Recursion first goes **down** until the base case.
* Then it comes **back up**, calculating the answer.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(log n)`

---

## Author

**Ramit Sarker**
