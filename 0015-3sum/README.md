# LeetCode 15 - 3Sum

## Problem

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

---

## Examples

### Example 1

**Input**

```python
nums = [-1,0,1,2,-1,-4]
```

**Output**

```python
[[-1,-1,2],[-1,0,1]]
```

---

### Example 2

**Input**

```python
nums = [0,1,1]
```

**Output**

```python
[]
```

---

### Example 3

**Input**

```python
nums = [0,0,0]
```

**Output**

```python
[[0,0,0]]
```

---

# Approach

1. Sort the array.
2. Iterate through the array using index `i`.
3. Skip duplicate values of `i` to avoid duplicate triplets.
4. Use two pointers:
   - `j = i + 1`
   - `k = len(nums) - 1`
5. Calculate the sum of the three numbers.
6. If the sum is:
   - Greater than `0` → decrease `k`
   - Less than `0` → increase `j`
   - Equal to `0` → store the triplet, move both pointers, and skip duplicate values.
7. Return the list of unique triplets.

---

# Code

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]

                if target > 0:
                    k -= 1

                elif target < 0:
                    j += 1

                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res
```

---

# Explanation

### Step 1: Sort the array

Sorting helps us:

- Apply the two-pointer technique.
- Skip duplicate elements easily.

Example:

```python
[-1,0,1,2,-1,-4]
```

becomes

```python
[-4,-1,-1,0,1,2]
```

---

### Step 2: Choose the first number

```python
for i in range(len(nums)):
```

`i` selects the first element of the triplet.

Example:

```
i
↓

[-4,-1,-1,0,1,2]
```

---

### Step 3: Skip duplicate first elements

```python
if i > 0 and nums[i] == nums[i-1]:
    continue
```

If the current value is the same as the previous one, we skip it.

Example:

```
[-4,-1,-1,0,1,2]
      ↑
      duplicate
```

This prevents duplicate triplets.

---

### Step 4: Initialize two pointers

```python
j = i + 1
k = len(nums) - 1
```

```
i        j        k
↓        ↓        ↓

[-4,-1,-1,0,1,2]
```

---

### Step 5: Find the sum

```python
target = nums[i] + nums[j] + nums[k]
```

If

- sum > 0 → decrease `k`
- sum < 0 → increase `j`
- sum == 0 → valid triplet found

---

### Step 6: Save the triplet

```python
res.append([nums[i], nums[j], nums[k]])
```

Then move both pointers.

```python
j += 1
k -= 1
```

---

### Step 7: Skip duplicate second elements

```python
while j < k and nums[j] == nums[j - 1]:
    j += 1
```

This avoids storing the same triplet multiple times.

---

# Dry Run

Input

```python
[-1,0,1,2,-1,-4]
```

Sorted

```python
[-4,-1,-1,0,1,2]
```

### i = 0 (-4)

No valid triplet.

---

### i = 1 (-1)

```
j = 2
k = 5
```

```
-1 + (-1) + 2 = 0
```

Store

```
[-1,-1,2]
```

Move pointers.

```
j = 3
k = 4
```

```
-1 + 0 + 1 = 0
```

Store

```
[-1,0,1]
```

---

### i = 2

Duplicate `-1`

Skip.

---

Remaining iterations produce no new triplets.

Final answer

```python
[[-1,-1,2],[-1,0,1]]
```

---

# Time Complexity

- Sorting: **O(n log n)**
- Two-pointer search for every element: **O(n²)**

Overall:

**O(n²)**

---

# Space Complexity

Ignoring the output list:

**O(1)**

Including the output list:

**O(k)**

where `k` is the number of triplets returned.

---

# Concepts Used

- Sorting
- Two Pointers
- Arrays
- Duplicate Handling
- Greedy Pointer Movement

---

# Python Features Used

- `sort()`
- `range()`
- `continue`
- `while`
- List `append()`

---

# Key Takeaways

- Sorting enables the two-pointer technique.
- Use one loop to fix the first element.
- Use two pointers to find the remaining two numbers.
- Skip duplicate first elements.
- After finding a valid triplet, move both pointers and skip duplicates.
- This reduces the brute-force **O(n³)** solution to **O(n²)**.

---

# Author

**Ramit Sarker**
