# 22. Generate Parentheses

## Problem

Given `n` pairs of parentheses, generate **all possible combinations of well-formed parentheses**.

A combination is valid when:

- Every opening parenthesis `(` has a matching closing parenthesis `)`.
- We never have more closing parentheses than opening parentheses at any point.
- The total number of opening and closing parentheses is exactly `n` each.

---

## Examples

### Example 1

**Input**

```text
n = 3
```

**Output**

```text
["((()))","(()())","(())()","()(())","()()()"]
```

There are `3` pairs of parentheses, and these are all the valid combinations.

---

### Example 2

**Input**

```text
n = 1
```

**Output**

```text
["()"]
```

---

# Approach

We use **Recursion + Backtracking**.

The main idea is to build the parentheses string one character at a time.

At every step, we have two possible choices:

```text
(
)
```

But we cannot blindly add either one.

We have to follow two rules:

### Rule 1: We can add `(` if we still have opening parentheses available.

```python
if open < n:
```

### Rule 2: We can add `)` only if there are more opening parentheses already used than closing parentheses.

```python
if close < open:
```

This prevents invalid strings such as:

```text
")("
```

or:

```text
"())"
```

---

# What Do `open` and `close` Mean?

Our recursive function is:

```python
fun(open, close, current)
```

Where:

```text
open  → number of '(' already used
close → number of ')' already used
current → parentheses string built so far
```

For example:

```text
fun(2, 1, "(()")
```

means:

```text
2 opening parentheses have been used
1 closing parenthesis has been used

current = "(()"
```

---

# Why Can We Add `(`?

We have exactly `n` opening parentheses available.

So as long as:

```python
open < n
```

we can add another:

```python
fun(open + 1, close, current + '(')
```

For example:

```text
n = 3

current = "(("
open = 2
close = 0
```

Since:

```text
2 < 3
```

we can add another `(`:

```text
"((("
```

---

# Why Can We Add `)`?

We can only add a closing parenthesis if there is an unmatched opening parenthesis.

That means:

```python
close < open
```

For example:

```text
current = "(()"
open = 2
close = 1
```

There is one unmatched `(`, so we can add:

```text
")"
```

giving:

```text
"(())"
```

---

# Why Can't We Add `)` When `close == open`?

Suppose:

```text
current = "()"
open = 1
close = 1
```

Every opening parenthesis has already been closed.

If we add another `)`:

```text
"())"
```

the string becomes invalid.

Therefore:

```python
if close < open:
```

is necessary.

---

# Base Case

The recursion stops when:

```python
if open == close == n:
```

This means:

```text
open = n
close = n
```

So we have used all parentheses.

For example, when:

```text
n = 3
```

and:

```text
current = "((()))"
```

we have:

```text
open = 3
close = 3
```

Therefore, the string is complete.

We add it to the answer:

```python
ans.append(current)
```

and stop that recursive path:

```python
return
```

---

# Code

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def fun(open, close, current):

            if open == close == n:
                ans.append(current)
                return

            if open < n:
                fun(open + 1, close, current + '(')

            if close < open:
                fun(open, close + 1, current + ')')

        fun(0, 0, '')

        return ans
```

---

# Dry Run

Consider:

```text
n = 2
```

Initially:

```text
open = 0
close = 0
current = ""
```

Call:

```text
fun(0, 0, "")
```

---

## Step 1: Add `(`

Since:

```text
open < n
0 < 2
```

we can add `(`:

```text
fun(1, 0, "(")
```

Now:

```text
current = "("
open = 1
close = 0
```

---

## Step 2: Add Another `(`

Again:

```text
open < n
1 < 2
```

So:

```text
fun(2, 0, "((")
```

Now:

```text
current = "(("
open = 2
close = 0
```

We cannot add another `(` because:

```text
open = n
```

But we can add `)` because:

```text
close < open
0 < 2
```

So:

```text
fun(2, 1, "(()")
```

---

## Step 3: Add `)`

Now:

```text
open = 2
close = 1
current = "(()"
```

We can add another `)`:

```text
fun(2, 2, "(())")
```

Now:

```text
open == close == n
```

So:

```text
ans = ["(())"]
```

---

# Backtracking to Another Choice

The recursion now goes back to:

```text
fun(1, 0, "(")
```

At this point, we already explored:

```text
"("
   ↓
"(("
   ↓
"(()"
   ↓
"(())"
```

Now we try the **other possible choice**.

Since:

```text
close < open
0 < 1
```

we can add `)`:

```text
fun(1, 1, "()")
```

Now:

```text
current = "()"
open = 1
close = 1
```

We cannot add `)` because:

```text
close < open
1 < 1
```

is false.

But we can add `(`:

```text
fun(2, 1, "()(")
```

Then:

```text
fun(2, 2, "()()")
```

This reaches the base case.

So:

```text
ans = ["(())", "()()"]
```

Final result:

```text
["(())", "()()"]
```

---

# Recursion Tree

For `n = 2`, the recursion roughly looks like:

```text
                    ""
                    |
                   "("
                 /     \
               "(("    "()"
                |        |
              "(()"     "()("
                |        |
             "(())"    "()()"
```

The valid completed strings are:

```text
(())   
()()
```

The important thing is that the recursion explores **different choices** and backtracks to try the alternatives.

---

# Backtracking

Backtracking means:

> Make a choice → continue recursively → when that path is finished, go back and try another choice.

Here, every position can potentially receive:

```text
(
```

or:

```text
)
```

but only when the rules allow it.

For example:

```text
current = "("
```

We can try:

```text
"(("
```

and after completely exploring that path, return and try:

```text
"()"
```

This is why the algorithm can generate **all valid combinations**.

---

# Why Do We Never Explicitly Remove a Character?

Notice that the code doesn't contain something like:

```python
current.pop()
```

because `current` is a **string** and we create a new string on every recursive call:

```python
current + '('
```

or:

```python
current + ')'
```

So each recursive call has its own version of `current`.

For example:

```text
current = "("
```

Calling:

```python
fun(..., current + '(')
```

creates:

```text
"(("
```

while the previous call still has:

```text
"("
```

This naturally handles the backtracking.

---

# Important Conditions

These two conditions are the heart of the solution:

```python
if open < n:
    fun(open + 1, close, current + '(')
```

and:

```python
if close < open:
    fun(open, close + 1, current + ')')
```

### Opening Parenthesis

```text
open < n
```

means:

> We haven't used all the opening parentheses yet.

### Closing Parenthesis

```text
close < open
```

means:

> There is an unmatched opening parenthesis that we can close.

Together, these conditions guarantee that every generated string is valid.

---

# Why Does `close < open` Guarantee Valid Parentheses?

Consider:

```text
current = "(()"
```

We have:

```text
open = 2
close = 1
```

So:

```text
close < open
```

is true.

There is one unmatched `(`.

Therefore, adding `)` is safe:

```text
"(())"
```

But consider:

```text
current = "()"
```

We have:

```text
open = 1
close = 1
```

There are no unmatched opening parentheses.

So:

```text
close < open
```

is false.

We cannot add another `)`.

This prevents invalid prefixes.

---

# Why Does the Base Case Use Both `open` and `close`?

We need exactly `n` pairs.

So we need:

```text
n opening parentheses
n closing parentheses
```

Therefore:

```python
if open == close == n:
```

means the string is completely finished.

For example, with `n = 3`:

```text
open = 3
close = 3
```

means exactly six characters have been placed:

```text
3 '(' + 3 ')'
```

---

# Algorithm

1. Start with:
   ```text
   open = 0
   close = 0
   current = ""
   ```
2. If `open == close == n`:
   - Add `current` to `ans`.
   - Stop this recursive path.
3. If `open < n`:
   - Add `(` and recurse.
4. If `close < open`:
   - Add `)` and recurse.
5. Continue until every valid combination has been generated.
6. Return `ans`.

---

# Complexity

The number of valid combinations is the **nth Catalan number**:

```text
Cₙ = 1/(n+1) × (2n choose n)
```

Since we must actually generate every valid string, the complexity depends on the number of results.

### Time Complexity

There are `Cₙ` valid combinations, and each string has length `2n`.

Therefore:

```text
O(Cₙ × n)
```

More precisely, because strings are constructed along the recursion, the output itself requires `O(Cₙ × n)` space/time.

### Space Complexity

The recursion depth can reach:

```text
2n
```

so the recursion stack uses:

```text
O(n)
```

The answer itself contains:

```text
Cₙ
```

strings of length `2n`, requiring:

```text
O(Cₙ × n)
```

space.

---

# Key Takeaways

- This is a **Backtracking + Recursion** problem.
- `open` tracks how many `(` have been used.
- `close` tracks how many `)` have been used.
- We can add `(` while:
  ```python
  open < n
  ```
- We can add `)` while:
  ```python
  close < open
  ```
- `close < open` prevents invalid parentheses.
- When:
  ```python
  open == close == n
  ```
  we have a complete valid combination.
- The recursion explores every valid possibility.
- **Time Complexity:** `O(Cₙ × n)`
- **Space Complexity:** `O(Cₙ × n)` including the output.

---

## Author

**Ramit Sarker**
