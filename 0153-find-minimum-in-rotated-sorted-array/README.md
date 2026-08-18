# 153. Find Minimum in Rotated Sorted Array

## Problem

Given an array that was originally sorted in **ascending order** and then rotated, find the **minimum element**.

All elements in the array are **unique**.

The solution must run in:

```text
O(log n)
```

time complexity.

---

## What Is a Rotated Sorted Array?

Suppose the original sorted array is:

```text
[0,1,2,4,5,6,7]
```

After rotation, it could become:

```text
[4,5,6,7,0,1,2]
```

The important observation is that the rotated array consists of **two sorted portions**:

```text
[4,5,6,7] [0,1,2]
     ↑        ↑
   larger   smaller
```

The minimum is where the rotation occurs.

---

## Examples

### Example 1

**Input**

```text
nums = [3,4,5,1,2]
```

**Output**

```text
1
```

**Explanation**

The array was originally:

```text
[1,2,3,4,5]
```

After rotation:

```text
[3,4,5,1,2]
```

The smallest element is `1`.

---

### Example 2

**Input**

```text
nums = [4,5,6,7,0,1,2]
```

**Output**

```text
0
```

The array contains two sorted portions:

```text
[4,5,6,7] [0,1,2]
              ↑
           minimum
```

Therefore, the minimum is `0`.

---

### Example 3

**Input**

```text
nums = [11,13,15,17]
```

**Output**

```text
11
```

The array is effectively in its original sorted order, so the first element is the minimum.

---

# Approach

We use **Binary Search**.

The important comparison is:

```python
nums[mid] > nums[high]
```

We compare the middle element with the **last element**.

Why?

Because the last element helps us determine which sorted portion contains the minimum.

---

# Case 1: `nums[mid] > nums[high]`

Suppose:

```text
nums = [4,5,6,7,0,1,2]
```

and:

```text
mid = 3
```

Then:

```text
nums[mid] = 7
nums[high] = 2
```

So:

```text
7 > 2
```

This tells us that `mid` is in the **left sorted portion**.

The minimum must be somewhere **to the right of `mid`**.

Therefore:

```python
low = mid + 1
```

---

# Case 2: `nums[mid] <= nums[high]`

Suppose:

```text
nums = [4,5,6,7,0,1,2]
```

and:

```text
mid = 5
```

Then:

```text
nums[mid] = 1
nums[high] = 2
```

So:

```text
1 <= 2
```

This means `mid` is in the **right sorted portion**.

The minimum could be:

* at `mid`
* somewhere to the left of `mid`

Therefore, we **keep `mid`**:

```python
high = mid
```

We do **not** use:

```python
high = mid - 1
```

because `nums[mid]` itself could be the minimum.

---

# Core Idea

The pattern is:

```text
nums[mid] > nums[high]
        ↓
Minimum is RIGHT of mid
        ↓
low = mid + 1
```

and:

```text
nums[mid] <= nums[high]
        ↓
Minimum is LEFT of or AT mid
        ↓
high = mid
```

---

# Why Compare With `nums[high]`?

This is the key to understanding the problem.

Consider:

```text
[4,5,6,7,0,1,2]
```

If:

```text
nums[mid] > nums[high]
```

then the middle value is larger than the last value.

That means the rotation point must be **after `mid`**.

Example:

```text
[4,5,6,7 | 0,1,2]
         ↑
        mid
```

The minimum is on the right:

```text
[0,1,2]
 ↑
min
```

But if:

```text
nums[mid] <= nums[high]
```

then `mid` and `high` belong to the same sorted portion:

```text
[4,5,6,7 | 0,1,2]
              ↑ ↑
             mid high
```

The minimum is at `mid` or somewhere before it.

Therefore:

```python
high = mid
```

---

# Algorithm

1. Set:

```python
low = 0
high = len(nums) - 1
```

2. While:

```python
low < high
```

3. Calculate:

```python
mid = (low + high) // 2
```

4. Compare `nums[mid]` with `nums[high]`.

5. If:

```python
nums[mid] > nums[high]
```

move right:

```python
low = mid + 1
```

6. Otherwise:

```python
high = mid
```

7. When:

```text
low == high
```

the minimum element is at that index.

8. Return:

```python
nums[high]
```

---

# Code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1

            if nums[mid] <= nums[high]:
                high = mid

        return nums[high]
```

---

# Dry Run

Consider:

```text
nums = [3,4,5,1,2]
```

Initial:

```text
low = 0
high = 4
```

Array:

```text
Index:  0  1  2  3  4
Array: [3, 4, 5, 1, 2]
```

---

### Iteration 1

Calculate:

```text
mid = (0 + 4) // 2
mid = 2
```

Values:

```text
nums[mid] = 5
nums[high] = 2
```

Compare:

```text
5 > 2
```

Therefore, the minimum must be to the right of `mid`.

```text
low = mid + 1
low = 3
```

Search range:

```text
[1,2]
```

---

### Iteration 2

Now:

```text
low = 3
high = 4
```

Calculate:

```text
mid = (3 + 4) // 2
mid = 3
```

Values:

```text
nums[mid] = 1
nums[high] = 2
```

Compare:

```text
1 <= 2
```

Therefore, the minimum can be at `mid` or to its left.

```text
high = mid
high = 3
```

Now:

```text
low = 3
high = 3
```

The loop stops.

Return:

```text
nums[3] = 1
```

Final answer:

```text
1
```

---

# Dry Run: Array Not Rotated

Consider:

```text
nums = [11,13,15,17]
```

Initial:

```text
low = 0
high = 3
```

### Iteration 1

```text
mid = (0 + 3) // 2
mid = 1
```

Compare:

```text
nums[1] = 13
nums[3] = 17
```

Since:

```text
13 <= 17
```

we move left:

```text
high = 1
```

---

### Iteration 2

```text
low = 0
high = 1
mid = 0
```

Compare:

```text
nums[0] = 11
nums[1] = 13
```

Since:

```text
11 <= 13
```

we set:

```text
high = 0
```

Now:

```text
low = 0
high = 0
```

Return:

```text
nums[0] = 11
```

---

# Why Do We Use `high = mid`?

This is one of the most important details.

Suppose:

```text
nums = [4,5,6,7,0,1,2]
```

and:

```text
mid = 5
```

Then:

```text
nums[mid] = 1
nums[high] = 2
```

Since:

```text
1 <= 2
```

the minimum could actually be `nums[mid]`.

Therefore, we cannot discard `mid`.

We use:

```python
high = mid
```

instead of:

```python
high = mid - 1
```

---

# Why Do We Use `low = mid + 1`?

When:

```text
nums[mid] > nums[high]
```

we know `mid` cannot be the minimum.

For example:

```text
[4,5,6,7,0,1,2]
       ↑
      mid
```

Here:

```text
7 > 2
```

The minimum must occur after `mid`.

Therefore, we can safely discard `mid`:

```python
low = mid + 1
```

---

# Visual Understanding

A rotated sorted array looks like:

```text
          Rotation Point
                ↓
[4,5,6,7] [0,1,2]
 ↑             ↑
larger       minimum
```

The goal is to find the point where the sorted order "wraps around."

Binary Search determines which side contains that point.

---

# Another Example

Consider:

```text
nums = [4,5,6,7,0,1,2]
```

The search behaves like:

```text
[4,5,6,7,0,1,2]
       ↑
      mid
```

Since:

```text
7 > 2
```

move right:

```text
[0,1,2]
```

Now:

```text
[0,1,2]
 ↑
mid
```

Since:

```text
1 <= 2
```

keep the left side.

Eventually only:

```text
[0]
```

remains.

Therefore, `0` is the minimum.

---

# Why Does It Work?

At every step, we maintain the condition that the minimum element is still inside:

```text
[low, high]
```

When:

```python
nums[mid] > nums[high]
```

the minimum must be to the right, so we safely remove:

```text
[low ... mid]
```

When:

```python
nums[mid] <= nums[high]
```

the minimum is at `mid` or to its left, so we remove:

```text
[mid + 1 ... high]
```

Eventually:

```text
low == high
```

Only the minimum's index remains.

---

# Edge Cases

### Single Element

```text
nums = [5]
```

Initially:

```text
low = 0
high = 0
```

The loop doesn't execute.

Return:

```text
5
```

---

### Minimum at the Beginning

```text
nums = [1,2,3,4,5]
```

The algorithm eventually reduces the search to index `0`.

Answer:

```text
1
```

---

### Minimum at the End

```text
nums = [2,3,4,5,1]
```

The minimum is:

```text
1
```

at the last index.

The binary search correctly moves toward the right and finds it.

---

# Complexity

Let:

```text
n = len(nums)
```

### Time Complexity

Each iteration eliminates approximately half of the remaining search space.

Therefore:

```text
O(log n)
```

### Space Complexity

Only:

```text
low
high
mid
```

are used.

Therefore:

```text
O(1)
```

---

# Key Takeaways

* The array was originally **sorted**, then rotated.
* The rotated array consists of two sorted portions.
* The minimum is at the **rotation point**.
* Use Binary Search to find that point.
* Compare `nums[mid]` with `nums[high]`.
* If:

```python
nums[mid] > nums[high]
```

the minimum is to the **right**:

```python
low = mid + 1
```

* If:

```python
nums[mid] <= nums[high]
```

the minimum is at `mid` or to the **left**:

```python
high = mid
```

* Keep `mid` when moving `high` because `mid` could be the minimum.
* Stop when `low == high`.
* Return `nums[high]`.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
