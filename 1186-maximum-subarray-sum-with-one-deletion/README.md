# 1186. Maximum Subarray Sum with One Deletion

## Problem

Given an integer array `arr`, return the **maximum sum** of a **non-empty contiguous subarray** after deleting **at most one element**.

- You may choose **not** to delete any element.
- If you delete one element, the remaining subarray must still contain **at least one element**.

---

## Examples

### Example 1

**Input**

```text
arr = [1, -2, 0, 3]
```

**Output**

```text
4
```

**Explanation**

Choose the subarray:

```text
[1, -2, 0, 3]
```

Delete:

```text
-2
```

Remaining subarray:

```text
[1, 0, 3]
```

Sum:

```text
1 + 0 + 3 = 4
```

---

### Example 2

**Input**

```text
arr = [1, -2, -2, 3]
```

**Output**

```text
3
```

**Explanation**

The best choice is:

```text
[3]
```

Sum:

```text
3
```

---

### Example 3

**Input**

```text
arr = [-1, -1, -1, -1]
```

**Output**

```text
-1
```

**Explanation**

Deleting the only element of a subarray would leave an empty subarray, which is **not allowed**.

Therefore, the answer is:

```text
-1
```

---

# Approach

This problem is an extension of **Kadane's Algorithm**.

Instead of maintaining one state, we maintain **two**.

### State 1

`no_deleted`

Maximum subarray sum ending at the current index **without using any deletion**.

### State 2

`one_deleted`

Maximum subarray sum ending at the current index **after using one deletion**.

---

## Transition

### Update `no_deleted`

Exactly Kadane's Algorithm.

Either:

- Extend the previous subarray.
- Start a new subarray.

```python
no_deleted = max(prev_no_deleted + arr[i], arr[i])
```

---

### Update `one_deleted`

There are two possibilities.

**Option 1**

Delete the current element.

```text
Take previous no_deleted
```

**Option 2**

Deletion was already used earlier.

Extend the previous `one_deleted`.

```text
previous one_deleted + arr[i]
```

Therefore,

```python
one_deleted = max(prev_one_deleted + arr[i], prev_no_deleted)
```

---

# Why `prev_no_deleted` and `prev_one_deleted`?

Both states for the current index must be calculated using the values from the **previous index**.

If we update `no_deleted` first, its previous value is lost.

So we save them.

```python
prev_no_deleted = no_deleted
prev_one_deleted = one_deleted
```

This is the same idea used in the **Maximum Product Subarray** problem where previous values are preserved before updating.

---

# Code

```python
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_deleted = arr[0]
        one_deleted = 0
        ans = arr[0]

        for i in range(1, len(arr)):
            prev_one_deleted = one_deleted
            prev_no_deleted = no_deleted

            no_deleted = max(prev_no_deleted + arr[i], arr[i])
            one_deleted = max(prev_one_deleted + arr[i], prev_no_deleted)

            ans = max(ans, no_deleted, one_deleted)

        return ans
```

---

# Dry Run

### Example

```text
arr = [1, -2, 0, 3]
```

| Index | Value | no_deleted | one_deleted | ans |
|------:|------:|-----------:|------------:|----:|
| 0 | 1 | 1 | 0 | 1 |
| 1 | -2 | -1 | 1 | 1 |
| 2 | 0 | 0 | 1 | 1 |
| 3 | 3 | 3 | 4 | 4 |

Answer:

```text
4
```

---

### Example

```text
arr = [1, -2, -2, 3]
```

| Index | Value | no_deleted | one_deleted | ans |
|------:|------:|-----------:|------------:|----:|
| 0 | 1 | 1 | 0 | 1 |
| 1 | -2 | -1 | 1 | 1 |
| 2 | -2 | -2 | -1 | 1 |
| 3 | 3 | 3 | 2 | 3 |

Answer:

```text
3
```

---

# Time Complexity

```text
O(n)
```

The array is traversed only once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Kadane's Algorithm
- Dynamic Programming
- Arrays
- State Transition

---

# Python Features Used

### Multiple Variables

```python
no_deleted
one_deleted
```

### Temporary Variables

```python
prev_no_deleted
prev_one_deleted
```

### max()

```python
max(a, b)
```

---

# Key Takeaways

- This is an extension of Kadane's Algorithm.
- Maintain two states:
  - `no_deleted` → No deletion used yet.
  - `one_deleted` → One deletion already used.
- Preserve previous values before updating.
- Compute both states independently for every index.
- The final answer is the maximum among all valid states.

---

## Author

**Ramit Sarker**
