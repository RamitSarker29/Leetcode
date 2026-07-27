# LeetCode 1464 - Maximum Product of Two Elements in an Array

> **Note:** Although your prompt says **1574**, the problem shown is actually **LeetCode 1464 - Maximum Product of Two Elements in an Array**.

---

## Problem

Given an integer array `nums`, choose two **different** indices `i` and `j`.

Return the maximum value of:

```text
(nums[i] - 1) * (nums[j] - 1)
```

---

## Examples

### Example 1

**Input**

```text
nums = [3,4,5,2]
```

**Output**

```text
12
```

**Explanation**

Choose `4` and `5`.

```text
(4 - 1) × (5 - 1)

= 3 × 4

= 12
```

---

### Example 2

**Input**

```text
nums = [1,5,4,5]
```

**Output**

```text
16
```

**Explanation**

Choose the two `5`s.

```text
(5 - 1) × (5 - 1)

= 4 × 4

= 16
```

---

### Example 3

**Input**

```text
nums = [3,7]
```

**Output**

```text
12
```

---

## Approach

To maximize

```text
(nums[i] - 1) × (nums[j] - 1)
```

we simply need the **two largest numbers** in the array.

Instead of sorting the array (`O(n log n)`), we can find the largest and second largest elements in **one traversal**.

Maintain:

- `max1` → Largest number seen so far.
- `max2` → Second largest number seen so far.

For every element:

- If it is larger than `max1`,
  - Move the old `max1` to `max2`.
  - Update `max1`.
- Otherwise, if it is larger than `max2`,
  - Update `max2`.

Finally, compute:

```text
(max1 - 1) × (max2 - 1)
```

---

## Code

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')

        for i in nums:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i

        return (max1 - 1) * (max2 - 1)
```

---

## Explanation

### Step 1

Initialize two variables.

```python
max1 = float('-inf')
max2 = float('-inf')
```

Initially, no numbers have been processed.

---

### Step 2

Traverse the array once.

```python
for i in nums:
```

Process one number at a time.

---

### Step 3

If the current number is greater than the largest number seen so far,

```python
if i > max1:
```

then:

```python
max2 = max1
max1 = i
```

The previous largest number becomes the second largest.

---

### Step 4

Otherwise,

if the current number is larger than the second largest,

```python
elif i > max2:
```

update only

```python
max2 = i
```

---

### Step 5

After the loop,

`max1` and `max2` store the two largest numbers.

Return

```python
(max1 - 1) * (max2 - 1)
```

---

## Dry Run

### Input

```text
nums = [3,4,5,2]
```

Initial

```text
max1 = -∞
max2 = -∞
```

---

### Process 3

```text
max1 = 3
max2 = -∞
```

---

### Process 4

```text
4 > 3
```

Update

```text
max2 = 3
max1 = 4
```

---

### Process 5

```text
5 > 4
```

Update

```text
max2 = 4
max1 = 5
```

---

### Process 2

```text
2 < max2
```

No changes.

Final values:

```text
max1 = 5
max2 = 4
```

Answer

```text
(5 - 1) × (4 - 1)

= 4 × 3

= 12
```

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

Only two extra variables are used.

---

## Concepts Used

- Array Traversal
- Finding Largest and Second Largest Element
- Greedy Observation
- One-Pass Algorithm

---

## Python Features Used

### Negative Infinity

```python
float('-inf')
```

Used to initialize the largest values.

---

### For-each Loop

```python
for i in nums:
```

Iterates through each element.

---

### Conditional Statements

```python
if
elif
```

Used to update the two maximum values.

---

## Key Takeaways

- To maximize `(a - 1) × (b - 1)`, choose the two largest numbers.
- Sorting works but takes **O(n log n)** time.
- Tracking the largest and second largest values in one pass gives an **O(n)** solution.
- When a new maximum is found, the old maximum automatically becomes the second maximum.

---

**Author:** Ramit Sarker
