# 643. Maximum Average Subarray I

## Problem

Given an integer array `nums` and an integer `k`, find the contiguous subarray of **length exactly `k`** that has the maximum average value.

Return the maximum average.

---

## Examples

### Example 1

**Input**

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

**Output**

```text
12.75
```

**Explanation**

Possible subarrays of length `4`:

```text
[1,12,-5,-6]  → Sum = 2
[12,-5,-6,50] → Sum = 51
[-5,-6,50,3]  → Sum = 42
```

Maximum sum:

```text
51
```

Average:

```text
51 / 4 = 12.75
```

---

### Example 2

**Input**

```text
nums = [5]
k = 1
```

**Output**

```text
5.0
```

---

# Intuition

Since the subarray length is **fixed (`k`)**, recalculating the sum of every window would be inefficient.

Instead, use a **Sliding Window**.

- Compute the sum of the current window.
- When the window moves:
  - Remove the leftmost element.
  - Add the new rightmost element.

This updates the window sum in **O(1)** time.

---

# Approach

Maintain a window of exactly `k` elements.

For every new element:

1. Add it to the window.
2. If the window becomes larger than `k`:
   - Remove the leftmost element.
3. Once the window size becomes `k`:
   - Update the maximum window sum.

Finally,

```text
Maximum Average = Maximum Window Sum / k
```

---

# Algorithm

1. Initialize:

```python
left = 0
window_sum = 0
max_sum = -∞
```

2. Traverse the array using `right`.

3. Add the current element.

```python
window_sum += nums[right]
```

4. If window size exceeds `k`, remove the leftmost element.

```python
window_sum -= nums[left]
left += 1
```

5. When the window size becomes exactly `k`, update the maximum sum.

6. Return:

```python
max_sum / k
```

---

# Code

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window_sum = 0
        max_sum = float("-inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            if right - left + 1 > k:
                window_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)

        return max_sum / k
```

---

# Dry Run

### Example

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

| Window | Window Sum | Maximum Sum |
|---------|-----------:|------------:|
| `[1,12,-5,-6]` | 2 | 2 |
| `[12,-5,-6,50]` | 51 | 51 |
| `[-5,-6,50,3]` | 42 | 51 |

Final Answer:

```text
51 / 4 = 12.75
```

---

# Why Sliding Window?

Without Sliding Window:

For every subarray of size `k`, we'd calculate its sum again.

```text
Time Complexity = O(n × k)
```

With Sliding Window:

Each element is:

- Added once.
- Removed once.

So,

```text
Time Complexity = O(n)
```

---

# Time Complexity

```text
O(n)
```

Each element enters and leaves the window at most once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are used.

---

# Concepts Used

- Sliding Window
- Arrays

---

# Python Features Used

### Maximum Value

```python
max_sum = max(max_sum, window_sum)
```

---

### Window Size

```python
right - left + 1
```

---

### Sliding the Window

```python
window_sum += nums[right]
window_sum -= nums[left]
```

---

# Key Takeaways

- The window size is **fixed**.
- Instead of recalculating the sum, update it by:
  - Adding the new element.
  - Removing the old element.
- Track the **maximum window sum**.
- Divide by `k` only once at the end.
- Sliding Window reduces the complexity from **O(n × k)** to **O(n)**.

---

## Author

**Ramit Sarker**
