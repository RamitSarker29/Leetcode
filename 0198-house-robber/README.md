# 198. House Robber

## Problem

You are a professional robber planning to rob houses along a street.

Each house contains a certain amount of money.

However, you **cannot rob two adjacent houses**, because doing so will trigger the security system and alert the police.

Given an integer array `nums`, where:

```text
nums[i] = money available in house i
```

return the **maximum amount of money** you can rob without robbing two adjacent houses.

---

# Example 1

```text
Input:
nums = [1,2,3,1]

Output:
4
```

The best choice is:

```text
House 1 → 1
House 3 → 3
```

Total:

```text
1 + 3 = 4
```

We cannot rob houses 1 and 2 together because they are adjacent.

---

# Example 2

```text
Input:
nums = [2,7,9,3,1]

Output:
12
```

The best choice is:

```text
House 1 → 2
House 3 → 9
House 5 → 1
```

Total:

```text
2 + 9 + 1 = 12
```

---

# Key Idea

At every house, we have **two choices**:

### Choice 1: Rob the current house

If we rob house `i`, we **cannot rob house `i-1`**.

So the money we get is:

```text
nums[i] + answer(i-2)
```

---

### Choice 2: Skip the current house

If we don't rob house `i`, we can use the best answer up to house `i-1`.

So:

```text
answer(i-1)
```

Therefore:

```text
answer(i) = max(
    nums[i] + answer(i-2),
    answer(i-1)
)
```

This is the main recurrence of the problem.

---

# Understanding the Recurrence

Suppose:

```text
nums = [2,7,9,3,1]
```

At house `3`:

```text
nums[2] = 9
```

We have two choices.

### Rob house 3

We get:

```text
9 + answer(house 1)
```

because house 2 cannot be robbed.

### Skip house 3

We keep:

```text
answer(house 2)
```

Therefore:

```text
answer(house 3)
=
max(
    9 + answer(house 1),
    answer(house 2)
)
```

---

# Recursive + Memoization Approach

We can define:

```text
fun(i)
```

as:

> The maximum amount of money that can be robbed from houses `0` through `i`.

For every index `i`:

```text
fun(i) = max(
    nums[i] + fun(i-2),
    fun(i-1)
)
```

We use a dictionary:

```python
dp = {}
```

to store already calculated results.

This prevents the same subproblem from being solved repeatedly.

---

# Base Cases

If there is only one house:

```text
nums = [5]
```

we can simply rob it:

```text
fun(0) = 5
```

For two houses:

```text
nums = [2,7]
```

we can rob only one of them.

So:

```text
fun(1) = max(2,7)
       = 7
```

---

# Code

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def fun(n):
            if n == 0:
                return nums[0]

            if n == 1:
                return max(nums[0], nums[1])

            if n in dp:
                return dp[n]

            dp[n] = max(
                nums[n] + fun(n - 2),
                fun(n - 1)
            )

            return dp[n]

        return fun(len(nums) - 1)
```

---

# How the Code Works

### Step 1: Create the memoization dictionary

```python
dp = {}
```

This stores the maximum amount calculated for each index.

For example:

```text
dp[2] = 11
```

means:

> The maximum money that can be robbed from houses `0` through `2` is `11`.

---

### Step 2: Define the recursive function

```python
def fun(n):
```

Here, `n` represents the index of the current house.

---

### Step 3: Handle one house

```python
if n == 0:
    return nums[0]
```

There is only one house, so the best option is to rob it.

---

### Step 4: Handle two houses

```python
if n == 1:
    return max(nums[0], nums[1])
```

Since the houses are adjacent, we can rob only one.

So we take whichever contains more money.

---

### Step 5: Check memoization

```python
if n in dp:
    return dp[n]
```

If the answer for this index was already calculated, return it immediately.

---

### Step 6: Calculate the best choice

```python
dp[n] = max(
    nums[n] + fun(n - 2),
    fun(n - 1)
)
```

There are two possibilities:

```text
Rob current house:
nums[n] + fun(n-2)
```

or:

```text
Skip current house:
fun(n-1)
```

We choose the larger one.

---

# Dry Run

Let's take:

```text
nums = [2,7,9,3,1]
```

We call:

```text
fun(4)
```

because the last index is `4`.

---

## Step 1: `fun(4)`

House `4` contains:

```text
1
```

Two possibilities:

```text
Rob house 4:
1 + fun(2)

Skip house 4:
fun(3)
```

Therefore:

```text
fun(4) = max(1 + fun(2), fun(3))
```

---

## Step 2: `fun(2)`

House `2` contains:

```text
9
```

So:

```text
fun(2) = max(9 + fun(0), fun(1))
```

---

## Step 3: `fun(0)`

Only the first house exists:

```text
fun(0) = 2
```

---

## Step 4: `fun(1)`

There are two houses:

```text
2, 7
```

We can rob only one.

Therefore:

```text
fun(1) = max(2,7)
       = 7
```

---

## Step 5: Finish `fun(2)`

Now:

```text
fun(0) = 2
fun(1) = 7
```

So:

```text
fun(2) = max(9 + 2, 7)
       = max(11, 7)
       = 11
```

Store:

```text
dp[2] = 11
```

---

## Step 6: Calculate `fun(3)`

House `3` contains:

```text
3
```

Two choices:

```text
Rob house 3:
3 + fun(1)
= 3 + 7
= 10
```

or:

```text
Skip house 3:
fun(2)
= 11
```

Therefore:

```text
fun(3) = max(10,11)
       = 11
```

Store:

```text
dp[3] = 11
```

---

## Step 7: Finish `fun(4)`

Now:

```text
fun(2) = 11
fun(3) = 11
```

Therefore:

```text
fun(4) = max(1 + 11, 11)
       = max(12, 11)
       = 12
```

So:

```text
Answer = 12
```

---

# Recursion Flow

For:

```text
nums = [2,7,9,3,1]
```

the recurrence looks like:

```text
                         fun(4)
                        /      \
                 fun(2)        fun(3)
                /     \        /     \
           fun(0)    fun(1)  fun(1)  fun(2)
```

Without memoization, `fun(1)` and `fun(2)` would be calculated multiple times.

With:

```python
if n in dp:
    return dp[n]
```

already calculated results are reused.

For example:

```text
dp[2] = 11
```

So when `fun(2)` is needed again, we simply return:

```text
11
```

instead of recalculating it.

---

# Why Does It Work?

For every house, there are only two possibilities:

```text
1. Rob it
2. Don't rob it
```

If we rob the current house, we must skip the previous house:

```text
nums[n] + fun(n-2)
```

If we skip the current house, the best result remains the answer for the previous house:

```text
fun(n-1)
```

Therefore:

```text
fun(n) = max(
    nums[n] + fun(n-2),
    fun(n-1)
)
```

Since every possible valid solution must fall into one of these two categories, taking the maximum gives the optimal answer.

Memoization ensures that every subproblem is solved only once.

---

# Important Example

Consider:

```text
nums = [1,2,3,1]
```

We can see:

```text
Rob 1 → 1
Rob 3 → 3
```

giving:

```text
1 + 3 = 4
```

Trying to rob house `2` and house `4` gives:

```text
2 + 1 = 3
```

So the maximum is:

```text
4
```

The algorithm automatically compares these possibilities through the recurrence.

---

# Dynamic Programming Pattern

This problem is a classic example of **Dynamic Programming**.

The state is:

```text
dp[i] = maximum money that can be robbed from houses 0 to i
```

The transition is:

```text
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
```

The two terms represent:

```text
dp[i-1]
    ↓
Skip current house
```

and:

```text
nums[i] + dp[i-2]
    ↓
Rob current house
```

---

# Algorithm

```text
1. Create an empty dictionary dp.

2. Define fun(n):
   
   a. If n == 0:
          return nums[0]

   b. If n == 1:
          return max(nums[0], nums[1])

   c. If n is already in dp:
          return dp[n]

   d. Consider robbing house n:
          nums[n] + fun(n-2)

   e. Consider skipping house n:
          fun(n-1)

   f. Store the larger result:
          dp[n] = max(nums[n] + fun(n-2),
                      fun(n-1))

   g. Return dp[n]

3. Call fun(len(nums)-1).

4. Return the result.
```

---

# Complexity Analysis

### Time Complexity

```text
O(n)
```

Each index is calculated at most once because of memoization.

Without memoization, the recursive solution would repeatedly solve the same subproblems and could take exponential time.

---

### Space Complexity

```text
O(n)
```

The dictionary can store results for up to `n` houses.

The recursive call stack can also grow up to `O(n)` in the worst case.

Therefore, the overall auxiliary space is:

```text
O(n)
```

---

# Key Takeaways

- Two adjacent houses cannot both be robbed.
- At every house, we have two choices: **rob or skip**.
- If we rob the current house, we must use the answer from `i-2`.
- If we skip it, we use the answer from `i-1`.
- The recurrence is:

```text
fun(i) = max(nums[i] + fun(i-2), fun(i-1))
```

- `dp` stores previously calculated answers.
- This technique is called **memoization / Top-Down Dynamic Programming**.
- Time Complexity: **O(n)**.
- Space Complexity: **O(n)**.

---

## Note About the Submitted Code

The code included with the question was:

```python
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

This is the recurrence for **Climbing Stairs**, not House Robber:

```text
ways(n) = ways(n-1) + ways(n-2)
```

House Robber instead requires:

```text
maximum(n) = max(
    nums[n] + maximum(n-2),
    maximum(n-1)
)
```

So the House Robber code above is the corrected version of the same **recursive + memoization DP style**.

---

## Author

**Ramit Sarker**
