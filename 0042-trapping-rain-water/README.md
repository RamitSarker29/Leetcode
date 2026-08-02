# 42. Trapping Rain Water

## Problem

Given an array `height` where each element represents the height of an elevation map, determine how much rainwater can be trapped after raining.

Each bar has a width of **1**.

---

## Examples

### Example 1

![Trapping Rain Water](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

**Input**

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

**Output**

```text
6
```

**Explanation**

The blue regions represent the trapped rainwater.

---

### Example 2

**Input**

```text
height = [4,2,0,3,2,5]
```

**Output**

```text
9
```

---

# Intuition

Water can only be trapped if there is a wall on **both sides**.

For every index:

```text
Water Level = min(Highest Wall on Left,
                  Highest Wall on Right)
```

The current bar already occupies some height.

Therefore,

```text
Water Trapped = Water Level - Current Height
```

For any index:

```text
water = min(leftMax, rightMax) - height[i]
```

---

# Key Observation

Instead of calculating the highest wall on both sides for every index (`O(n²)`), we can use **Two Pointers**.

Maintain:

- `left` pointer
- `right` pointer
- `leftMax`
- `rightMax`

`leftMax` stores the tallest bar seen so far from the left.

`rightMax` stores the tallest bar seen so far from the right.

---

# Why Move the Smaller Maximum?

Suppose:

```text
leftMax = 4
rightMax = 7
```

The water level is

```text
min(4,7) = 4
```

Even if the right wall becomes taller later,

```text
rightMax = 10
```

the water level is still

```text
min(4,10) = 4
```

Therefore, the amount of water on the **left side** is already determined.

So we process the left pointer.

Similarly,

If

```text
rightMax < leftMax
```

then the water on the **right side** is already determined.

So we process the right pointer.

---

# Algorithm

1. Initialize two pointers.

```python
left = 0
right = len(height) - 1
```

2. Store the tallest wall seen from both ends.

```python
leftMax = height[left]
rightMax = height[right]
```

3. While `left < right`:

- If `leftMax <= rightMax`
    - Move left.
    - Update `leftMax`.
    - Add trapped water.
- Otherwise
    - Move right.
    - Update `rightMax`.
    - Add trapped water.

4. Return the total trapped water.

---

# Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1

        left_max = height[0]
        right_max = height[-1]

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
```

---

# Dry Run

### Example

```text
height = [4,2,0,3,2,5]
```

| Left | Right | Left Max | Right Max | Water Added | Total |
|-----:|------:|---------:|----------:|------------:|------:|
| 0 | 5 | 4 | 5 | 0 | 0 |
| 1 | 5 | 4 | 5 | 2 | 2 |
| 2 | 5 | 4 | 5 | 4 | 6 |
| 3 | 5 | 6 | 5 | 0 | 6 |
| 3 | 4 | 6 | 5 | 3 | 9 |

Final Answer

```text
9
```

---

# Why Does This Work?

At every step,

- If `leftMax <= rightMax`, then the left wall limits the water level.

So,

```text
Water = leftMax - height[left]
```

No future right wall can change this.

Similarly,

If

```text
rightMax < leftMax
```

then

```text
Water = rightMax - height[right]
```

is already fixed.

This allows us to process one side in each iteration without scanning the array again.

---

# Time Complexity

```text
O(n)
```

Each pointer moves at most `n` times.

---

# Space Complexity

```text
O(1)
```

Only constant extra space is used.

---

# Concepts Used

- Two Pointers
- Arrays
- Greedy

---

# Python Features Used

### Maximum Height

```python
left_max = max(left_max, height[left])
right_max = max(right_max, height[right])
```

### Accumulating Water

```python
water += left_max - height[left]
```

or

```python
water += right_max - height[right]
```

### Two Pointer Traversal

```python
while left < right:
```

---

# Key Takeaways

- Water above an index depends on the **smaller** of the tallest walls on both sides.
- `leftMax` and `rightMax` store the tallest walls seen so far.
- Always process the side with the **smaller maximum**.
- Update the maximum **before** calculating trapped water.
- Each index is processed exactly once.
- Runs in **O(n)** time using **O(1)** extra space.

---

## Author

**Ramit Sarker**
