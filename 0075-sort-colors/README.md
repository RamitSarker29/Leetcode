# LeetCode 75 - Sort Colors

## Problem

Given an array `nums` containing only `0`, `1`, and `2`, sort the array **in-place** without using the built-in sort function.

- `0` represents **Red**
- `1` represents **White**
- `2` represents **Blue**

The goal is to arrange them in the order:

```text
0 → 1 → 2
```

---

## Examples

### Example 1

**Input**

```text
nums = [2,0,2,1,1,0]
```

**Output**

```text
[0,0,1,1,2,2]
```

---

### Example 2

**Input**

```text
nums = [2,0,1]
```

**Output**

```text
[0,1,2]
```

---

## Approach

This problem is solved using the **Dutch National Flag Algorithm**.

We divide the array into four regions:

```text
| 0s | 1s | Unknown | 2s |
```

We use three pointers:

- **low** → Position where the next `0` should be placed.
- **mid** → Current element being inspected.
- **high** → Position where the next `2` should be placed.

### Rules

### If `nums[mid] == 0`

- Swap `nums[low]` and `nums[mid]`
- Move both `low` and `mid`

---

### If `nums[mid] == 1`

- `1` is already in the correct region.
- Move `mid` only.

---

### If `nums[mid] == 2`

- Swap `nums[mid]` and `nums[high]`
- Move `high` only.
- Do **not** move `mid` because the swapped element has not been processed yet.

---

## Code

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

            else:
                mid += 1

        return nums
```

---

## Explanation

Initially,

```text
low = 0
mid = 0
high = n - 1
```

The array is divided into four parts.

```text
| 0s | 1s | Unknown | 2s |
```

Initially,

```text
| | | Entire Array | |
```

Only the **Unknown** region needs to be processed.

---

### Case 1: Current element is `0`

Example

```text
[2,0,2,1,1,0]
    ↑
   mid
```

`0` belongs on the left.

Swap it with `low`.

Move

```text
low++
mid++
```

---

### Case 2: Current element is `1`

Example

```text
[0,1,2,1,2]
    ↑
   mid
```

`1` is already in the correct position.

Simply move

```text
mid++
```

---

### Case 3: Current element is `2`

Example

```text
[0,1,2,1,0]
      ↑   ↑
     mid high
```

Swap

```text
2 ↔ 0
```

Result

```text
[0,1,0,1,2]
```

Move

```text
high--
```

Notice that **mid does not move** because the element swapped from the end has not been checked yet.

---

## Dry Run

### Input

```text
nums = [2,0,2,1,1,0]
```

### Initial State

```text
low = 0
mid = 0
high = 5

[2,0,2,1,1,0]
```

---

### Step 1

Current

```text
2
```

Swap with `high`

```text
[0,0,2,1,1,2]
```

Move

```text
high--
```

---

### Step 2

Current

```text
0
```

Swap with `low`

```text
[0,0,2,1,1,2]
```

Move

```text
low++
mid++
```

---

### Step 3

Current

```text
0
```

Swap with `low`

```text
[0,0,2,1,1,2]
```

Move

```text
low++
mid++
```

---

### Step 4

Current

```text
2
```

Swap with `high`

```text
[0,0,1,1,2,2]
```

Move

```text
high--
```

---

### Step 5

Current

```text
1
```

Move

```text
mid++
```

---

### Step 6

Current

```text
1
```

Move

```text
mid++
```

Now

```text
mid > high
```

The array is completely sorted.

---

## Time Complexity

```text
O(n)
```

Each element is processed at most once.

---

## Space Complexity

```text
O(1)
```

The sorting is done in-place using only three pointers.

---

## Concepts Used

- Dutch National Flag Algorithm
- Three Pointers
- In-place Array Modification
- One-pass Traversal

---

## Python Features Used

- Multiple Assignment (Swapping)

```python
nums[a], nums[b] = nums[b], nums[a]
```

- `while` loop
- Conditional statements (`if`, `elif`, `else`)

---

## Key Takeaways

- The Dutch National Flag Algorithm sorts an array containing only three distinct values in **one traversal**.
- `low` points to the next position for `0`.
- `mid` scans the current element.
- `high` points to the next position for `2`.
- Move:
  - `low` and `mid` after processing `0`
  - `mid` after processing `1`
  - `high` only after processing `2`
- Do **not** move `mid` after swapping a `2` because the new element at `mid` has not been processed yet.

---

**Author:** Ramit Sarker
