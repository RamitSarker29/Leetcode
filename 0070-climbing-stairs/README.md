# 70. Climbing Stairs

## Problem

You are climbing a staircase with `n` steps.

At each move, you can climb either:

- `1` step
- `2` steps

The task is to find the **total number of distinct ways** to reach the top.

The **order matters**.

For example:

```text
1 + 2
```

and

```text
2 + 1
```

are two different ways.

---

# Example 1

```text
Input:
n = 2

Output:
2
```

There are two ways:

```text
1 + 1
2
```

Therefore:

```text
Answer = 2
```

---

# Example 2

```text
Input:
n = 3

Output:
3
```

The three ways are:

```text
1 + 1 + 1
1 + 2
2 + 1
```

Therefore:

```text
Answer = 3
```

---

# Key Idea

The most important observation is:

> To reach step `n`, the last move must either be `1` step or `2` steps.

So there are only two possibilities:

```text
Reach n from n-1
```

or

```text
Reach n from n-2
```

Therefore:

```text
ways(n) = ways(n-1) + ways(n-2)
```

This is exactly the same pattern as the Fibonacci sequence.

---

# Understanding the Recurrence

Suppose:

```text
n = 5
```

To reach step `5`, we can come from:

```text
4 → 5
```

or:

```text
3 → 5
```

So:

```text
ways(5) = ways(4) + ways(3)
```

Similarly:

```text
ways(4) = ways(3) + ways(2)
```

and:

```text
ways(3) = ways(2) + ways(1)
```

Our base cases are:

```text
ways(1) = 1
ways(2) = 2
```

Therefore:

```text
ways(3) = 2 + 1 = 3
ways(4) = 3 + 2 = 5
ways(5) = 5 + 3 = 8
```

So yes:

```text
n = 5 → Answer = 8
```

---

# Why Do We Need `dp`?

A simple recursive solution would repeatedly calculate the same values.

For example:

```text
fun(5)
├── fun(4)
│   ├── fun(3)
│   │   ├── fun(2)
│   │   └── fun(1)
│   └── fun(2)
└── fun(3)
    ├── fun(2)
    └── fun(1)
```

Notice that:

```text
fun(3)
fun(2)
fun(1)
```

are calculated multiple times.

This creates unnecessary work.

To avoid this, we use:

```python
dp = {}
```

The dictionary stores answers that we have already calculated.

This technique is called **memoization**.

---

# How `dp` Stores the Answer

Suppose we calculate:

```text
fun(3)
```

We know:

```text
fun(3) = fun(2) + fun(1)
       = 2 + 1
       = 3
```

So we store:

```python
dp[3] = 3
```

The dictionary now looks like:

```text
dp = {
    3: 3
}
```

Later, if we need `fun(3)` again:

```python
if n in dp:
    return dp[n]
```

Since `3` is already stored, we immediately return:

```text
3
```

We don't calculate it again.

---

# Approach

We use **Recursion + Memoization**.

### Step 1: Create a dictionary

```python
dp = {}
```

This stores already calculated results.

---

### Step 2: Define the recursive function

```python
def fun(n):
```

`fun(n)` represents:

> The number of ways to climb exactly `n` remaining steps.

---

### Step 3: Handle the base cases

```python
if n == 1:
    return 1
```

There is only one way to climb one step:

```text
1
```

And:

```python
if n == 2:
    return 2
```

There are two ways:

```text
1 + 1
2
```

---

### Step 4: Check whether the answer is already stored

```python
if n in dp:
    return dp[n]
```

If we have already calculated `fun(n)`, return the stored result.

This prevents repeated calculations.

---

### Step 5: Calculate the answer

```python
dp[n] = fun(n - 1) + fun(n - 2)
```

The last move is either:

```text
1 step
```

or:

```text
2 steps
```

Therefore:

```text
ways(n) = ways(n-1) + ways(n-2)
```

---

### Step 6: Return the stored answer

```python
return dp[n]
```

Finally:

```python
return fun(n)
```

starts the recursion from the original `n`.

---

# Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def fun(n):
            if n == 1:
                return 1

            if n == 2:
                return 2

            if n in dp:
                return dp[n]

            dp[n] = fun(n - 1) + fun(n - 2)

            return dp[n]

        return fun(n)
```

---

# Dry Run

Let's take:

```text
n = 5
```

We call:

```python
fun(5)
```

---

## Step 1: `fun(5)`

`5` is neither `1` nor `2`.

Also:

```text
5 not in dp
```

So:

```python
dp[5] = fun(4) + fun(3)
```

We need to calculate `fun(4)` and `fun(3)`.

---

## Step 2: `fun(4)`

Again, `4` is not a base case.

So:

```python
dp[4] = fun(3) + fun(2)
```

---

## Step 3: `fun(3)`

Again, not a base case.

So:

```python
dp[3] = fun(2) + fun(1)
```

Now:

```text
fun(2) = 2
fun(1) = 1
```

Therefore:

```text
fun(3) = 2 + 1
        = 3
```

Store it:

```text
dp = {
    3: 3
}
```

Return:

```text
3
```

---

## Step 4: Finish `fun(4)`

We already know:

```text
fun(3) = 3
fun(2) = 2
```

Therefore:

```text
fun(4) = 3 + 2
        = 5
```

Store:

```text
dp = {
    3: 3,
    4: 5
}
```

Return:

```text
5
```

---

## Step 5: Calculate `fun(3)` for `fun(5)`

Now `fun(3)` is already in `dp`.

So this line:

```python
if n in dp:
    return dp[n]
```

returns:

```text
dp[3] = 3
```

We **do not calculate `fun(3)` again**.

---

## Step 6: Finish `fun(5)`

We now have:

```text
fun(4) = 5
fun(3) = 3
```

Therefore:

```text
fun(5) = 5 + 3
        = 8
```

Store:

```text
dp = {
    3: 3,
    4: 5,
    5: 8
}
```

Finally:

```text
Answer = 8
```

---

# Recursion Flow

For `n = 5`, the important calculation is:

```text
                fun(5)
               /      \
          fun(4)      fun(3)
          /    \       ↑
     fun(3)   fun(2)   │
       ↑
       │
     stored
```

When `fun(3)` is calculated for the first time:

```text
fun(3) = 3
```

we store:

```text
dp[3] = 3
```

When we encounter `fun(3)` again, we simply retrieve:

```text
dp[3]
```

instead of recursively calculating it again.

---

# What Exactly Is Stored?

This is an important part of the solution.

The dictionary doesn't store every individual climbing path.

It stores the **answer for a particular number of steps**.

For example:

```text
dp[3] = 3
```

means:

> There are 3 ways to climb 3 steps.

Similarly:

```text
dp[4] = 5
```

means:

> There are 5 ways to climb 4 steps.

And:

```text
dp[5] = 8
```

means:

> There are 8 ways to climb 5 steps.

So `dp` is basically:

```text
number of steps → number of ways
```

---

# Why Does It Work?

Every valid way to reach step `n` must have one of two possible final moves:

```text
... → n-1 → n
```

or:

```text
... → n-2 → n
```

There is no other possibility because we can only take `1` or `2` steps.

Therefore, all ways to reach `n` can be divided into two groups:

```text
Ways reaching n-1 + 1-step move
```

and:

```text
Ways reaching n-2 + 2-step move
```

These groups do not overlap, so we can add them:

```text
ways(n) = ways(n-1) + ways(n-2)
```

The memoization dictionary ensures that each `ways(n)` is calculated only once.

---

# Fibonacci Connection

The results are:

```text
n = 1 → 1
n = 2 → 2
n = 3 → 3
n = 4 → 5
n = 5 → 8
n = 6 → 13
n = 7 → 21
```

Notice the pattern:

```text
1, 2, 3, 5, 8, 13, 21...
```

Each number is the sum of the previous two.

This is essentially the **Fibonacci sequence shifted by one position**.

---

# Algorithm

```text
1. Create an empty dictionary dp.

2. Define fun(n):
   
   a. If n == 1:
          return 1

   b. If n == 2:
          return 2

   c. If n is already in dp:
          return dp[n]

   d. Calculate:
          dp[n] = fun(n-1) + fun(n-2)

   e. Return dp[n]

3. Call fun(n).

4. Return the result.
```

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

Without memoization, recursion would repeatedly calculate the same values and could take exponential time.

With memoization, each value from `1` to `n` is calculated at most once.

Therefore:

```text
O(n)
```

---

### Space Complexity

```text
O(n)
```

The dictionary can store up to `n` results:

```text
dp[3]
dp[4]
dp[5]
...
dp[n]
```

Additionally, recursion uses a call stack of up to `O(n)` in the worst case.

So the overall auxiliary space is:

```text
O(n)
```

---

# Key Takeaways

- At every step, we can climb either `1` or `2` steps.
- To reach step `n`, we must come from either `n-1` or `n-2`.
- Therefore:

```text
ways(n) = ways(n-1) + ways(n-2)
```

- `fun(1) = 1`.
- `fun(2) = 2`.
- `dp` stores already calculated answers.
- `if n in dp` prevents repeated recursive calculations.
- This technique is called **memoization** or **Top-Down Dynamic Programming**.
- For `n = 5`, the answer is `8`.
- Time Complexity: **O(n)**.
- Space Complexity: **O(n)**.

---

## Author

**Ramit Sarker**
