# 121 - Best Time to Buy and Sell Stock

## Problem

Given an array `prices` where `prices[i]` represents the stock price on the `iᵗʰ` day.

You are allowed to complete **only one transaction**:

- Buy one stock.
- Sell it on a **future** day.

Return the **maximum profit** you can achieve.

If no profit is possible, return `0`.

---

# Examples

## Example 1

```text
Input:
prices = [7,1,5,3,6,4]

Output:
5

Explanation:
Buy at price 1 (Day 2)
Sell at price 6 (Day 5)

Profit = 6 - 1 = 5
```

---

## Example 2

```text
Input:
prices = [7,6,4,3,1]

Output:
0

Explanation:
Prices keep decreasing, so no profitable transaction is possible.
```

---

# Approach

The main idea is to traverse the array **from left to right** while keeping track of the lowest price seen so far.

We use three variables:

```python
buy
profit
max_profit
```

### `buy`

Stores the **lowest stock price seen so far**.

### `profit`

Stores the profit possible if we sell at the current price.

### `max_profit`

Stores the maximum profit found so far.

---

# Key Idea

For every price, we ask:

> Is today's price lower than the best buying price we have seen?

If yes, update `buy`.

Otherwise, today's price can be considered as a selling price.

We calculate:

```text
profit = current price - lowest buying price
```

and update `max_profit`.

Because we traverse from **left to right**, the buying price always comes from the current day or an earlier day, so the stock is never sold before it is bought.

---

# Code

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]

        profit = 0
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                max_profit = max(max_profit, profit)

        return max_profit
```

---

# Explanation

## Step 1: Initialize `buy`

```python
buy = prices[0]
```

We initially assume that the first day's price is the cheapest price.

For:

```text
prices = [7,1,5,3,6,4]
```

we start with:

```text
buy = 7
```

---

## Step 2: Initialize Profit Variables

```python
profit = 0
max_profit = 0
```

Initially, we haven't made any transaction.

Therefore:

```text
profit = 0
max_profit = 0
```

---

## Step 3: Traverse the Array

```python
for i in range(len(prices)):
```

We examine every day's price exactly once.

---

## Step 4: Check for a Lower Buying Price

```python
if prices[i] < buy:
    buy = prices[i]
```

If today's price is lower than our current `buy`, today's price becomes the new best buying price.

For example:

```text
buy = 7
current price = 1
```

Since:

```text
1 < 7
```

we update:

```text
buy = 1
```

---

## Step 5: Calculate Profit

If today's price is not lower than `buy`, we can calculate the profit from selling today:

```python
profit = prices[i] - buy
```

For example:

```text
buy = 1
current price = 6
```

Then:

```text
profit = 6 - 1
       = 5
```

---

## Step 6: Update Maximum Profit

```python
max_profit = max(max_profit, profit)
```

We compare today's possible profit with the best profit found previously.

For example:

```text
max_profit = 4
profit = 5
```

Then:

```text
max_profit = 5
```

---

## Step 7: Return the Answer

After processing every price:

```python
return max_profit
```

This gives the maximum possible profit.

---

# Dry Run

Let's take:

```text
prices = [7,1,5,3,6,4]
```

Initially:

```text
buy = 7
profit = 0
max_profit = 0
```

### Iteration 1

Current price:

```text
7
```

Check:

```text
7 < 7
```

False.

Calculate:

```text
profit = 7 - 7
       = 0
```

Update:

```text
max_profit = max(0, 0)
           = 0
```

---

### Iteration 2

Current price:

```text
1
```

Check:

```text
1 < 7
```

True.

So:

```text
buy = 1
```

We don't calculate a selling profit here because `1` is now our new cheapest buying price.

---

### Iteration 3

Current price:

```text
5
```

Check:

```text
5 < 1
```

False.

Calculate:

```text
profit = 5 - 1
       = 4
```

Update:

```text
max_profit = max(0, 4)
           = 4
```

---

### Iteration 4

Current price:

```text
3
```

Check:

```text
3 < 1
```

False.

Calculate:

```text
profit = 3 - 1
       = 2
```

Update:

```text
max_profit = max(4, 2)
           = 4
```

---

### Iteration 5

Current price:

```text
6
```

Check:

```text
6 < 1
```

False.

Calculate:

```text
profit = 6 - 1
       = 5
```

Update:

```text
max_profit = max(4, 5)
           = 5
```

---

### Iteration 6

Current price:

```text
4
```

Check:

```text
4 < 1
```

False.

Calculate:

```text
profit = 4 - 1
       = 3
```

Update:

```text
max_profit = max(5, 3)
           = 5
```

Final result:

```text
Answer = 5
```

---

# Dry Run Table

| Current Price | `buy` | `profit` | `max_profit` |
|---:|---:|---:|---:|
| 7 | 7 | 0 | 0 |
| 1 | 1 | — | 0 |
| 5 | 1 | 4 | 4 |
| 3 | 1 | 2 | 4 |
| 6 | 1 | 5 | 5 |
| 4 | 1 | 3 | 5 |

Final:

```text
5
```

---

# Example 2 Dry Run

Consider:

```text
prices = [7,6,4,3,1]
```

Initially:

```text
buy = 7
max_profit = 0
```

The price keeps decreasing:

```text
7 → 6 → 4 → 3 → 1
```

Every time we find a smaller price, we update `buy`.

```text
7 → buy = 7
6 → buy = 6
4 → buy = 4
3 → buy = 3
1 → buy = 1
```

There is never a profitable selling opportunity.

Therefore:

```text
max_profit = 0
```

Final answer:

```text
0
```

---

# Why Does It Work?

The solution works because for every possible selling day, we only need the **lowest price that occurred before or on that day**.

Suppose:

```text
prices = [7,1,5,3,6,4]
```

When we reach price `6`, the lowest price seen so far is:

```text
1
```

Therefore, the best profit for selling at `6` is:

```text
6 - 1 = 5
```

There is no need to check every previous price individually.

The variable:

```python
buy
```

already stores the best possible buying price.

So every day we only perform:

```text
current price - lowest buying price
```

and compare that profit with the maximum found so far.

---

# Why Can't We Just Find the Minimum and Maximum?

It is important that the buying day comes **before** the selling day.

For example:

```text
prices = [5,4,3,2,1,6]
```

Here:

```text
minimum = 1
maximum = 6
```

This works because `1` occurs before `6`.

But consider:

```text
prices = [6,5,4,3,2,1]
```

The minimum is `1` and the maximum is `6`, but:

```text
6 → 1
```

would mean buying at `6` and selling at `1`, which is a loss.

Our left-to-right traversal automatically respects the order:

```text
BUY → SELL
```

---

# Brute Force vs This Approach

### Brute Force

We could try every possible pair:

```text
Buy Day 1 → Sell Day 2
Buy Day 1 → Sell Day 3
Buy Day 1 → Sell Day 4
...
```

This requires:

```text
O(n²)
```

time.

---

### Optimized Approach

Instead, we maintain:

```text
lowest buying price
```

and calculate the best selling profit in one traversal.

Therefore:

```text
O(n)
```

time.

---

# Algorithm

```text
1. Set buy = first price.

2. Set profit = 0.

3. Set max_profit = 0.

4. Traverse every price:

   If current price < buy:
       Update buy.

   Otherwise:
       Calculate:
           profit = current price - buy

       Update:
           max_profit = max(max_profit, profit)

5. Return max_profit.
```

---

# Complexity Analysis

## Time Complexity

```text
O(n)
```

The array is traversed exactly once.

If there are `n` prices, we perform approximately `n` iterations.

---

## Space Complexity

```text
O(1)
```

Only three variables are used:

```text
buy
profit
max_profit
```

No additional array, dictionary, or data structure is required.

---

# Concepts Used

- Arrays
- Greedy Algorithm
- One-Pass Traversal
- Running Minimum
- Maximum Tracking
- Optimization
- Buy Before Sell Constraint

---

# Python Features Used

### `for` Loop

```python
for i in range(len(prices)):
```

Used to traverse the array.

### `min`-style comparison

The code manually updates the minimum:

```python
if prices[i] < buy:
    buy = prices[i]
```

### `max()`

```python
max_profit = max(max_profit, profit)
```

Used to keep the largest profit found so far.

---

# Key Takeaways

- Keep track of the **lowest buying price** seen so far.
- For every later price, calculate the profit if we sell on that day.
- Keep updating `max_profit`.
- Traversing from left to right guarantees that the buying price comes before the selling price.
- We don't need to check every pair of days.
- The brute-force solution takes `O(n²)`.
- This approach solves the problem in **O(n)** time.
- Only constant extra space is required.

---

## Author

**Ramit Sarker**
