# LeetCode 283 - Move Zeroes

## Problem

Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of the non-zero elements.

**Constraints:**

* Modify the array **in-place**.
* Do not create a copy of the array.

---

## Examples

### Example 1

**Input**

```text
nums = [0,1,0,3,12]
```

**Output**

```text
[1,3,12,0,0]
```

---

### Example 2

**Input**

```text
nums = [0]
```

**Output**

```text
[0]
```

---

## Approach

* Use two pointers:

  * `i` points to the position where the next non-zero element should be placed.
  * `j` traverses the array.
* Whenever a non-zero element is found at `j`, swap it with the element at `i`.
* Increment `i` after placing a non-zero element.
* By the end of the traversal, all non-zero elements are moved to the front while the zeros automatically shift to the end.

---

## Code

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
```

---

## Explanation

Initially, both pointers start at the beginning of the array.

* `j` scans every element.
* If `nums[j]` is non-zero, it is swapped with the element at index `i`.
* After the swap, `i` moves forward to the next available position.
* If `nums[j]` is zero, only `j` moves forward.
* This preserves the order of non-zero elements while moving all zeros to the end.

### Dry Run

**Input**

```text
[0,1,0,3,12]
```

| j | nums[j] |  i | Array        |
| - | ------: | -: | ------------ |
| 0 |       0 |  0 | [0,1,0,3,12] |
| 1 |       1 |  0 | [1,0,0,3,12] |
| 2 |       0 |  1 | [1,0,0,3,12] |
| 3 |       3 |  1 | [1,3,0,0,12] |
| 4 |      12 |  2 | [1,3,12,0,0] |

Final Answer:

```text
[1,3,12,0,0]
```

---

## Time Complexity

```text
O(n)
```

The array is traversed only once.

---

## Space Complexity

```text
O(1)
```

The array is modified in-place without using any extra space.

---

## Concepts Used

* Two Pointers
* In-Place Array Manipulation
* Swapping
* Array Traversal

---

## Author

**Ramit Sarker**
