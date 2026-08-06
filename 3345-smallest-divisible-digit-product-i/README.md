# 3345. Smallest Divisible Digit Product I

## Problem

You are given two integers:

- `n`
- `t`

Return the **smallest integer greater than or equal to `n`** such that the **product of its digits** is divisible by `t`.

---

## Examples

### Example 1

**Input**

```text
n = 10
t = 2
```

**Output**

```text
10
```

**Explanation**

Digit product:

```text
1 × 0 = 0
```

Since

```text
0 % 2 == 0
```

the answer is `10`.

---

### Example 2

**Input**

```text
n = 15
t = 3
```

**Output**

```text
16
```

**Explanation**

```text
15

1 × 5 = 5

5 % 3 != 0
```

Next number:

```text
16

1 × 6 = 6

6 % 3 == 0
```

Hence, the answer is `16`.

---

# Intuition

Starting from `n`, check every number one by one.

For each number:

1. Find the product of all its digits.
2. Check whether the product is divisible by `t`.
3. If it is, return the number.
4. Otherwise, increment the number and repeat.

Since the constraints are small (`n ≤ 100`), a brute-force approach is sufficient.

---

# Approach

### Step 1

Create a helper function to calculate the product of all digits.

Extract each digit using:

```python
digit = n % 10
```

Multiply it with the running product.

```python
product *= digit
```

Remove the last digit.

```python
n //= 10
```

Continue until all digits are processed.

---

### Step 2

Starting from `n`, repeatedly check every number.

```python
while True:
```

---

### Step 3

Calculate its digit product.

```python
digit_product(n)
```

---

### Step 4

If the product is divisible by `t`,

return the current number.

```python
if digit_product(n) % t == 0:
    return n
```

---

### Step 5

Otherwise,

move to the next number.

```python
n += 1
```

Repeat until the answer is found.

---

# Algorithm

1. Create a function to calculate the product of all digits.
2. Start checking from `n`.
3. If the digit product is divisible by `t`, return the number.
4. Otherwise, increment `n`.
5. Repeat until a valid number is found.

---

# Code

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(n):
            product = 1
            while n != 0:
                digit = n % 10
                product *= digit
                n //= 10
            return product

        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1
```

---

# Dry Run

### Example

```text
n = 15
t = 3
```

### Check 15

Digit product:

```text
1 × 5 = 5
```

```text
5 % 3 != 0
```

Not valid.

Increment:

```text
n = 16
```

---

### Check 16

Digit product:

```text
1 × 6 = 6
```

```text
6 % 3 == 0
```

Return:

```text
16
```

---

# Why Does This Work?

The algorithm checks every integer starting from `n` in increasing order.

The first number whose digit product is divisible by `t` is immediately returned.

Since the numbers are checked in ascending order, the returned value is guaranteed to be the **smallest valid number**.

---

# Time Complexity

Let:

- `d` = number of digits in `n`
- `k` = number of numbers checked before finding the answer

Each digit product calculation takes:

```text
O(d)
```

Overall:

```text
O(k × d)
```

Since `n ≤ 100`, `d` is at most `3`, making the solution efficient.

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Brute Force
- Simulation
- Number Manipulation
- Modulo Arithmetic

---

# Python Features Used

### Modulo

```python
digit = n % 10
```

Extracts the last digit.

---

### Floor Division

```python
n //= 10
```

Removes the last digit.

---

### Infinite Loop

```python
while True:
```

Continues checking numbers until a valid answer is found.

---

# Key Takeaways

- Use `% 10` to extract the last digit.
- Use `// 10` to remove the last digit.
- Compute the product of all digits using a helper function.
- Check each number starting from `n`.
- Return the first number whose digit product is divisible by `t`.
- The solution uses a simple brute-force approach and is efficient because of the small constraints.

---

## Author

**Ramit Sarker**
