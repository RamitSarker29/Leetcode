# LeetCode 16 - 3Sum Closest

## Problem

Given an integer array `nums` of length `n` and an integer `target`, find three integers at **distinct indices** such that their sum is **closest** to the target.

Return the sum of the three integers.

You may assume that each input has exactly one solution.

---

## Examples

### Example 1

**Input**

```python
nums = [-1,2,1,-4]
target = 1
```

**Output**

```python
2
```

**Explanation**

The closest sum to the target is:

```python
-1 + 2 + 1 = 2
```

Difference from target:

```python
|2 - 1| = 1
```

---

### Example 2

**Input**

```python
nums = [0,0,0]
target = 1
```

**Output**

```python
0
```

---

# Approach

1. Sort the array.
2. Iterate through each element using index `i`.
3. For every `i`, initialize:
   - `j = i + 1`
   - `k = len(nums) - 1`
4. Compute the current sum.
5. If the current sum is closer to the target than the previous best sum, update the answer.
6. If:
   - current sum > target → move `k` left.
   - current sum < target → move `j` right.
   - current sum == target → return immediately because an exact match cannot be improved.
7. Return the closest sum found.

---

# Code

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum > target:
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    return current_sum

        return closest_sum
```

---

# Explanation

### Step 1: Sort the array

Sorting allows us to efficiently apply the two-pointer technique.

Example:

```python
[-1,2,1,-4]
```

becomes

```python
[-4,-1,1,2]
```

---

### Step 2: Fix the first element

```python
for i in range(len(nums)-2):
```

Each iteration chooses one number as the first element of the triplet.

```
i
↓

[-4,-1,1,2]
```

---

### Step 3: Initialize two pointers

```python
j = i + 1
k = len(nums) - 1
```

```
i      j      k
↓      ↓      ↓

[-4,-1,1,2]
```

---

### Step 4: Calculate the current sum

```python
current_sum = nums[i] + nums[j] + nums[k]
```

Find how close it is to the target.

```python
abs(current_sum - target)
```

---

### Step 5: Update the closest sum

```python
if abs(current_sum-target) < abs(closest_sum-target):
    closest_sum = current_sum
```

Only replace the answer if the current sum is closer to the target.

---

### Step 6: Move the pointers

If the current sum is:

Greater than target

```python
k -= 1
```

Move the right pointer left to reduce the sum.

If the current sum is:

Less than target

```python
j += 1
```

Move the left pointer right to increase the sum.

If the current sum equals the target:

```python
return current_sum
```

This is the best possible answer because the difference is `0`.

---

# Dry Run

Input

```python
nums = [-1,2,1,-4]
target = 1
```

Sorted

```python
[-4,-1,1,2]
```

### First iteration

```
i = 0
j = 1
k = 3
```

```
current_sum = -4 + (-1) + 2 = -3
```

Closest sum becomes

```
-3
```

Since

```
-3 < 1
```

Move `j`.

---

```
j = 2
```

```
current_sum = -4 + 1 + 2 = -1
```

Closer than `-3`.

Update answer.

Move `j`.

---

### Second iteration

```
i = 1
j = 2
k = 3
```

```
current_sum = -1 + 1 + 2 = 2
```

Difference:

```
|2 - 1| = 1
```

This is closer than the previous answer.

Update:

```
closest_sum = 2
```

Pointers meet.

Algorithm finishes.

Final answer:

```python
2
```

---

# Time Complexity

- Sorting: **O(n log n)**
- Outer loop: **O(n)**
- Two-pointer search: **O(n)**

Overall:

**O(n²)**

---

# Space Complexity

Ignoring the sorting algorithm:

**O(1)**

---

# Concepts Used

- Sorting
- Two Pointers
- Greedy Pointer Movement
- Arrays

---

# Python Features Used

- `sort()`
- `range()`
- `abs()`
- `float('inf')`
- `while`

---

# Key Takeaways

- Sorting enables the two-pointer technique.
- Keep track of the closest sum instead of looking for an exact sum.
- Update the answer whenever a closer sum is found.
- Move the pointers based on whether the current sum is smaller or larger than the target.
- Return immediately if an exact match is found.

---

# Author

**Ramit Sarker**
