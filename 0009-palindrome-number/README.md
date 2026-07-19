# LeetCode 9 - Palindrome Number

## Problem

Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A palindrome is a number that reads the same from left to right and right to left.

### Examples

#### Example 1

```text
Input: x = 121
Output: True
```

#### Example 2

```text
Input: x = -121
Output: False
```

#### Example 3

```text
Input: x = 10
Output: False
```

---

## Approach

The idea is to reverse the given integer without converting it into a string.

1. Negative numbers cannot be palindromes because of the negative sign.
2. Store the original number in another variable.
3. Reverse the digits of the number using modulo (`%`) and integer division (`//`).
4. Compare the reversed number with the original number.
5. If both are equal, return `True`; otherwise, return `False`.

---

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        num = x

        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10

        return rev == x
```

---

## Explanation

### Step 1: Handle Negative Numbers

```python
if x < 0:
    return False
```

Negative numbers are never palindromes.

Example:

```text
-121
```

Reversed:

```text
121-
```

They are not the same.

---

### Step 2: Initialize Variables

```python
rev = 0
num = x
```

- `rev` stores the reversed number.
- `num` is a copy of the original number because we'll modify it during reversal.

---

### Step 3: Reverse the Number

```python
while num != 0:
```

Continue until all digits are processed.

Inside the loop:

```python
rev = rev * 10 + num % 10
```

- `num % 10` extracts the last digit.
- `rev * 10` shifts previous digits to the left.
- Adding the last digit builds the reversed number.

Then remove the last digit:

```python
num = num // 10
```

---

### Step 4: Compare

```python
return rev == x
```

If the reversed number equals the original number, it is a palindrome.

---

## Dry Run

### Input

```text
x = 1221
```

| Iteration | num | Last Digit | rev |
|-----------|----:|-----------:|----:|
| Start | 1221 | - | 0 |
| 1 | 122 | 1 | 1 |
| 2 | 12 | 2 | 12 |
| 3 | 1 | 2 | 122 |
| 4 | 0 | 1 | 1221 |

Final Comparison:

```text
rev = 1221
x   = 1221
```

Return:

```text
True
```

---

### Another Example

Input:

```text
x = 123
```

| Iteration | num | Last Digit | rev |
|-----------|----:|-----------:|----:|
| Start | 123 | - | 0 |
| 1 | 12 | 3 | 3 |
| 2 | 1 | 2 | 32 |
| 3 | 0 | 1 | 321 |

Final Comparison:

```text
321 != 123
```

Return:

```text
False
```

---

## Time Complexity

- The loop runs once for every digit in the number.

**Time Complexity:** `O(log₁₀ n)`

---

## Space Complexity

Only a few integer variables are used.

**Space Complexity:** `O(1)`

---

## Concepts Used

- Integer reversal
- Modulo operator (`%`)
- Integer division (`//`)
- While loop
- Conditional statements

---

## Python Features Used

- Integer arithmetic
- Floor division (`//`)
- Modulo operator (`%`)
- Boolean comparison

---

## Key Takeaways

- No string conversion is required.
- `% 10` extracts the last digit.
- `// 10` removes the last digit.
- Multiplying the reversed number by `10` shifts its digits left before appending the next digit.
- Comparing the reversed number with the original determines whether the number is a palindrome.

---

## Author

**Ramit Sarker**
