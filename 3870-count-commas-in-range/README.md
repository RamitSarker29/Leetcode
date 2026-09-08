# 4245. Count Commas in Range

## Problem

You are given an integer `n`.

Return the **total number of commas** used when writing all integers from:

```text
[1, n]
```

using standard number formatting.

In standard formatting:

- A comma is inserted after every three digits from the right.
- Numbers with fewer than 4 digits contain no commas.

For example:

```text
999     → no comma
1,000   → 1 comma
1,001   → 1 comma
10,000  → 1 comma
```

---

# Examples

## Example 1

**Input:**

```text
n = 1002
```

**Output:**

```text
3
```

**Explanation:**

The numbers from `1` to `1002` that contain commas are:

```text
1,000
1,001
1,002
```

Each contains exactly one comma.

Therefore:

```text
1 + 1 + 1 = 3
```

So the answer is:

```text
3
```

---

## Example 2

**Input:**

```text
n = 998
```

**Output:**

```text
0
```

**Explanation:**

Every number from `1` to `998` has at most 3 digits.

Therefore, none of them contains a comma.

```text
Total commas = 0
```

---

# Approach

The key observation is that **the first comma appears when we reach `1000`**.

Numbers below `1000` have no commas:

```text
1
10
100
999
```

Starting from `1000`, every number up to `n` has exactly **one comma** because `n ≤ 10^5`.

For example:

```text
1,000
1,001
...
9,999
10,000
...
99,999
```

Each of these numbers contains exactly one comma.

Therefore, if:

```text
n < 1000
```

the answer is:

```text
0
```

Otherwise, the numbers containing commas are:

```text
1000, 1001, 1002, ..., n
```

The number of integers in this range is:

```text
n - 1000 + 1
```

which simplifies to:

```text
n - 999
```

---

# Understanding the Code

Your solution is:

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n // 1000 == 0:
            return 0
        else:
            return n - 1000 + 1
```

Let's understand each part.

---

## Step 1: Check Whether `n` Is Less Than 1000

```python
if n // 1000 == 0:
    return 0
```

Integer division by `1000` tells us whether `n` has reached at least `1000`.

For example:

```text
998 // 1000 = 0
999 // 1000 = 0
1000 // 1000 = 1
1002 // 1000 = 1
5000 // 1000 = 5
```

So when:

```python
n // 1000 == 0
```

we know:

```text
n < 1000
```

and therefore no number from `1` to `n` contains a comma.

We simply return:

```text
0
```

---

# Step 2: Count Numbers Starting From 1000

If:

```text
n >= 1000
```

then the first number containing a comma is:

```text
1,000
```

We need to count how many numbers exist from `1000` through `n`.

The formula for counting integers in an inclusive range `[a, b]` is:

```text
b - a + 1
```

Here:

```text
a = 1000
b = n
```

Therefore:

```text
n - 1000 + 1
```

Your code uses exactly this:

```python
return n - 1000 + 1
```

---

# Why Does `+1` Matter?

Suppose:

```text
n = 1000
```

There is exactly one number containing a comma:

```text
1,000
```

Using:

```text
1000 - 1000 = 0
```

would incorrectly give `0`.

So we add `1`:

```text
1000 - 1000 + 1
= 1
```

Correct.

The `+1` is needed because both endpoints are included.

---

# Dry Run

Let's dry run:

```text
n = 1002
```

### Step 1

Calculate:

```text
1002 // 1000
```

Result:

```text
1
```

So:

```python
n // 1000 == 0
```

is:

```text
False
```

Therefore, we go to the `else` block.

---

### Step 2

Calculate:

```text
n - 1000 + 1
```

Substitute `n = 1002`:

```text
1002 - 1000 + 1
```

```text
2 + 1
```

```text
3
```

Return:

```text
3
```

The three numbers are:

```text
1,000
1,001
1,002
```

So the answer is correct.

---

# Dry Run for `n = 998`

Now consider:

```text
n = 998
```

Calculate:

```text
998 // 1000
```

Result:

```text
0
```

Therefore:

```python
if n // 1000 == 0:
```

is true.

We immediately return:

```text
0
```

No numbers from `1` to `998` contain commas.

---

# Dry Run for `n = 1000`

Consider:

```text
n = 1000
```

First:

```text
1000 // 1000 = 1
```

So we enter the `else` block.

Calculate:

```text
1000 - 1000 + 1
```

```text
1
```

The only number containing a comma is:

```text
1,000
```

Therefore:

```text
Answer = 1
```

---

# Dry Run for `n = 5000`

Consider:

```text
n = 5000
```

First:

```text
5000 // 1000 = 5
```

So `n` is at least `1000`.

Now:

```text
5000 - 1000 + 1
```

```text
4001
```

Therefore:

```text
Answer = 4001
```

The numbers containing commas are:

```text
1000, 1001, 1002, ..., 5000
```

There are `4001` numbers in this inclusive range.

---

# Visualizing the Idea

The entire range can be divided into two parts:

```text
1 ─────────────────── 999 | 1000 ─────────────── n
       No commas              Has comma
```

Therefore:

```text
Numbers with no comma:
1 → 999

Numbers with a comma:
1000 → n
```

The first part contributes:

```text
0
```

The second part contributes:

```text
n - 1000 + 1
```

So:

```text
Answer =
    0                         if n < 1000
    n - 1000 + 1              if n >= 1000
```

---

# Why Does It Work?

Because of the constraint:

```text
n <= 10^5
```

we never need to worry about numbers having **two or more commas**.

For example:

```text
1,000       → 1 comma
9,999       → 1 comma
10,000      → 1 comma
99,999      → 1 comma
100,000     → 1 comma
```

Even `100,000` contains only one comma.

Therefore, every number from `1000` to `n` contributes exactly **one comma**.

So the problem becomes simply:

> How many integers are there from `1000` to `n`?

The answer is:

```text
n - 1000 + 1
```

---

# Algorithm

1. Check whether `n // 1000 == 0`.
2. If true, `n < 1000`, so return `0`.
3. Otherwise, count the integers from `1000` through `n`.
4. Use:
   ```text
   n - 1000 + 1
   ```
5. Return the result.

---

# Code

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n // 1000 == 0:
            return 0
        else:
            return n - 1000 + 1
```

---

# Complexity

### Time Complexity

```text
O(1)
```

The solution performs only a few arithmetic operations.

It does not loop through any of the numbers from `1` to `n`.

### Space Complexity

```text
O(1)
```

Only a constant amount of memory is used.

---

# Key Takeaways

- The first number containing a comma is **1000**.
- Every number below `1000` contributes `0` commas.
- Because `n ≤ 10^5`, every number from `1000` to `n` contains exactly **one comma**.
- `n // 1000 == 0` tells us that `n < 1000`.
- For `n >= 1000`, the number of comma-containing integers is:
  ```text
  n - 1000 + 1
  ```
- No iteration is necessary.
- Time complexity: `O(1)`.
- Space complexity: `O(1)`.

---

## Author

**Ramit Sarker**
