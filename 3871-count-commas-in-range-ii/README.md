# 4248. Count Commas in Range II

## Problem

You are given an integer `n`.

Return the **total number of commas** used when writing every integer from `1` to `n` in standard number formatting.

In standard formatting:

- A comma is inserted after every **three digits** from the right.
- Numbers with fewer than **4 digits** contain no commas.

For example:

```text
1000     → 1,000      → 1 comma
10000    → 10,000     → 1 comma
1000000  → 1,000,000  → 2 commas
```

The goal is to count **all commas used across every number from `1` to `n`**.

---

# Example 1

```text
Input:
n = 1002

Output:
3
```

### Explanation

The numbers containing commas are:

```text
1,000 → 1 comma
1,001 → 1 comma
1,002 → 1 comma
```

Therefore:

```text
1 + 1 + 1 = 3
```

---

# Example 2

```text
Input:
n = 998

Output:
0
```

### Explanation

Every number from `1` to `998` has fewer than four digits.

Therefore, no commas are required.

```text
Answer = 0
```

---

# Key Observation

The first number that requires a comma is:

```text
1000
```

Every number from:

```text
1000 → n
```

contains **at least one comma**.

So the number of integers from `1000` to `n` is:

```text
n - 1000 + 1
```

The `+1` is important because both `1000` and `n` are included.

---

# Multiple Commas

For larger numbers, a number can contain more than one comma.

For example:

```text
1,000       → 1 comma
1,000,000   → 2 commas
1,000,000,000 → 3 commas
```

Therefore, we can count commas in layers.

### First comma

Every number from:

```text
1000 → n
```

contributes at least one comma.

Count:

```text
n - 1000 + 1
```

---

### Second comma

Every number from:

```text
1,000,000 → n
```

has at least two commas.

The **additional** comma can therefore be counted for every number starting from `1,000,000`.

Count:

```text
n - 1000000 + 1
```

---

### Third comma

Every number from:

```text
1,000,000,000 → n
```

has at least three commas.

Count:

```text
n - 1000000000 + 1
```

---

### Fourth comma

Every number from:

```text
1,000,000,000,000 → n
```

has at least four commas.

Count:

```text
n - 1000000000000 + 1
```

---

### Fifth comma

Every number from:

```text
1,000,000,000,000,000 → n
```

has at least five commas.

Count:

```text
n - 1000000000000000 + 1
```

Since the constraint is:

```text
n <= 10^15
```

these are all the comma thresholds that need to be considered.

---

# Approach

Your solution handles the different ranges of `n` using a sequence of conditions.

First:

```python
if n // 1000 == 0:
    return 0
```

If `n < 1000`, there are no numbers containing commas.

Otherwise, the code checks how large `n` is.

For example, if `n` is at least:

```text
1,000,000
```

then we know that both the first and second comma layers contribute.

So:

```python
(n - 1000 + 1) + (n - 1000000 + 1)
```

counts the total commas.

For even larger values, additional thresholds are added.

---

# Code

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n // 1000 == 0:
            return 0

        if (n // 1000 >= 1 and
            n // 1000000 >= 1 and
            n // 1000000000 >= 1 and
            n // 1000000000000 >= 1 and
            n // 1000000000000000 >= 1):

            return ((n - 1000 + 1) +
                    (n - 1000000 + 1) +
                    (n - 1000000000 + 1) +
                    (n - 1000000000000 + 1) +
                    (n - 1000000000000000 + 1))

        if (n // 1000 >= 1 and
            n // 1000000 >= 1 and
            n // 1000000000 >= 1 and
            n // 1000000000000 >= 1):

            return ((n - 1000 + 1) +
                    (n - 1000000 + 1) +
                    (n - 1000000000 + 1) +
                    (n - 1000000000000 + 1))

        if (n // 1000 >= 1 and
            n // 1000000 >= 1 and
            n // 1000000000 >= 1):

            return ((n - 1000 + 1) +
                    (n - 1000000 + 1) +
                    (n - 1000000000 + 1))

        if n // 1000 >= 1 and n // 1000000 >= 1:
            return ((n - 1000 + 1) +
                    (n - 1000000 + 1))

        if n // 1000 >= 1:
            return n - 1000 + 1
```

---

# Dry Run 1

Let's take:

```text
n = 1002
```

### Step 1

Check:

```python
n // 1000
```

We get:

```text
1002 // 1000 = 1
```

So:

```python
if n // 1000 == 0:
```

is false.

---

### Step 2

Check whether `n` is at least `1,000,000`.

```text
1002 // 1000000 = 0
```

So the larger-range conditions are false.

Eventually we reach:

```python
if n // 1000 >= 1:
    return n - 1000 + 1
```

Substitute:

```text
1002 - 1000 + 1
= 3
```

Therefore:

```text
Answer = 3
```

Which matches:

```text
1,000
1,001
1,002
```

---

# Dry Run 2

Let's take:

```text
n = 1000002
```

Now:

```text
n >= 1000
n >= 1000000
```

but:

```text
n < 1000000000
```

Therefore, the code uses:

```python
(n - 1000 + 1) + (n - 1000000 + 1)
```

Calculate the first contribution:

```text
1000002 - 1000 + 1
= 999003
```

Second contribution:

```text
1000002 - 1000000 + 1
= 3
```

Total:

```text
999003 + 3
= 999006
```

So:

```text
Answer = 999006
```

The first term counts the first comma for every number from `1000` onward.

The second term counts the **additional comma** for the numbers from `1,000,000` onward.

---

# Dry Run 3

Consider:

```text
n = 1000000000
```

This number has three comma positions:

```text
1,000,000,000
```

The code counts:

### First layer

```text
1000000000 - 1000 + 1
```

### Second layer

```text
1000000000 - 1000000 + 1
```

### Third layer

```text
1000000000 - 1000000000 + 1
```

The third term is:

```text
1
```

because exactly one number, `1,000,000,000`, reaches the third comma threshold.

Therefore the solution correctly counts all three layers.

---

# Why Does It Work?

Instead of examining every number individually, the solution groups numbers according to the **number of commas they must contain**.

For example:

```text
Range                         Additional comma
------------------------------------------------
1000 → n                      1st comma
1000000 → n                   2nd comma
1000000000 → n                3rd comma
1000000000000 → n             4th comma
1000000000000000 → n          5th comma
```

This is the main idea.

A number such as:

```text
1,234,567
```

contains two commas.

It gets counted once by:

```text
n - 1000 + 1
```

and once more by:

```text
n - 1000000 + 1
```

Therefore it contributes exactly:

```text
2 commas
```

to the answer.

Similarly:

```text
1,234,567,890
```

gets counted in three layers and therefore contributes three commas.

---

# Understanding `n - threshold + 1`

This expression appears repeatedly:

```python
n - threshold + 1
```

It calculates the number of integers in the inclusive range:

```text
[threshold, n]
```

For example:

```text
n = 1002
threshold = 1000
```

Numbers are:

```text
1000
1001
1002
```

There are `3` numbers.

Using the formula:

```text
1002 - 1000 + 1
= 3
```

---

# Why Use `n // 1000`?

The expression:

```python
n // 1000
```

is used to determine whether `n` has reached the first comma threshold.

If:

```text
n < 1000
```

then:

```text
n // 1000 = 0
```

So:

```python
if n // 1000 == 0:
    return 0
```

immediately handles all values below `1000`.

For example:

```text
998 // 1000 = 0
```

Therefore:

```text
Answer = 0
```

---

# Comma Thresholds

The important thresholds are:

```text
1,000
1,000,000
1,000,000,000
1,000,000,000,000
1,000,000,000,000,000
```

Or numerically:

```text
10^3
10^6
10^9
10^12
10^15
```

Each threshold represents the point where an **additional comma** starts appearing.

---

# Algorithm

```text
1. If n < 1000:
       return 0

2. If n reaches 10^15:
       count contributions from 10^3, 10^6, 10^9, 10^12 and 10^15

3. Otherwise, if n reaches 10^12:
       count contributions from 10^3, 10^6, 10^9 and 10^12

4. Otherwise, if n reaches 10^9:
       count contributions from 10^3, 10^6 and 10^9

5. Otherwise, if n reaches 10^6:
       count contributions from 10^3 and 10^6

6. Otherwise:
       count contribution from 10^3

7. Return the total.
```

---

# Complexity Analysis

### Time Complexity

```text
O(1)
```

There is no loop that depends on `n`.

The solution performs only a fixed number of arithmetic operations and condition checks.

---

### Space Complexity

```text
O(1)
```

Only a few integer variables and arithmetic expressions are used.

No additional data structures are required.

---

# Key Takeaways

- The first comma appears at `1000`.
- Every number from `1000` onward contributes at least one comma.
- Every number from `1,000,000` onward contributes an **additional** comma.
- Every number from `1,000,000,000` onward contributes another additional comma.
- The same pattern continues for `10^12` and `10^15`.
- `n - threshold + 1` counts the numbers in the inclusive range `[threshold, n]`.
- The solution handles the entire range up to `10^15` in **O(1)** time.
- No iteration through the numbers from `1` to `n` is required.

---

## Author

**Ramit Sarker**
