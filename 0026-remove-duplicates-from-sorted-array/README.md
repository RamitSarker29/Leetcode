# LeetCode 26 - Remove Duplicates from Sorted Array

## Problem

Given a sorted integer array `nums`, remove the duplicates **in-place** such that each unique element appears only once.

The relative order of the elements must remain the same.

Return the number of unique elements (`k`). The first `k` elements of `nums` should contain all the unique elements in sorted order.

---

## Examples

### Example 1

**Input**

```text
nums = [1,1,2]
```

**Output**

```text
2
nums = [1,2,_]
```

---

### Example 2

**Input**

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

**Output**

```text
5
nums = [0,1,2,3,4,_,_,_,_,_]
```

---

## Approach

- Since the array is already sorted, duplicate elements always appear next to each other.
- Use two pointers:
  - `i` traverses the array.
  - `pos` keeps track of the position where the next unique element should be placed.
- Compare each element with its previous element.
- If they are different, it is a new unique element.
- Store it at index `pos` and increment `pos`.
- Finally, return `pos`, which represents the number of unique elements.

---

## Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            pos = 1
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]:
                    nums[pos] = nums[i]
                    pos += 1
            return pos
```

---

## Explanation

Initially, the first element is always unique, so `pos` starts at `1`.

The pointer `i` scans the array from left to right.

Whenever `nums[i]` is different from `nums[i - 1]`, a new unique element is found.

That element is copied to index `pos`, and `pos` is incremented.

After the traversal, the first `pos` elements of the array contain all unique elements in sorted order.

---

## Dry Run

**Input**

```text
nums = [1,1,2,2,3]
```

| i | nums[i] | nums[i-1] | Action | pos | Array |
|---|---------|-----------|--------|-----|-------|
|1|1|1|Duplicate, skip|1|[1,1,2,2,3]|
|2|2|1|Copy to index 1|2|[1,2,2,2,3]|
|3|2|2|Duplicate, skip|2|[1,2,2,2,3]|
|4|3|2|Copy to index 2|3|[1,2,3,2,3]|

Final Result:

```text
k = 3
nums = [1,2,3,2,3]
```

Only the first **3** elements are considered:

```text
[1,2,3]
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

No extra data structure is used. The array is modified in-place.

---

## Concepts Used

- Two Pointers
- In-Place Array Modification
- Array Traversal
- Sorted Arrays

---

## Author

**Ramit Sarker**
