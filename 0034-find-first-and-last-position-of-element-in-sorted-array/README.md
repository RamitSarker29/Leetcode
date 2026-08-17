# 34. Find First and Last Position of Element in Sorted Array

## Problem

Given an array of integers `nums` sorted in **non-decreasing order**, find the **starting and ending position** of a given `target` value.

If `target` is not present in the array, return:

```text
[-1, -1]
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
nums = [5,7,7,8,8,10]
target = 8
```

**Output**

```text
[3,4]
```

**Explanation**

The target `8` appears at:

```text
Index:  0  1  2  3  4  5
Array: [5, 7, 7, 8, 8, 10]
                  ↑  ↑
                  3  4
```

Therefore:

* First occurrence → index `3`
* Last occurrence → index `4`

---

### Example 2

**Input**

```text
nums = [5,7,7,8,8,10]
target = 6
```

**Output**

```text
[-1,-1]
```

**Explanation**

`6` does not exist in the array.

Therefore, both positions remain `-1`.

---

### Example 3

**Input**

```text
nums = []
target = 0
```

**Output**

```text
[-1,-1]
```

The array is empty, so the target cannot be found.

---

# Approach

Since the array is sorted, we can use **Binary Search**.

We need to find two things:

1. The **first occurrence** of `target`.
2. The **last occurrence** of `target`.

Instead of using a linear search, we perform **two separate binary searches**.

Both searches take `O(log n)` time.

---

# Finding the First Occurrence

The first binary search tries to find the **leftmost position** where:

```python
nums[mid] == target
```

When we find the target, we don't immediately return.

Instead:

```python
res[0] = mid
high = mid - 1
```

We store the current index as a possible answer and continue searching to the **left**.

There might be another occurrence of the target earlier in the array.

---

## Example

```text
nums = [5,7,7,8,8,10]
target = 8
```

When we find the first `8`:

```text
[5,7,7,8,8,10]
       ↑
       mid
```

we store:

```text
res[0] = mid
```

and move:

```text
high = mid - 1
```

This forces Binary Search to look for an earlier `8`.

Eventually:

```text
res[0] = 3
```

---

# Finding the Last Occurrence

The second binary search works similarly, but this time we search for the **rightmost occurrence**.

When we find:

```python
nums[mid] == target
```

we store:

```python
res[1] = mid
```

Then search to the **right**:

```python
low = mid + 1
```

There might be another occurrence of the target later in the array.

---

## Example

```text
nums = [5,7,7,8,8,10]
target = 8
```

After finding an `8`:

```text
[5,7,7,8,8,10]
          ↑
          mid
```

we store its index and move:

```python
low = mid + 1
```

Eventually, we find the last `8` at index `4`.

Therefore:

```text
res[1] = 4
```

---

# Algorithm

### First Binary Search

1. Initialize `res = [-1, -1]`.
2. Set `low = 0` and `high = len(nums) - 1`.
3. Perform Binary Search.
4. If `nums[mid] > target`, search left.
5. If `nums[mid] < target`, search right.
6. If `nums[mid] == target`:

   * Store `mid` as the first position.
   * Continue searching left.

### Second Binary Search

1. Reset `low` and `high`.

2. Perform Binary Search again.

3. If `nums[mid] > target`, search left.

4. If `nums[mid] < target`, search right.

5. If `nums[mid] == target`:

   * Store `mid` as the last position.
   * Continue searching right.

6. Return `res`.

---

# Code

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        # Find first occurrence
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1

            if nums[mid] < target:
                low = mid + 1

            if nums[mid] == target:
                res[0] = mid
                high = mid - 1

        # Find last occurrence
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1

            if nums[mid] < target:
                low = mid + 1

            if nums[mid] == target:
                res[1] = mid
                low = mid + 1

        return res
```

---

# Dry Run

Consider:

```text
nums = [5,7,7,8,8,10]
target = 8
```

## First Binary Search

Initial:

```text
low = 0
high = 5
res = [-1,-1]
```

### Iteration 1

```text
mid = (0 + 5) // 2
mid = 2
```

```text
nums[2] = 7
```

Since:

```text
7 < 8
```

move right:

```text
low = 3
```

---

### Iteration 2

```text
mid = (3 + 5) // 2
mid = 4
```

```text
nums[4] = 8
```

Target found.

Store:

```text
res[0] = 4
```

But we want the **first** occurrence, so search left:

```text
high = 3
```

---

### Iteration 3

```text
mid = (3 + 3) // 2
mid = 3
```

```text
nums[3] = 8
```

Target found again.

Update:

```text
res[0] = 3
```

Search further left:

```text
high = 2
```

Now:

```text
low = 3
high = 2
```

The loop ends.

Therefore:

```text
first occurrence = 3
```

---

# Second Binary Search

Reset:

```text
low = 0
high = 5
```

### Iteration 1

```text
mid = 2
nums[2] = 7
```

Since:

```text
7 < 8
```

move right:

```text
low = 3
```

---

### Iteration 2

```text
mid = 4
nums[4] = 8
```

Target found.

Store:

```text
res[1] = 4
```

But we want the **last** occurrence, so search right:

```text
low = 5
```

---

### Iteration 3

```text
mid = 5
nums[5] = 10
```

Since:

```text
10 > 8
```

move left:

```text
high = 4
```

Now:

```text
low = 5
high = 4
```

The loop ends.

Therefore:

```text
last occurrence = 4
```

Final result:

```text
[3,4]
```

---

# Why Does It Work?

The key difference between the two searches is what happens when we find the target.

### First Occurrence

When:

```python
nums[mid] == target
```

we move left:

```python
high = mid - 1
```

This searches for an earlier occurrence.

```text
        target
          ↓
[... 8 ... 8 ...]
    ← search
```

---

### Last Occurrence

When:

```python
nums[mid] == target
```

we move right:

```python
low = mid + 1
```

This searches for a later occurrence.

```text
        target
          ↓
[... 8 ... 8 ...]
              → search
```

This is the core idea of the problem.

---

# What Happens If the Target Does Not Exist?

Consider:

```text
nums = [5,7,7,8,8,10]
target = 6
```

During both searches, we never encounter:

```python
nums[mid] == target
```

Therefore:

```text
res = [-1,-1]
```

The initial value of `res` handles this case automatically.

---

# Important Binary Search Pattern

This problem is an important extension of normal Binary Search.

Normal Binary Search:

```python
if nums[mid] == target:
    return mid
```

But here, finding the target is **not enough**.

For the first occurrence:

```python
if nums[mid] == target:
    res[0] = mid
    high = mid - 1
```

For the last occurrence:

```python
if nums[mid] == target:
    res[1] = mid
    low = mid + 1
```

So remember:

```text
First occurrence → move LEFT
Last occurrence  → move RIGHT
```

---

# Complexity

Let:

```text
n = len(nums)
```

We perform two Binary Searches.

### First Search

```text
O(log n)
```

### Second Search

```text
O(log n)
```

Therefore:

```text
O(log n) + O(log n) = O(log n)
```

### Space Complexity

Only a constant number of variables are used:

```text
low
high
mid
res
```

Therefore:

```text
O(1)
```

---

# Key Takeaways

* The array is sorted, so use **Binary Search**.
* We need **two searches**:

  * One for the first occurrence.
  * One for the last occurrence.
* When the target is found:

  * **First occurrence:** move `high` left.
  * **Last occurrence:** move `low` right.
* Don't immediately return when the target is found.
* Store the current index and continue searching.
* If the target doesn't exist, `res` remains `[-1, -1]`.
* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Author

**Ramit Sarker**
