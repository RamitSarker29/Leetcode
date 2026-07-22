# LeetCode 4312 - Limit Occurrences in Sorted Array

## Problem

Given a **sorted** integer array `nums` and an integer `k`, return an array such that each distinct element appears **at most `k` times**, while preserving the original order.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,1,1,2,2,3]
k = 2
```

**Output:**

```text
[1,1,2,2,3]
```

---

### Example 2

**Input:**

```text
nums = [1,2,3]
k = 1
```

**Output:**

```text
[1,2,3]
```

---

## Approach

Since the array is already **sorted**, all duplicate elements are adjacent.

We use a **write pointer (`i`)** to track where the next valid element should be placed.

### Logic

- The first `k` elements are always valid.
- After that, compare the current element with the element `k` positions behind the write pointer.
- If they are different, it means we have not yet kept `k` copies of the current element, so we keep it.
- Otherwise, skip it.

This allows us to modify the array **in-place** using only **O(1)** extra space.

---

## Code

```python
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        i = 0

        for n in nums:
            if i < k or n != nums[i - k]:
                nums[i] = n
                i += 1

        return nums[:i]
```

---

## Explanation

Suppose:

```text
nums = [1,1,1,2,2,3]
k = 2
```

### Initial State

```text
i = 0
```

---

### Read first `1`

```text
i < k

0 < 2 ✔
```

Keep it.

```text
[1]
```

---

### Read second `1`

```text
1 < 2 ✔
```

Keep it.

```text
[1,1]
```

---

### Read third `1`

Now

```text
i = 2
```

Check

```text
n != nums[i-k]

1 != nums[0]

1 != 1 ✖
```

Skip it.

---

### Read first `2`

```text
2 != nums[0]

2 != 1 ✔
```

Keep it.

```text
[1,1,2]
```

---

### Read second `2`

```text
2 != nums[1]

2 != 1 ✔
```

Keep it.

```text
[1,1,2,2]
```

---

### Read `3`

```text
3 != nums[2]

3 != 2 ✔
```

Keep it.

```text
[1,1,2,2,3]
```

---

## Dry Run

| Current Number | i | Condition | Action | Result |
|---------------|---|-----------|--------|--------|
|1|0|0 < 2|Keep|[1]|
|1|1|1 < 2|Keep|[1,1]|
|1|2|1 == nums[0]|Skip|[1,1]|
|2|2|2 != nums[0]|Keep|[1,1,2]|
|2|3|2 != nums[1]|Keep|[1,1,2,2]|
|3|4|3 != nums[2]|Keep|[1,1,2,2,3]|

---

## Time Complexity

- **O(n)**

Each element is visited exactly once.

---

## Space Complexity

- **O(1)**

The array is modified in-place.

---

## Concepts Used

- Two Pointers
- In-place Array Modification
- Sorted Array
- Write Pointer Technique

---

## Python Features Used

- `for n in nums`
- List Slicing (`nums[:i]`)
- In-place List Assignment

---

## Key Takeaways

- A **write pointer** can be used to modify an array without extra space.
- Since the array is **sorted**, duplicates are always consecutive.
- Comparing with `nums[i-k]` tells us whether we've already kept `k` copies of the current element.
- This technique is an extension of the approach used in **LeetCode 26 (Remove Duplicates from Sorted Array)**.

---

**Author:** Ramit Sarker
