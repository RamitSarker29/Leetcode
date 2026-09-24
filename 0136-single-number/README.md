# 136. Single Number

## Problem

You are given a **non-empty** array of integers `nums`.

Every element appears **exactly twice**, except for one element that appears only once.

Find and return that single number.

The solution must have:

- **O(n)** runtime
- **O(1)** extra space

---

# Examples

## Example 1

```text
Input:  nums = [2, 2, 1]
Output: 1
```

`2` appears twice, while `1` appears only once.

---

## Example 2

```text
Input:  nums = [4, 1, 2, 1, 2]
Output: 4
```

The numbers `1` and `2` appear twice.

Only `4` appears once.

---

## Example 3

```text
Input:  nums = [1]
Output: 1
```

There is only one element, so it is automatically the single number.

---

# Approach

This solution uses the **XOR (`^`) bitwise operator**.

The key properties of XOR are:

```text
a ^ a = 0
a ^ 0 = a
```

And XOR is **commutative and associative**, meaning the order does not matter:

```text
a ^ b ^ a = (a ^ a) ^ b
          = 0 ^ b
          = b
```

Therefore, if every number appears twice except one:

```text
2 ^ 2 ^ 4 ^ 1 ^ 1
```

the pairs cancel each other:

```text
(2 ^ 2) ^ (1 ^ 1) ^ 4
```

becomes:

```text
0 ^ 0 ^ 4
```

which gives:

```text
4
```

So we can XOR every element together, and all duplicate pairs disappear automatically.

---

# Code

```python
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0

        for i in nums:
            ans ^= i

        return ans
```

---

# Code Explanation

## 1. Initialize `ans`

```python
ans = 0
```

We start with `0` because:

```text
0 ^ x = x
```

So the first number can be XORed with `0` without changing its value.

---

## 2. Traverse the Array

```python
for i in nums:
```

We visit every number exactly once.

---

## 3. XOR Each Number

```python
ans ^= i
```

This is shorthand for:

```python
ans = ans ^ i
```

Every duplicate number eventually XORs with itself and becomes `0`.

---

# Understanding XOR

XOR compares the corresponding bits of two numbers.

The basic XOR rules are:

| A | B | A ^ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The important rule for this problem is:

```text
1 ^ 1 = 0
```

and:

```text
0 ^ 0 = 0
```

Therefore:

```text
x ^ x = 0
```

---

# Why Does `x ^ x = 0`?

Consider:

```text
5 = 101
```

XOR `5` with itself:

```text
  101
^ 101
-----
  000
```

Therefore:

```text
5 ^ 5 = 0
```

This works for every integer.

---

# Why Does `0 ^ x = x`?

Consider:

```text
0 ^ 5
```

In binary:

```text
  000
^ 101
-----
  101
```

So:

```text
0 ^ 5 = 5
```

This is why starting with:

```python
ans = 0
```

works perfectly.

---

# Dry Run

Consider:

```python
nums = [4, 1, 2, 1, 2]
```

Start:

```text
ans = 0
```

### Step 1

```text
ans = 0 ^ 4
    = 4
```

### Step 2

```text
ans = 4 ^ 1
```

### Step 3

```text
ans = (4 ^ 1) ^ 2
```

### Step 4

Now we encounter another `1`:

```text
ans = 4 ^ 1 ^ 2 ^ 1
```

Because XOR is associative and commutative, we can rearrange:

```text
ans = 4 ^ (1 ^ 1) ^ 2
```

Since:

```text
1 ^ 1 = 0
```

we get:

```text
ans = 4 ^ 0 ^ 2
```

### Step 5

Finally, we encounter another `2`:

```text
ans = 4 ^ 2 ^ 2
```

Rearrange:

```text
ans = 4 ^ (2 ^ 2)
```

Therefore:

```text
ans = 4 ^ 0
```

And:

```text
ans = 4
```

Final answer:

```text
4
```

---

# Another Simple Example

Consider:

```text
nums = [2, 2, 1]
```

The XOR operation becomes:

```text
0 ^ 2 ^ 2 ^ 1
```

Group the duplicate pair:

```text
(2 ^ 2) ^ 1
```

Since:

```text
2 ^ 2 = 0
```

we get:

```text
0 ^ 1
```

Therefore:

```text
1
```

---

# Why Does It Work?

Every number except one appears exactly twice.

When the same number appears twice:

```text
x ^ x = 0
```

So every duplicate pair cancels itself out.

The single number has no matching pair, so it remains.

For example:

```text
[a, b, c, b, c]
```

XORing everything gives:

```text
a ^ b ^ c ^ b ^ c
```

Rearranging:

```text
a ^ (b ^ b) ^ (c ^ c)
```

Then:

```text
a ^ 0 ^ 0
```

Finally:

```text
a
```

Therefore, the final XOR result is exactly the number that appears once.

---

# Algorithm

1. Initialize `ans = 0`.
2. Traverse every element in `nums`.
3. XOR the current element with `ans`.
4. Duplicate values cancel each other because `x ^ x = 0`.
5. The only unpaired number remains in `ans`.
6. Return `ans`.

---

# Complexity Analysis

Let `n` be the number of elements in the array.

### Time Complexity

We traverse the array exactly once:

```text
O(n)
```

This satisfies the required linear runtime.

### Space Complexity

Only one extra variable is used:

```python
ans
```

Therefore:

```text
O(1)
```

This satisfies the constant extra space requirement.

---

# Why Not Use a Hash Map?

A common approach would be to count the frequency of every number using a dictionary.

For example:

```python
frequency = {}
```

But that would require:

```text
O(n)
```

extra space.

The XOR approach avoids storing frequencies completely.

```text
Hash Map → O(n) space
XOR      → O(1) space
```

---

# Concepts Used

- Bit manipulation
- XOR (`^`)
- Bitwise operators
- Associative property
- Commutative property
- Array traversal
- Constant-space algorithms

---

# Python Features Used

### XOR Assignment Operator

```python
ans ^= i
```

This is shorthand for:

```python
ans = ans ^ i
```

---

### For-each Loop

```python
for i in nums:
```

Directly visits every element of the array.

---

# Key Takeaways

- XOR is extremely useful when numbers appear in pairs.
- The most important property here is:

```text
x ^ x = 0
```

- Another important property is:

```text
0 ^ x = x
```

- Every duplicate pair cancels out.
- The number appearing only once remains.
- No sorting is required.
- No hash map or set is required.
- The solution achieves **O(n) time** and **O(1) extra space**.

---

# Author

**Ramit Sarker**
