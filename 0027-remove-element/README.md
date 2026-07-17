# LeetCode 27 - Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**.

Return the number of elements that are **not equal** to `val`.

The first `k` elements of `nums` should contain all the elements that are not equal to `val`. The remaining elements can be ignored.

---

## Examples

### Example 1

**Input**

```text
nums = [3,2,2,3]
val = 3
```

**Output**

```text
2
nums = [2,2,_,_]
```

---

### Example 2

**Input**

```text
nums = [0,1,2,2,3,0,4,2]
val = 2
```

**Output**

```text
5
nums = [0,1,4,0,3,_,_,_]
```

---

## Approach

- Use two pointers:
  - `i` traverses every element in the array.
  - `index` keeps track of where the next valid element should be placed.
- If the current element is **not equal** to `val`, copy it to `nums[index]`.
- Increment `index` after placing a valid element.
- Continue until the entire array is traversed.
- Return `index`, which represents the number of remaining elements.

---

## Code

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index
```

---

## Explanation

The pointer `i` reads every element in the array.

Whenever an element is **not equal** to `val`, it is copied to the position indicated by `index`.

After copying, `index` is incremented to point to the next available position.

By the end of the traversal:

- The first `index` elements contain all valid elements.
- The remaining elements are ignored.
- Returning `index` gives the number of elements remaining after removing `val`.

---

## Dry Run

**Input**

```text
nums = [3,2,2,3]
val = 3
```

| i | nums[i] | Action | index | Array |
|---|---------|--------|------:|-------|
|0|3|Skip|0|[3,2,2,3]|
|1|2|Copy to index 0|1|[2,2,2,3]|
|2|2|Copy to index 1|2|[2,2,2,3]|
|3|3|Skip|2|[2,2,2,3]|

Final Result:

```text
k = 2
nums = [2,2,2,3]
```

Only the first **2** elements are considered:

```text
[2,2]
```

The remaining elements can contain any values.

---

## Time Complexity

```text
O(n)
```

The array is traversed exactly once.

---

## Space Complexity

```text
O(1)
```

The array is modified in-place without using extra space.

---

## Concepts Used

- Two Pointers
- In-Place Array Modification
- Array Traversal

---

## Author

**Ramit Sarker**
