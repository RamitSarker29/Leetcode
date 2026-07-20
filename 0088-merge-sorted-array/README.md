# LeetCode 88 - Merge Sorted Array

## Problem

You are given two sorted integer arrays `nums1` and `nums2`.

- `nums1` has a size of `m + n`.
- The first `m` elements are valid.
- The last `n` elements are empty spaces (represented by `0`).
- `nums2` has `n` valid elements.

Merge `nums2` into `nums1` in **non-decreasing order**.

**Note:** Modify `nums1` **in-place**. Do not return a new array.

---

## Examples

### Example 1

**Input**

```text
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
```

**Output**

```text
[1,2,2,3,5,6]
```

---

### Example 2

**Input**

```text
nums1 = [1]
m = 1
nums2 = []
n = 0
```

**Output**

```text
[1]
```

---

### Example 3

**Input**

```text
nums1 = [0]
m = 0
nums2 = [1]
n = 1
```

**Output**

```text
[1]
```

---

# Approach

Instead of merging from the beginning, merge **from the end**.

### Why?

The last `n` positions of `nums1` are empty, so we can safely place the largest remaining element there without overwriting useful data.

Use three pointers:

- `i` → Last valid element of `nums1`
- `j` → Last element of `nums2`
- `k` → Last position of `nums1`

At each step:

- Compare `nums1[i]` and `nums2[j]`.
- Place the larger element at `nums1[k]`.
- Move the corresponding pointer.
- Decrease `k`.

Continue until every element of `nums2` has been copied.

---

# Code

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
```

---

# Explanation

### Initialize pointers

```text
i = m - 1
```

Points to the last valid element of `nums1`.

```text
j = n - 1
```

Points to the last element of `nums2`.

```text
k = m + n - 1
```

Points to the last index of `nums1`.

---

### Compare elements

If `nums1[i]` is larger,

copy it to `nums1[k]`.

Otherwise,

copy `nums2[j]` to `nums1[k]`.

Move the pointer of the copied element and decrease `k`.

---

### Why `while j >= 0`?

The loop continues until every element of `nums2` has been copied.

If `nums1` still has elements left after `nums2` is exhausted, they are already in their correct positions.

Therefore, only `nums2` must be completely processed.

---

# Dry Run

### Input

```text
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

Initial pointers

```text
i = 2
j = 2
k = 5
```

### Step 1

Compare

```text
3 and 6
```

Place 6.

```text
[1,2,3,0,0,6]
```

---

### Step 2

Compare

```text
3 and 5
```

Place 5.

```text
[1,2,3,0,5,6]
```

---

### Step 3

Compare

```text
3 and 2
```

Place 3.

```text
[1,2,3,3,5,6]
```

---

### Step 4

Compare

```text
2 and 2
```

Place 2 from `nums2`.

```text
[1,2,2,3,5,6]
```

---

`nums2` is exhausted (`j = -1`).

The remaining elements of `nums1` are already in the correct place.

Final answer:

```text
[1,2,2,3,5,6]
```

---

# Time Complexity

- Each element is processed at most once.

**Time Complexity:** `O(m + n)`

---

# Space Complexity

No extra array is created.

Only three integer variables (`i`, `j`, `k`) are used.

**Space Complexity:** `O(1)`

---

# Concepts Used

- Two Pointers
- In-place Array Modification
- Reverse Traversal
- Array Merging
- Greedy Placement

---

# Python Features Used

- List Indexing
- `while` Loop
- Conditional Statements
- In-place List Modification

---

# Key Takeaways

- Merge from the **end** to avoid overwriting valid elements.
- Use three pointers (`i`, `j`, `k`) to keep track of the current positions.
- Continue until `nums2` is fully copied (`while j >= 0`).
- No additional array is required, making the solution **O(1)** in extra space.

---

## Author

**Ramit Sarker**
