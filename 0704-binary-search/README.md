# 792. Binary Search

## Problem

Given an array of integers `nums` that is sorted in **ascending order**, and an integer `target`, find the index of `target`.

If `target` exists in the array, return its index.

If it does not exist, return:

```text
-1
```

The solution must have a time complexity of:

```text
O(log n)
```

---

## Examples

### Example 1

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output**

```text
4
```

**Explanation**

`9` exists in `nums` at index `4`.

```text
Index:  0   1   2   3   4   5
        ↓   ↓   ↓   ↓   ↓   ↓
nums = [-1,  0,  3,  5,  9, 12]
                            ↑
                          target
```

---

### Example 2

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 2
```

**Output**

```text
-1
```

**Explanation**

`2` does not exist in the array, so we return `-1`.

---

# Approach

Since the array is already **sorted**, we can use **Binary Search**.

Instead of checking every element one by one, Binary Search repeatedly divides the search space into two halves.

We maintain two pointers:

```python
low
high
```

They represent the current search range.

Initially:

```python
low = 0
high = len(nums) - 1
```

Then we calculate the middle index:

```python
mid = (low + high) // 2
```

We compare `nums[mid]` with `target`.

---

# Three Possible Cases

### Case 1: `nums[mid] < target`

The middle value is smaller than the target.

Because the array is sorted, everything to the **left of `mid`** is also smaller.

So we can discard the left half:

```python
low = mid + 1
```

---

### Case 2: `nums[mid] > target`

The middle value is greater than the target.

Because the array is sorted, everything to the **right of `mid`** is also greater.

So we discard the right half:

```python
high = mid - 1
```

---

### Case 3: `nums[mid] == target`

We found the target.

Return:

```python
mid
```

---

# Algorithm

1. Set `low = 0`.
2. Set `high = len(nums) - 1`.
3. While `low <= high`:

   * Calculate `mid`.
   * If `nums[mid] < target`, move `low` to `mid + 1`.
   * If `nums[mid] > target`, move `high` to `mid - 1`.
   * If `nums[mid] == target`, return `mid`.
4. If the loop finishes, the target does not exist.
5. Return `-1`.

---

# Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1

            if nums[mid] > target:
                high = mid - 1

            if nums[mid] == target:
                return mid

        return -1
```

---

# Dry Run

Consider:

```text
nums = [-1,0,3,5,9,12]
target = 9
```

Initial:

```text
low = 0
high = 5
```

Array:

```text
Index:  0   1   2   3   4   5
        ↓   ↓   ↓   ↓   ↓   ↓
       -1   0   3   5   9  12
```

---

### Iteration 1

Calculate:

```text
mid = (0 + 5) // 2
mid = 2
```

So:

```text
nums[mid] = 3
```

Compare:

```text
3 < 9
```

The target must be on the right.

Therefore:

```text
low = mid + 1
low = 3
```

Search range:

```text
[5, 9, 12]
```

---

### Iteration 2

Now:

```text
low = 3
high = 5
```

Calculate:

```text
mid = (3 + 5) // 2
mid = 4
```

So:

```text
nums[4] = 9
```

Compare:

```text
9 == 9
```

Target found.

Return:

```text
4
```

---

# Dry Run: Target Not Found

Consider:

```text
nums = [-1,0,3,5,9,12]
target = 2
```

Initial:

```text
low = 0
high = 5
```

### Iteration 1

```text
mid = 2
nums[mid] = 3
```

Since:

```text
3 > 2
```

discard the right half:

```text
high = 1
```

---

### Iteration 2

Now:

```text
low = 0
high = 1
```

```text
mid = 0
nums[mid] = -1
```

Since:

```text
-1 < 2
```

move right:

```text
low = 1
```

---

### Iteration 3

Now:

```text
low = 1
high = 1
```

```text
mid = 1
nums[mid] = 0
```

Since:

```text
0 < 2
```

move right:

```text
low = 2
```

Now:

```text
low = 2
high = 1
```

The condition:

```python
high >= low
```

is false.

Therefore, the target does not exist.

Return:

```text
-1
```

---

# Why Does Binary Search Work?

The key requirement is that the array is **sorted**.

Suppose:

```text
[-1, 0, 3, 5, 9, 12]
```

If we check the middle value `3` and the target is `9`, we immediately know:

```text
[-1, 0, 3]
```

cannot contain `9`.

We can completely discard that half.

Similarly, if the middle value is greater than the target, we discard everything to its right.

Therefore, every iteration eliminates approximately half of the remaining elements.

---

# Search Space Reduction

For `n` elements:

```text
n
↓
n/2
↓
n/4
↓
n/8
↓
...
↓
1
```

This logarithmic reduction gives:

```text
O(log n)
```

time complexity.

---

# Understanding `low` and `high`

Think of them as the boundaries of the current search area:

```text
low                    high
 ↓                       ↓
[-1, 0, 3, 5, 9, 12]
```

After deciding the target must be on the right:

```text
          low           high
           ↓              ↓
[-1, 0, 3, 5, 9, 12]
```

After deciding it must be on the left:

```text
low       high
 ↓          ↓
[-1, 0, 3, 5, 9, 12]
```

Everything outside `[low, high]` has been eliminated from consideration.

---

# Why Use `mid = (low + high) // 2`?

The middle index divides the current search space into two approximately equal parts:

```python
mid = (low + high) // 2
```

For example:

```text
low = 0
high = 5

mid = (0 + 5) // 2
mid = 2
```

So index `2` becomes the middle of the search range.

---

# Complexity

Let:

```text
n = len(nums)
```

### Time Complexity

Each iteration eliminates roughly half of the remaining elements.

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

No additional data structure is required.

Therefore:

```text
O(1)
```

---

# Key Takeaways

* Binary Search works because the array is **sorted**.
* Maintain a search range using `low` and `high`.
* Calculate the middle using:

```python
mid = (low + high) // 2
```

* If `nums[mid] < target` → search the **right half**.
* If `nums[mid] > target` → search the **left half**.
* If `nums[mid] == target` → return `mid`.
* If the search range becomes empty → return `-1`.
* Each iteration removes half of the remaining search space.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
