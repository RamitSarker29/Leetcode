# 17. Letter Combinations of a Phone Number

## Problem

Given a string containing digits from `2-9`, return **all possible letter combinations** that the number could represent.

Each digit corresponds to a set of letters, just like the buttons on a telephone keypad.

![Telephone Keypad](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

The mapping is:

```text
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
7 → pqrs
8 → tuv
9 → wxyz
```

The answer can be returned in **any order**.

---

## Examples

### Example 1

**Input**

```text
digits = "23"
```

**Output**

```text
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Explanation**

For `2`, we can choose:

```text
a, b, c
```

For `3`, we can choose:

```text
d, e, f
```

So every possible combination is:

```text
a + d = ad
a + e = ae
a + f = af

b + d = bd
b + e = be
b + f = bf

c + d = cd
c + e = ce
c + f = cf
```

---

### Example 2

**Input**

```text
digits = "2"
```

**Output**

```text
["a","b","c"]
```

---

# Approach

We use **Recursion + Backtracking**.

The main idea is:

> For each digit, try every letter that belongs to that digit.

For example:

```text
digits = "23"
```

The first digit is:

```text
2 → abc
```

So we have three choices:

```text
a
b
c
```

For each of those choices, we move to the next digit:

```text
3 → def
```

This creates a decision tree.

---

# Digit to Letter Mapping

We first create a dictionary:

```python
hash_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
```

For example:

```python
hash_map['2']
```

gives:

```text
"abc"
```

and:

```python
hash_map['7']
```

gives:

```text
"pqrs"
```

This allows us to easily find the possible letters for each digit.

---

# Recursive Function

Our recursive function is:

```python
fun(index, current)
```

where:

```text
index   → which digit we are currently processing
current → combination built so far
```

For example:

```text
fun(1, "a")
```

means:

```text
We have already processed the first digit.
The current combination is "a".
Now process the digit at index 1.
```

---

# Base Case

The base case is:

```python
if index == len(digits):
    ans.append(current)
    return
```

This means we have processed **every digit**.

For:

```text
digits = "23"
```

the indices are:

```text
0 → '2'
1 → '3'
```

When:

```text
index = 2
```

we have processed both digits.

Therefore:

```text
current
```

is a complete combination.

We add it to `ans`.

---

# Recursive Case

The important part is:

```python
for i in hash_map[digits[index]]:
    fun(index + 1, current + i)
```

Suppose:

```text
digits[index] = '2'
```

Then:

```python
hash_map['2']
```

is:

```text
"abc"
```

So the loop tries:

```text
a
b
c
```

For each letter, we recursively process the next digit.

---

# Code

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hash_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ans = []

        def fun(index, current):

            if index == len(digits):
                ans.append(current)
                return

            for i in hash_map[digits[index]]:
                fun(index + 1, current + i)

        fun(0, '')

        return ans
```

---

# Dry Run

Consider:

```text
digits = "23"
```

Initially:

```text
index = 0
current = ""
```

We call:

```python
fun(0, "")
```

---

## First Digit: `2`

```text
2 → abc
```

The loop tries:

```text
a
b
c
```

Let's follow the `a` path first.

We call:

```text
fun(1, "a")
```

---

## Second Digit: `3`

```text
3 → def
```

Now the loop tries:

```text
d
e
f
```

### Choose `d`

```text
current = "a" + "d"
       = "ad"
```

We call:

```text
fun(2, "ad")
```

Since:

```text
index == len(digits)
```

we add:

```text
"ad"
```

to the answer.

---

### Choose `e`

```text
current = "ae"
```

Add:

```text
"ae"
```

---

### Choose `f`

```text
current = "af"
```

Add:

```text
"af"
```

So after processing the `a` branch:

```text
["ad", "ae", "af"]
```

---

## Backtrack to `b`

Now recursion goes back and chooses:

```text
b
```

We get:

```text
"bd"
"be"
"bf"
```

---

## Backtrack to `c`

Finally, choose:

```text
c
```

We get:

```text
"cd"
"ce"
"cf"
```

Final result:

```text
[
    "ad","ae","af",
    "bd","be","bf",
    "cd","ce","cf"
]
```

---

# Recursion Tree

For:

```text
digits = "23"
```

the recursion tree looks like:

```text
                    ""
                  / | \
                 a  b  c
                /|\ /|\ /|\
               d e f d e f d e f
               | | | | | | | | |
              ad ae af bd be bf cd ce cf
```

Each level represents one digit.

```text
Level 0 → ""
Level 1 → choose a letter for '2'
Level 2 → choose a letter for '3'
```

When we reach the last level, we have a complete combination.

---

# Why Is This Backtracking?

At each digit, we make a choice.

For:

```text
2 → abc
```

we first choose:

```text
a
```

and explore everything possible after `a`:

```text
ad
ae
af
```

Then we go back and try:

```text
b
```

giving:

```text
bd
be
bf
```

Then:

```text
c
```

giving:

```text
cd
ce
cf
```

This pattern:

```text
Choose
  ↓
Explore
  ↓
Return
  ↓
Choose another
```

is **backtracking**.

---

# Understanding `index`

The `index` variable tells us **which digit we are currently working on**.

Suppose:

```text
digits = "234"
```

Then:

```text
index = 0 → '2'
index = 1 → '3'
index = 2 → '4'
index = 3 → finished
```

Every recursive call moves forward:

```python
fun(index + 1, ...)
```

So we never process the same digit twice.

---

# Understanding `current`

`current` stores the combination we have built so far.

For example:

```text
fun(0, "")
```

No letters have been chosen.

Then:

```text
fun(1, "a")
```

means we selected `a` for the first digit.

Then:

```text
fun(2, "ad")
```

means:

```text
a → from digit 2
d → from digit 3
```

Now the combination is complete.

---

# Why Use `current + i`?

This line:

```python
fun(index + 1, current + i)
```

adds the selected character to the current combination.

For example:

```text
current = "a"
i = "d"
```

Then:

```text
current + i
```

becomes:

```text
"ad"
```

The recursive call then continues building from `"ad"`.

---

# Why Don't We Need `pop()`?

In many backtracking problems, we see:

```python
current.append(...)
...
current.pop()
```

Here, `current` is a **string**.

Strings are immutable, so:

```python
current + i
```

creates a new string for each recursive call.

For example:

```text
current = "a"
```

Calling:

```python
fun(..., current + "d")
```

creates:

```text
"ad"
```

while the previous call still has:

```text
"a"
```

The original string is unchanged.

So we don't need to manually remove the character afterward.

---

# Important Pattern

This problem follows a very common recursion pattern:

```text
For every possible choice:
    make the choice
    recursively solve the remaining problem
```

In code:

```python
for i in hash_map[digits[index]]:
    fun(index + 1, current + i)
```

This is the core of the solution.

---

# Number of Combinations

Most digits have `3` letters:

```text
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
8 → tuv
```

while `7` and `9` have `4` letters:

```text
7 → pqrs
9 → wxyz
```

For:

```text
digits = "23"
```

we have:

```text
3 × 3 = 9
```

combinations.

For:

```text
digits = "234"
```

we have:

```text
3 × 3 × 3 = 27
```

combinations.

For four digits, the maximum is:

```text
4 × 4 × 4 × 4 = 256
```

---

# Algorithm

1. Create a mapping from each digit to its letters.
2. Create an empty result list.
3. Start recursion from:
   ```text
   index = 0
   current = ""
   ```
4. If all digits have been processed:
   - Add `current` to `ans`.
5. Otherwise:
   - Get the letters corresponding to the current digit.
   - Try each letter.
   - Recursively process the next digit.
6. Return `ans`.

---

# Complexity

Let `n` be the number of digits.

The number of combinations can be as large as:

```text
4ⁿ
```

because digits `7` and `9` have four letters.

Each combination has length `n`.

### Time Complexity

```text
O(4ⁿ × n)
```

This includes constructing and storing the resulting strings.

### Space Complexity

The recursion depth is:

```text
O(n)
```

The result can contain up to:

```text
O(4ⁿ × n)
```

characters.

Therefore, including the output:

```text
O(4ⁿ × n)
```

---

# Key Takeaways

- This is a **Recursion + Backtracking** problem.
- Use a dictionary to map each digit to its letters.
- `index` tells us which digit we're processing.
- `current` stores the combination built so far.
- For every digit, try **every possible letter**.
- When:
  ```python
  index == len(digits)
  ```
  the combination is complete.
- Add the completed combination to `ans`.
- `current + i` creates a new string, so no explicit `pop()` is needed.
- **Time Complexity:** `O(4ⁿ × n)`
- **Space Complexity:** `O(4ⁿ × n)` including the output.

---

## Author

**Ramit Sarker**
