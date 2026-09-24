# 3550. Smallest Index With Digit Sum Equal to Index

## Problem

You are given an integer array `nums`.

For every index `i`, calculate the **sum of the digits** of `nums[i]`.

Return the **smallest index** where:

```text
sum of digits of nums[i] == i
```

If no such index exists, return `-1`.

---

# Examples

## Example 1

```text
Input:  nums = [1, 3, 2]
Output: 2
```

Explanation:

```text
Index 0 → nums[0] = 1 → digit sum = 1 → 1 != 0

Index 1 → nums[1] = 3 → digit sum = 3 → 3 != 1

Index 2 → nums[2] = 2 → digit sum = 2 → 2 == 2
```

Therefore:

```text
Answer = 2
```

---

## Example 2

```text
Input:  nums = [1, 10, 11]
Output: 1
```

Check each index:

```text
Index 0 → 1  → digit sum = 1 → 1 != 0

Index 1 → 10 → digit sum = 1 + 0 = 1 → 1 == 1

Index 2 → 11 → digit sum = 1 + 1 = 2 → 2 == 2
```

Both indices `1` and `2` satisfy the condition.

Since we need the **smallest** index:

```text
Answer = 1
```

---

## Example 3

```text
Input:  nums = [1, 2, 3]
Output: -1
```

```text
Index 0 → 1 → digit sum = 1 → 1 != 0

Index 1 → 2 → digit sum = 2 → 2 != 1

Index 2 → 3 → digit sum = 3 → 3 != 2
```

No index satisfies the condition.

Therefore:

```text
Answer = -1
```

---

# Approach

The solution can be divided into two parts:

1. Find the digit sum of a number.
2. Check whether that digit sum is equal to its index.

A helper function `fun(n)` is used to calculate the digit sum.

Then we traverse the array from left to right.

Because we start from index `0` and move forward, the **first matching index is automatically the smallest index**.

---

# Code

```python
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def fun(n):
            ans = 0

            if n <= 9:
                return ans + n

            while n > 0:
                d = n % 10
                ans += d
                n = n // 10

            return ans

        for i in range(len(nums)):
            digit_sum = fun(nums[i])

            if digit_sum == i:
                return i

        return -1
```

---

# Code Explanation

## 1. Helper Function

```python
def fun(n):
```

The function `fun()` calculates the **sum of digits** of a number.

For example:

```text
123 → 1 + 2 + 3 = 6
```

---

## 2. Initialize the Sum

```python
ans = 0
```

`ans` stores the sum of the digits.

For example, while processing `123`:

```text
ans = 0
```

Then it becomes:

```text
1
3
6
```

---

## 3. Single-Digit Number

```python
if n <= 9:
    return ans + n
```

If `n` is a single digit, its digit sum is simply `n`.

For example:

```text
n = 7

digit sum = 7
```

So the function immediately returns `7`.

This also handles `n = 0`.

---

# 4. Extract the Last Digit

For numbers with multiple digits:

```python
while n > 0:
```

Inside the loop:

```python
d = n % 10
```

The modulo operator `%` gives the **last digit**.

For example:

```text
123 % 10 = 3
```

So:

```text
d = 3
```

---

# 5. Add the Digit

```python
ans += d
```

The extracted digit is added to the running sum.

For `123`:

```text
ans = 0

3 → ans = 3
2 → ans = 5
1 → ans = 6
```

---

# 6. Remove the Last Digit

```python
n = n // 10
```

Integer division by `10` removes the last digit.

For example:

```text
123 // 10 = 12
12  // 10 = 1
1   // 10 = 0
```

Once `n` becomes `0`, the loop stops.

---

# How the Digit Sum Function Works

For:

```text
n = 123
```

The process is:

```text
        n       n % 10       ans
       123         3          3
        12         2          5
         1         1          6
         0         -          6
```

Therefore:

```text
fun(123) = 6
```

---

# 7. Traverse the Array

After defining the helper function:

```python
for i in range(len(nums)):
```

we check every index from left to right.

For example:

```text
nums = [1, 10, 11]

i = 0
i = 1
i = 2
```

---

# 8. Calculate Digit Sum

```python
digit_sum = fun(nums[i])
```

For the current element, calculate its digit sum.

For example:

```text
i = 1
nums[1] = 10

digit_sum = fun(10)
         = 1
```

---

# 9. Compare Digit Sum With Index

```python
if digit_sum == i:
    return i
```

This is the main condition of the problem.

We check:

```text
digit sum == index
```

If it is true, we immediately return the index.

---

# Why Can We Return Immediately?

The problem asks for the **smallest index**.

We traverse the array like this:

```text
0 → 1 → 2 → 3 → 4 → ...
```

Therefore, if we find a valid index, every smaller index has already been checked.

So the first valid index must be the smallest one.

---

# Dry Run

Consider:

```python
nums = [1, 3, 2]
```

### Index 0

```text
nums[0] = 1
```

Digit sum:

```text
1
```

Compare:

```text
digit_sum = 1
index = 0

1 != 0
```

Continue.

---

### Index 1

```text
nums[1] = 3
```

Digit sum:

```text
3
```

Compare:

```text
3 != 1
```

Continue.

---

### Index 2

```text
nums[2] = 2
```

Digit sum:

```text
2
```

Compare:

```text
2 == 2
```

Condition satisfied.

So:

```python
return 2
```

Final answer:

```text
2
```

---

# Detailed Dry Run With Multiple Digits

Consider:

```python
nums = [5, 10, 23, 4]
```

### Index 0

```text
nums[0] = 5

digit sum = 5
index = 0

5 != 0
```

Continue.

### Index 1

```text
nums[1] = 10

10 % 10 = 0
ans = 0

10 // 10 = 1

1 % 10 = 1
ans = 1

1 // 10 = 0
```

Therefore:

```text
digit sum = 1
index = 1
```

So:

```text
1 == 1
```

Return:

```text
1
```

We don't need to check the remaining elements because index `1` is already the smallest valid index.

---

# Why Does It Work?

For every element `nums[i]`, the helper function correctly calculates its digit sum using:

```python
n % 10
```

to extract the last digit and:

```python
n // 10
```

to remove the last digit.

After calculating the digit sum, the algorithm checks:

```python
digit_sum == i
```

If the condition is true, that index satisfies the problem requirement.

Since the array is traversed from left to right, the first valid index encountered is necessarily the **smallest valid index**.

If the entire array is checked without finding a match, the algorithm returns:

```text
-1
```

which correctly represents that no valid index exists.

---

# Algorithm

1. Define a helper function `fun(n)` to calculate the digit sum.
2. If `n` is a single digit, return `n`.
3. Otherwise:
   - Extract the last digit using `n % 10`.
   - Add it to `ans`.
   - Remove the last digit using `n // 10`.
   - Repeat until `n` becomes `0`.
4. Traverse `nums` from index `0` to `len(nums) - 1`.
5. Calculate the digit sum of `nums[i]`.
6. If `digit_sum == i`, return `i`.
7. If no index satisfies the condition, return `-1`.

---

# Complexity Analysis

Let:

- `n` = number of elements in `nums`
- `d` = number of digits in a number

### Time Complexity

For every element, we calculate its digit sum.

Therefore:

```text
O(n × d)
```

Under the given constraints:

```text
nums[i] <= 1000
```

so each number has at most 4 digits.

Thus, `d` is very small and the solution is effectively:

```text
O(n)
```

---

### Space Complexity

The algorithm uses only a few variables:

```text
ans
d
i
digit_sum
```

Therefore, the auxiliary space is:

```text
O(1)
```

---

# Concepts Used

- Array traversal
- Digit extraction
- Modulo operator `%`
- Integer division `//`
- Helper functions
- String-independent digit manipulation
- Early return
- Comparison of computed values with indices

---

# Python Features Used

### Modulo Operator

```python
n % 10
```

Used to extract the last digit.

---

### Integer Division

```python
n // 10
```

Used to remove the last digit.

---

### Nested Function

```python
def fun(n):
```

The helper function is defined inside `smallestIndex()`.

---

### `range()`

```python
range(len(nums))
```

Used to iterate through all valid indices.

---

### Early Return

```python
return i
```

Once the smallest valid index is found, the function immediately stops.

---

# Key Takeaways

- The problem requires comparing an index with the digit sum of the value at that index.
- `% 10` extracts the last digit.
- `// 10` removes the last digit.
- Traversing from left to right guarantees that the first valid index is the smallest.
- The helper function makes the digit-sum calculation clean and reusable.
- If no index satisfies the condition, return `-1`.
- Because `nums[i] <= 1000`, the number of digits is very small, making the solution effectively linear in the array size.

---

# Author

**Ramit Sarker**
