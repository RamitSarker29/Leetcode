# 162. Find Peak Element

## Problem

A **peak element** is an element that is strictly greater than its neighbors.

Given a `0-indexed` integer array `nums`, find **any peak element** and return its index.

If there are multiple peaks, returning the index of **any one of them** is valid.

The solution must have a time complexity of:

```text
O(log n)
```

---

## Important Observation

We can imagine that:

```text
nums[-1] = -∞
nums[n] = -∞
```

This means the first and last elements can also be peaks.

For example:

```text
[1, 2, 3, 1]
```

`3` is greater than both of its neighbors:

```text
2 < 3 > 1
```

so index `2` is a peak.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,3,1]
```

**Output**

```text
2
```

**Explanation**

```text
1 < 2 < 3 > 1
        ↑
      peak
```

The element `3` at index `2` is a peak.

---

### Example 2

**Input**

```text
nums = [1,2,1,3,5,6,4]
```

**Output**

```text
5
```

**Explanation**

There are two peaks:

```text
1 < 2 > 1

and

3 < 5 < 6 > 4
```

So both index `1` and index `5` are valid answers.

The given solution returns:

```text
5
```

---

# Approach

Since we need an `O(log n)` solution, we use **Binary Search**.

The key idea is to compare:

```python
nums[mid]
```

with:

```python
nums[mid + 1]
```

There are two possibilities.

---

# Case 1: `nums[mid] > nums[mid + 1]`

This means we are moving **downhill**.

For example:

```text
        ↓
[1, 3, 7, 5, 2]
       mid
```

Here:

```text
nums[mid] > nums[mid + 1]
```

Since we are already going downward, there must be a peak at `mid` or somewhere to its **left**.

Therefore:

```python
high = mid
```

We keep `mid` because `mid` itself could be the peak.

---

# Case 2: `nums[mid] < nums[mid + 1]`

This means we are moving **uphill**.

For example:

```text
[1, 3, 5, 7, 4]
       ↑
      mid
```

Here:

```text
nums[mid] < nums[mid + 1]
```

The next element is larger, so `mid` cannot be a peak.

There must be a peak somewhere to the **right**.

Therefore:

```python
low = mid + 1
```

---

# The Core Idea

Remember this pattern:

```text
nums[mid] > nums[mid + 1]
        ↓
Going DOWN
        ↓
Peak is LEFT or MID
        ↓
high = mid
```

And:

```text
nums[mid] < nums[mid + 1]
        ↓
Going UP
        ↓
Peak is RIGHT
        ↓
low = mid + 1
```

This is the same important Binary Search pattern used in **Peak Index in a Mountain Array**.

The difference is that this problem does **not** require the entire array to be a mountain.

---

# Why Can We Always Find a Peak?

This is the key reasoning behind the solution.

Suppose:

```text
nums[mid] < nums[mid + 1]
```

We know the array is increasing at this point.

If we keep moving right while the values continue increasing, eventually one of two things happens:

### Situation 1: We reach a point where the array decreases

```text
1 < 3 < 5 < 8 > 4
            ↑
           peak
```

The point where the increasing sequence changes to decreasing is a peak.

### Situation 2: We reach the end

Because the element outside the array is considered `-∞`:

```text
1 < 3 < 5 < 8
            ↑
           peak
```

The last element is a peak.

Therefore, when we see:

```text
nums[mid] < nums[mid + 1]
```

it is always safe to search the right half.

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

4. Compare `nums[mid]` and `nums[mid + 1]`.

5. If:

```python
nums[mid] > nums[mid + 1]
```

move left:

```python
high = mid
```

6. Otherwise:

```python
low = mid + 1
```

7. When `low == high`, return that index.

---

# Code

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid

            if nums[mid] < nums[mid + 1]:
                low = mid + 1

        return high
```

---

# Dry Run

Consider:

```text
nums = [1,2,3,1]
```

Initial:

```text
low = 0
high = 3
```

---

### Iteration 1

Calculate:

```text
mid = (0 + 3) // 2
mid = 1
```

Values:

```text
nums[1] = 2
nums[2] = 3
```

Compare:

```text
2 < 3
```

We are going uphill.

Therefore:

```text
low = mid + 1
low = 2
```

Now:

```text
low = 2
high = 3
```

---

### Iteration 2

Calculate:

```text
mid = (2 + 3) // 2
mid = 2
```

Values:

```text
nums[2] = 3
nums[3] = 1
```

Compare:

```text
3 > 1
```

We are going downhill.

Therefore:

```text
high = mid
high = 2
```

Now:

```text
low = 2
high = 2
```

The loop stops.

Return:

```text
2
```

Therefore, index `2` is a peak.

---

# Dry Run With Multiple Peaks

Consider:

```text
nums = [1,2,1,3,5,6,4]
```

Initial:

```text
low = 0
high = 6
```

### Iteration 1

```text
mid = (0 + 6) // 2
mid = 3
```

Compare:

```text
nums[3] = 3
nums[4] = 5
```

Since:

```text
3 < 5
```

we are going uphill.

Move right:

```text
low = 4
```

---

### Iteration 2

Now:

```text
low = 4
high = 6
```

Calculate:

```text
mid = (4 + 6) // 2
mid = 5
```

Compare:

```text
nums[5] = 6
nums[6] = 4
```

Since:

```text
6 > 4
```

we are going downhill.

Move left while keeping `mid`:

```text
high = 5
```

Now:

```text
low = 5
high = 5
```

Return:

```text
5
```

And indeed:

```text
5 < 6 > 4
    ↑
   peak
```

---

# Why Do We Use `high = mid`?

This is an important detail.

When:

```python
nums[mid] > nums[mid + 1]
```

`mid` might itself be the peak.

For example:

```text
[1, 3, 7, 5, 2]
       ↑
      mid
```

Here:

```text
7 > 5
```

and `7` could be the peak.

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

```python
nums[mid] < nums[mid + 1]
```

`mid` definitely cannot be the peak because its right neighbor is larger.

For example:

```text
[1, 3, 5, 7, 4]
       ↑
      mid
```

Since:

```text
5 < 7
```

index `2` cannot be a peak.

Therefore, we can safely discard `mid`:

```python
low = mid + 1
```

---

# Why Does `low < high` Work?

We want the search to continue until only **one possible index** remains.

Eventually:

```text
low == high
```

For example:

```text
low = 5
high = 5
```

There is only one possible answer.

That index must be a peak.

Therefore, we return:

```python
return high
```

---

# Why Is `return high` Correct?

At the end:

```text
low == high
```

Therefore:

```python
return low
```

and:

```python
return high
```

would produce the same result.

The solution uses:

```python
return high
```

---

# Important Difference From Normal Binary Search

In normal Binary Search, we usually search for a specific value:

```text
target
```

Here, we are not searching for a known value.

Instead, we use the **direction of the array**:

```text
Increasing → Peak → Decreasing
```

The comparison:

```python
nums[mid] < nums[mid + 1]
```

tells us:

```text
We are going UP → Peak is RIGHT
```

while:

```python
nums[mid] > nums[mid + 1]
```

tells us:

```text
We are going DOWN → Peak is LEFT or MID
```

This is a very useful **Binary Search on a property** pattern.

---

# Complexity

Let:

```text
n = len(nums)
```

### Time Complexity

Each iteration removes approximately half of the search space.

Therefore:

```text
O(log n)
```

### Space Complexity

Only three variables are used:

```text
low
high
mid
```

Therefore:

```text
O(1)
```

---

# Key Takeaways

* Use **Binary Search** to achieve `O(log n)`.
* Compare `nums[mid]` with `nums[mid + 1]`.
* If:

```python
nums[mid] < nums[mid + 1]
```

we are going **uphill**, so the peak is on the **right**:

```python
low = mid + 1
```

* If:

```python
nums[mid] > nums[mid + 1]
```

we are going **downhill**, so the peak is on the **left or at `mid`**:

```python
high = mid
```

* Keep `mid` when moving left because it may itself be the peak.
* Discard `mid` when moving right because it cannot be the peak.
* Stop when `low == high`.
* Any peak is acceptable when multiple peaks exist.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
