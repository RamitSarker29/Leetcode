# LeetCode 977 - Squares of a Sorted Array

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, return an array of the **squares of each number**, also sorted in **non-decreasing order**.

**Note:** Squaring the elements may change their order because negative numbers become positive after squaring.

---

## Examples

### Example 1

**Input**

```text
nums = [-4,-1,0,3,10]
```

**Output**

```text
[0,1,9,16,100]
```

**Explanation**

After squaring:

```text
[16,1,0,9,100]
```

After sorting:

```text
[0,1,9,16,100]
```

---

### Example 2

**Input**

```text
nums = [-7,-3,2,3,11]
```

**Output**

```text
[4,9,9,49,121]
```

---

## Approach

The largest square always comes from one of the two ends of the array.

- The left end may contain a large negative number.
- The right end may contain a large positive number.

Instead of squaring everything and sorting, compare the **absolute values** of the leftmost and rightmost elements.

- If the left element has a larger absolute value, place its square at the end of the result array.
- Otherwise, place the square of the right element.
- Move the corresponding pointer.
- Continue until all elements are processed.

This avoids sorting and achieves **O(n)** time complexity.

---

## Code

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        l = 0
        r = n - 1
        k = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[k] = nums[l] * nums[l]
                l += 1
            else:
                res[k] = nums[r] * nums[r]
                r -= 1

            k -= 1

        return res
```

---

## Explanation

### Step 1

Create a result array of the same size.

```python
res = [0] * n
```

---

### Step 2

Initialize three pointers.

```text
l → First element

r → Last element

k → Last position of the result array
```

---

### Step 3

Compare

```text
abs(nums[l])
```

and

```text
abs(nums[r])
```

The larger absolute value produces the larger square.

Place that square at `res[k]`.

---

### Step 4

Move the pointer of the element that was used.

Decrease `k` after every insertion.

Continue until `l > r`.

---

## Dry Run

### Input

```text
nums = [-4,-1,0,3,10]
```

Initial state

```text
l = 0
r = 4
k = 4

res = [0,0,0,0,0]
```

### Step 1

Compare

```text
|-4| = 4
|10| = 10
```

10 is larger.

```text
res = [0,0,0,0,100]
```

```text
r = 3
k = 3
```

---

### Step 2

Compare

```text
|-4| = 4
|3| = 3
```

4 is larger.

```text
res = [0,0,0,16,100]
```

```text
l = 1
k = 2
```

---

### Step 3

Compare

```text
|-1| = 1
|3| = 3
```

3 is larger.

```text
res = [0,0,9,16,100]
```

```text
r = 2
k = 1
```

---

### Step 4

Compare

```text
|-1| = 1
|0| = 0
```

1 is larger.

```text
res = [0,1,9,16,100]
```

```text
l = 2
k = 0
```

---

### Step 5

Compare

```text
|0| = 0
|0| = 0
```

Place 0.

```text
res = [0,1,9,16,100]
```

Finished.

---

## Time Complexity

Each element is processed exactly once.

**Time Complexity:** `O(n)`

---

## Space Complexity

A result array of size `n` is created.

No additional data structures are used.

**Space Complexity:** `O(n)`

---

## Concepts Used

- Two Pointers
- Array Traversal
- Absolute Value
- In-place Pointer Movement
- Greedy Approach

---

## Python Features Used

- `abs()`
- List Initialization
- `while` Loop
- List Indexing

---

## Key Takeaways

- The largest square always comes from one of the two ends of the sorted array.
- Comparing absolute values eliminates the need to sort after squaring.
- Fill the result array from the end toward the beginning.
- Achieves the optimal **O(n)** time complexity.

---

## Author

**Ramit Sarker**
