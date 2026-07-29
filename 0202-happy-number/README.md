# 202. Happy Number

## Problem

Write an algorithm to determine whether a given positive integer `n` is a **happy number**.

A happy number is defined by the following process:

1. Replace the number with the **sum of the squares of its digits**.
2. Repeat this process.
3. If the number eventually becomes **1**, it is a happy number.
4. If the process enters a cycle that does **not** include `1`, it is not a happy number.

Return:

- `True` if `n` is a happy number.
- `False` otherwise.

---

## Examples

### Example 1

**Input**

```text
n = 19
```

**Output**

```text
True
```

**Explanation**

```text
19
↓
1² + 9² = 82
↓
8² + 2² = 68
↓
6² + 8² = 100
↓
1² + 0² + 0² = 1
```

Since the process reaches **1**, `19` is a happy number.

---

### Example 2

**Input**

```text
n = 2
```

**Output**

```text
False
```

**Explanation**

```text
2
↓
4
↓
16
↓
37
↓
58
↓
89
↓
145
↓
42
↓
20
↓
4 ...
```

The sequence repeats forever without reaching `1`, so `2` is not a happy number.

---

# Approach (Floyd's Cycle Detection Algorithm)

Instead of storing previously visited numbers in a hash set, we can detect a cycle using **Floyd's Cycle Detection Algorithm**.

## Phase 1

Create two pointers:

- **Slow Pointer** → Applies the transformation once.
- **Fast Pointer** → Applies the transformation twice.

```text
slow = f(n)
fast = f(f(n))
```

If the number is happy, the fast pointer eventually reaches **1**.

If the number is not happy, both pointers eventually meet inside a cycle.

---

# Code

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        def fun(n):
            sum = 0
            while n > 0:
                d = n % 10
                n = n // 10
                sum += d * d
            return sum

        while fast != 1:
            slow = fun(slow)
            fast = fun(fast)
            fast = fun(fast)

            if slow == fast and slow != 1:
                return False

        return True
```

---

# Explanation

Initialize both pointers.

```python
slow, fast = n, n
```

Create a helper function that returns the sum of the squares of the digits.

```python
def fun(n):
```

Extract each digit.

```python
d = n % 10
```

Remove the last digit.

```python
n = n // 10
```

Add the square of the digit.

```python
sum += d * d
```

Move the slow pointer one transformation.

```python
slow = fun(slow)
```

Move the fast pointer two transformations.

```python
fast = fun(fast)
fast = fun(fast)
```

If both pointers meet before reaching `1`, a cycle exists.

```python
if slow == fast and slow != 1:
    return False
```

If the fast pointer reaches `1`, the number is happy.

```python
return True
```

---

# Dry Run

### Example

```text
n = 19
```

Sequence:

```text
19 → 82 → 68 → 100 → 1
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 19 | 19 |
| 1 | 82 | 68 |
| 2 | 68 | 1 |

The fast pointer reaches **1**.

Return:

```text
True
```

---

### Example

```text
n = 2
```

Sequence:

```text
2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 ...
```

| Iteration | Slow | Fast |
|-----------|------|------|
| Start | 2 | 2 |
| 1 | 4 | 16 |
| 2 | 16 | 58 |
| 3 | 37 | 145 |
| 4 | 58 | 20 |
| 5 | 89 | 16 |
| 6 | 145 | 58 |
| 7 | 42 | 145 |
| 8 | 20 | 20 ✅ |

The pointers meet at **20**, indicating a cycle.

Return:

```text
False
```

---

# Time Complexity

```text
O(log n)
```

Each transformation processes all digits of the current number. The values quickly become small, so the algorithm runs efficiently.

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Floyd's Cycle Detection Algorithm
- Fast & Slow Pointer
- Two Pointers
- Number Manipulation
- Digit Extraction
- Cycle Detection

---

# Python Features Used

### Multiple Variable Assignment

```python
slow, fast = n, n
```

### Nested Function

```python
def fun(n):
```

### While Loop

```python
while n > 0:
```

### Integer Division

```python
n //= 10
```

### Modulo Operator

```python
d = n % 10
```

---

# Key Takeaways

- A happy number either reaches **1** or enters a cycle.
- Floyd's Cycle Detection Algorithm detects the cycle without using extra memory.
- The slow pointer moves one transformation at a time.
- The fast pointer moves two transformations at a time.
- If the fast pointer reaches **1**, the number is happy.
- If the two pointers meet before reaching **1**, the number is not happy.
- The solution uses **O(1)** extra space.

---

## Author

**Ramit Sarker**
