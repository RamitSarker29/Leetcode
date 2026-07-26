# Maximum Sum Subarray of Size K

## Problem

Given an array of integers `arr[]` and an integer `k`, find the **maximum sum** of any contiguous subarray of size `k`.

A subarray is a contiguous part of the array.

---

## Examples

### Example 1

**Input:**

```text
arr = [100, 200, 300, 400]
k = 2
```

**Output:**

```text
700
```

**Explanation:**

The subarrays of size 2 are:

```text
[100, 200] → 300
[200, 300] → 500
[300, 400] → 700
```

The maximum sum is **700**.

---

### Example 2

**Input:**

```text
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
```

**Output:**

```text
39
```

**Explanation:**

The subarray

```text
[4, 2, 10, 23]
```

has the maximum sum of **39**.

---

### Example 3

**Input:**

```text
arr = [100, 200, 300, 400]
k = 1
```

**Output:**

```text
400
```

---

## Approach

A brute-force solution calculates the sum of every subarray of size `k`, resulting in **O(n × k)** time complexity.

We can optimize this using the **Sliding Window** technique.

### Steps

1. Calculate the sum of the first window of size `k`.
2. Store it as both the current window sum and the maximum sum.
3. Slide the window one element at a time.
4. Remove the element leaving the window.
5. Add the new element entering the window.
6. Update the maximum sum if the current window sum is greater.
7. Continue until the window reaches the end of the array.

---

## Code

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        i = 0
        j = k - 1

        window_sum = sum(arr[0:k])
        max_sum = window_sum

        while j < len(arr) - 1:
            window_sum = window_sum - arr[i] + arr[j + 1]
            max_sum = max(window_sum, max_sum)

            i += 1
            j += 1

        return max_sum
```

---

## Explanation

Suppose

```text
arr = [100, 200, 300, 400]
k = 2
```

The first window is

```text
[100, 200]
```

Its sum is

```text
300
```

Now slide the window one position to the right.

Instead of calculating the sum again, we:

- Remove the outgoing element.
- Add the incoming element.

```python
window_sum = window_sum - arr[i] + arr[j + 1]
```

For the next window:

```text
[200, 300]
```

```text
window_sum = 300 - 100 + 300 = 500
```

Update the maximum:

```python
max_sum = max(max_sum, window_sum)
```

Repeat the same process until all windows have been checked.

---

## Dry Run

### Input

```text
arr = [100, 200, 300, 400]
k = 2
```

### Initial Window

```text
Window = [100, 200]

window_sum = 300
max_sum = 300
```

---

### Slide 1

Remove **100**

Add **300**

```text
window_sum = 300 - 100 + 300 = 500
max_sum = 500
```

Current Window

```text
[200, 300]
```

---

### Slide 2

Remove **200**

Add **400**

```text
window_sum = 500 - 200 + 400 = 700
max_sum = 700
```

Current Window

```text
[300, 400]
```

---

### Final Answer

```text
700
```

---

## Time Complexity

- Initial window sum: **O(k)**
- Sliding the window: **O(n − k)**

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

Only a few variables are used.

---

## Concepts Used

- Sliding Window
- Two Pointers
- Running Sum
- Array Traversal

---

## Python Features Used

- `sum()`
- `max()`
- List Slicing
- `while` loop

---

## Key Takeaways

- Sliding Window avoids recalculating the sum of every subarray.
- Keep a running sum of the current window.
- When the window moves:
  - Remove the outgoing element.
  - Add the incoming element.
- Update the maximum after each window shift.
- This improves the time complexity from **O(n × k)** to **O(n)**.

---

**Author:** Ramit Sarker
