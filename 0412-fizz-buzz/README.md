# 412 - Fizz Buzz

## Problem

Given an integer `n`, return a string array `answer` containing the numbers from `1` to `n`, following these rules:

- If a number is divisible by **both 3 and 5**, add `"FizzBuzz"`.
- If a number is divisible by **3**, add `"Fizz"`.
- If a number is divisible by **5**, add `"Buzz"`.
- Otherwise, add the number itself as a **string**.

The result is **1-indexed**, meaning we start checking from `1`.

---

# Examples

## Example 1

```text
Input:
n = 3

Output:
["1","2","Fizz"]
```

Explanation:

```text
1 → "1"
2 → "2"
3 → "Fizz"
```

---

## Example 2

```text
Input:
n = 5

Output:
["1","2","Fizz","4","Buzz"]
```

Explanation:

```text
1 → "1"
2 → "2"
3 → "Fizz"
4 → "4"
5 → "Buzz"
```

---

## Example 3

```text
Input:
n = 15

Output:
["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

The important case is `15`:

```text
15 % 3 == 0
15 % 5 == 0
```

So:

```text
15 → "FizzBuzz"
```

---

# Approach

We simply traverse every number from `1` to `n`.

For each number `i`, we check the conditions in this order:

```text
1. Divisible by both 3 and 5 → FizzBuzz
2. Divisible by 3 → Fizz
3. Divisible by 5 → Buzz
4. Otherwise → number as string
```

We store each result in the `ans` list.

---

# Code

```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')

            elif i % 3 == 0:
                ans.append('Fizz')

            elif i % 5 == 0:
                ans.append('Buzz')

            else:
                ans.append(str(i))

        return ans
```

---

# Explanation

## Step 1: Create an Empty List

```python
ans = []
```

This list will store the final answers.

For example:

```text
ans = []
```

After processing some numbers, it might become:

```text
ans = ["1", "2", "Fizz", "4"]
```

---

## Step 2: Loop From 1 to n

```python
for i in range(1, n + 1):
```

Python's `range()` excludes the ending value.

Therefore, to include `n`, we use:

```text
range(1, n + 1)
```

For:

```text
n = 5
```

the loop gives:

```text
1 → 2 → 3 → 4 → 5
```

---

# Step 3: Check FizzBuzz First

```python
if i % 3 == 0 and i % 5 == 0:
    ans.append('FizzBuzz')
```

This checks whether `i` is divisible by **both 3 and 5**.

For example:

```text
i = 15
```

Then:

```text
15 % 3 = 0
15 % 5 = 0
```

Both conditions are true.

Therefore:

```text
"FizzBuzz"
```

is added.

---

# Why Do We Check FizzBuzz First?

This is very important.

Consider:

```text
i = 15
```

Since `15` is divisible by `3`:

```text
15 % 3 == 0
```

is true.

It is also divisible by `5`:

```text
15 % 5 == 0
```

is true.

If we checked only:

```python
if i % 3 == 0:
    ans.append("Fizz")
```

first, `15` would become:

```text
"Fizz"
```

and the program would never reach the `"FizzBuzz"` condition.

Therefore, the combined condition must come **first**.

---

# Step 4: Check Divisibility by 3

```python
elif i % 3 == 0:
    ans.append('Fizz')
```

If the number wasn't divisible by both `3` and `5`, we check whether it is divisible by `3`.

For example:

```text
i = 6
```

Since:

```text
6 % 3 = 0
```

we append:

```text
"Fizz"
```

---

# Step 5: Check Divisibility by 5

```python
elif i % 5 == 0:
    ans.append('Buzz')
```

If the number wasn't handled by the previous conditions, we check whether it is divisible by `5`.

For example:

```text
i = 10
```

Since:

```text
10 % 5 = 0
```

we append:

```text
"Buzz"
```

---

# Step 6: Otherwise Add the Number

```python
else:
    ans.append(str(i))
```

If the number is not divisible by either `3` or `5`, we add the number itself.

However, the answer must contain **strings**, not integers.

Therefore we use:

```python
str(i)
```

For example:

```text
i = 7
```

becomes:

```text
"7"
```

---

# Understanding `%`

The `%` operator gives the **remainder** after division.

For example:

```text
9 % 3 = 0
```

Since the remainder is `0`, `9` is divisible by `3`.

Similarly:

```text
10 % 5 = 0
```

So `10` is divisible by `5`.

But:

```text
7 % 3 = 1
```

Therefore, `7` is not divisible by `3`.

---

# Dry Run

Let's take:

```text
n = 15
```

Initially:

```text
ans = []
```

---

### `i = 1`

```text
1 % 3 != 0
1 % 5 != 0
```

Go to `else`:

```text
ans = ["1"]
```

---

### `i = 2`

```text
2 % 3 != 0
2 % 5 != 0
```

So:

```text
ans = ["1", "2"]
```

---

### `i = 3`

```text
3 % 3 == 0
```

So:

```text
ans = ["1", "2", "Fizz"]
```

---

### `i = 4`

Not divisible by `3` or `5`.

```text
ans = ["1", "2", "Fizz", "4"]
```

---

### `i = 5`

```text
5 % 5 == 0
```

So:

```text
ans = ["1", "2", "Fizz", "4", "Buzz"]
```

---

### `i = 6`

```text
6 % 3 == 0
```

So:

```text
ans = ["1", "2", "Fizz", "4", "Buzz", "Fizz"]
```

---

### `i = 7`

Not divisible by `3` or `5`.

```text
ans = [..., "7"]
```

---

### `i = 8`

Not divisible by `3` or `5`.

```text
ans = [..., "8"]
```

---

### `i = 9`

```text
9 % 3 == 0
```

So:

```text
9 → "Fizz"
```

---

### `i = 10`

```text
10 % 5 == 0
```

So:

```text
10 → "Buzz"
```

---

### `i = 11`

Neither condition is true:

```text
11 → "11"
```

---

### `i = 12`

```text
12 % 3 == 0
```

So:

```text
12 → "Fizz"
```

---

### `i = 13`

```text
13 → "13"
```

---

### `i = 14`

```text
14 → "14"
```

---

### `i = 15`

Now both conditions are true:

```text
15 % 3 == 0
15 % 5 == 0
```

Therefore:

```text
15 → "FizzBuzz"
```

Final result:

```text
["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

---

# Dry Run Table

| `i` | `i % 3` | `i % 5` | Result |
|---:|---:|---:|---|
| 1 | 1 | 1 | `"1"` |
| 2 | 2 | 2 | `"2"` |
| 3 | 0 | 3 | `"Fizz"` |
| 4 | 1 | 4 | `"4"` |
| 5 | 2 | 0 | `"Buzz"` |
| 6 | 0 | 1 | `"Fizz"` |
| 7 | 1 | 2 | `"7"` |
| 8 | 2 | 3 | `"8"` |
| 9 | 0 | 4 | `"Fizz"` |
| 10 | 1 | 0 | `"Buzz"` |
| 11 | 2 | 1 | `"11"` |
| 12 | 0 | 2 | `"Fizz"` |
| 13 | 1 | 3 | `"13"` |
| 14 | 2 | 4 | `"14"` |
| 15 | 0 | 0 | `"FizzBuzz"` |

---

# `if` vs `elif`

The use of `elif` here is important.

Your structure is:

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...
```

Once one condition becomes true, Python executes that block and **skips the remaining conditions**.

For example, for:

```text
i = 15
```

the first condition is true:

```python
i % 3 == 0 and i % 5 == 0
```

So Python appends:

```text
"FizzBuzz"
```

and does not check the `elif` conditions.

This is exactly what we want.

---

# What Would Happen With Separate `if` Statements?

If we wrote:

```python
if i % 3 == 0:
    ans.append("Fizz")

if i % 5 == 0:
    ans.append("Buzz")
```

then for `15`, **both** conditions would execute:

```text
15 → "Fizz"
15 → "Buzz"
```

That is not the required output.

We need:

```text
15 → "FizzBuzz"
```

Therefore, using:

```python
if
elif
elif
else
```

makes the conditions mutually exclusive.

---

# Why Does It Work?

Every integer falls into exactly one of these categories:

```text
                    Number
                       |
              Is it divisible
                by 3 AND 5?
                /          \
              Yes           No
               |             |
          "FizzBuzz"    Divisible by 3?
                           /       \
                         Yes        No
                          |          |
                       "Fizz"   Divisible by 5?
                                   /      \
                                 Yes       No
                                  |         |
                               "Buzz"    Number
```

Because the conditions are checked in the correct order, every number receives exactly the required output.

---

# Algorithm

```text
1. Create an empty list ans.

2. Loop from 1 to n.

3. For every number i:

   If i is divisible by both 3 and 5:
       Add "FizzBuzz"

   Else if i is divisible by 3:
       Add "Fizz"

   Else if i is divisible by 5:
       Add "Buzz"

   Else:
       Add i as a string

4. Return ans.
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

We process every number from `1` to `n` exactly once.

---

## Space Complexity

```text
O(n)
```

The result array contains `n` strings.

The extra working space apart from the required output is `O(1)`.

---

# Concepts Used

- Arrays / Lists
- Loops
- Conditional Statements
- Modulo Operator
- `if / elif / else`
- String Conversion
- One-Pass Traversal

---

# Python Features Used

### `range()`

```python
range(1, n + 1)
```

Generates numbers from `1` through `n`.

### Modulo `%`

```python
i % 3 == 0
```

Checks divisibility.

### `append()`

```python
ans.append("Fizz")
```

Adds an element to the result list.

### `str()`

```python
str(i)
```

Converts an integer into a string.

---

# Key Takeaways

- Traverse from `1` to `n`.
- Use `%` to check divisibility.
- Check **both 3 and 5 first**.
- Use `elif` so that only one result is added for each number.
- `15` is `"FizzBuzz"` because it is divisible by both `3` and `5`.
- Convert ordinary numbers using `str(i)` because the output must contain strings.
- Time Complexity: **O(n)**.
- Output Space: **O(n)**.

---

## Author

**Ramit Sarker**
