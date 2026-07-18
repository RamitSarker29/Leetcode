# LeetCode 121 - Best Time to Buy and Sell Stock

## Problem

Given an array `prices` where `prices[i]` represents the stock price on the `iᵗʰ` day.

You are allowed to complete **only one transaction**:
- Buy one stock.
- Sell it on a **future** day.

Return the maximum profit you can achieve. If no profit is possible, return `0`.

---

## Examples

### Example 1

```text
Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation:
Buy at price 1 (Day 2)
Sell at price 6 (Day 5)

Profit = 6 - 1 = 5
```

### Example 2

```text
Input: prices = [7,6,4,3,1]

Output: 0

Explanation:
Prices keep decreasing, so no profit can be made.
```

---

## Approach

Instead of checking every possible pair of buying and selling days (`O(n²)`), we keep track of the **lowest buying price** seen so far while traversing the array once.

For every day's price:

- Update the lowest buying price.
- Calculate the profit if we sell today.
- Update the maximum profit.

Since we move from left to right, the buying day is always before the selling day.

---

## Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = prices[0]

        for current_price in prices:
            lowest_buy = min(lowest_buy, current_price)
            profit = current_price - lowest_buy
            max_profit = max(max_profit, profit)

        return max_profit
```

---

## Explanation

### Step 1

Initialize two variables.

```python
max_profit = 0
lowest_buy = prices[0]
```

- `lowest_buy` stores the minimum stock price seen so far.
- `max_profit` stores the maximum profit found.

---

### Step 2

Traverse every stock price.

```python
for current_price in prices:
```

We process each day exactly once.

---

### Step 3

Update the minimum buying price.

```python
lowest_buy = min(lowest_buy, current_price)
```

If today's price is lower than all previous prices, it becomes our new buying price.

---

### Step 4

Calculate today's possible profit.

```python
profit = current_price - lowest_buy
```

This represents the profit if we buy at the cheapest price seen so far and sell today.

---

### Step 5

Update the maximum profit.

```python
max_profit = max(max_profit, profit)
```

If today's profit is larger than the previous maximum, update it.

---

### Step 6

Return the answer.

```python
return max_profit
```

---

## Dry Run

Input

```text
prices = [7,1,5,3,6,4]
```

| Current Price | Lowest Buy | Profit | Max Profit |
|---------------|------------|--------|------------|
| 7 | 7 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 5 | 1 | 4 | 4 |
| 3 | 1 | 2 | 4 |
| 6 | 1 | 5 | 5 |
| 4 | 1 | 3 | 5 |

Final Answer

```text
5
```

---

## Time Complexity

```text
O(n)
```

The array is traversed only once.

---

## Space Complexity

```text
O(1)
```

Only two extra variables are used.

---

## Concepts Used

- Arrays
- Greedy Algorithm
- One Pass Traversal
- Running Minimum
- Maximum Profit Tracking

---

## Python Features Used

- `for` loop
- `min()`
- `max()`

---

## Key Takeaways

- Always keep track of the **lowest buying price** seen so far.
- Calculate the profit for every selling day.
- Update the maximum profit whenever a better profit is found.
- Traversing from left to right automatically ensures **buy before sell**.
- This reduces the brute-force `O(n²)` solution to an optimal **`O(n)`** solution.

---

**Author:** **Ramit Sarker**
