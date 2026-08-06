# 435. Non-overlapping Intervals

## Problem

You are given an array of intervals where:

```text
intervals[i] = [start, end]
```

Return the **minimum number of intervals** that must be removed so that the remaining intervals are **non-overlapping**.

> **Note:** Intervals that only touch at one point are **not** considered overlapping.

For example:

```text
[1,2] and [2,3]
```

are non-overlapping.

---

## Examples

### Example 1

**Input**

```text
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

**Output**

```text
1
```

**Explanation**

Removing:

```text
[1,3]
```

makes the remaining intervals non-overlapping.

---

### Example 2

**Input**

```text
intervals = [[1,2],[1,2],[1,2]]
```

**Output**

```text
2
```

**Explanation**

Only one interval can remain.

The other two must be removed.

---

### Example 3

**Input**

```text
intervals = [[1,2],[2,3]]
```

**Output**

```text
0
```

**Explanation**

The intervals only touch at one point, so they are already non-overlapping.

---

# Intuition

To minimize removals, we should keep the interval that is **more likely** to fit with future intervals.

When two intervals overlap,

keeping the interval with the **smaller ending value** leaves more room for future intervals.

This greedy choice minimizes future overlaps.

---

# Approach

### Step 1

Sort the intervals by their starting values.

```python
intervals.sort()
```

---

### Step 2

Store the ending value of the first interval.

```python
end1 = intervals[0][1]
```

This represents the interval currently being kept.

---

### Step 3

Traverse the remaining intervals.

```python
for start2, end2 in intervals[1:]:
```

---

### Step 4

Check whether the current interval overlaps.

Since touching intervals are allowed,

the overlap condition is:

```python
start2 < end1
```

---

### Step 5

If they overlap,

one interval must be removed.

```python
count += 1
```

Keep the interval that ends earlier.

```python
end1 = min(end1, end2)
```

This maximizes the space available for future intervals.

---

### Step 6

If they do not overlap,

keep the new interval.

```python
end1 = end2
```

---

### Step 7

Return the total number of removed intervals.

---

# Algorithm

1. Sort the intervals.
2. Keep the end of the first interval.
3. Traverse the remaining intervals.
4. If they overlap, increase the removal count.
5. Keep the interval with the smaller ending value.
6. Otherwise, update the current interval.
7. Return the removal count.

---

# Code

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        end1 = intervals[0][1]

        for start2, end2 in intervals[1:]:
            if start2 < end1:
                count += 1
                end1 = min(end1, end2)
            else:
                end1 = end2

        return count
```

---

# Dry Run

### Example

```text
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

After sorting:

```text
[[1,2],[1,3],[2,3],[3,4]]
```

Current interval:

```text
[1,2]
```

---

Compare:

```text
[1,2]

[1,3]
```

Since

```text
1 < 2
```

they overlap.

Remove one interval.

```text
count = 1
```

Keep the interval ending earlier.

```text
end = min(2,3) = 2
```

---

Compare:

```text
[2,3]
```

Since

```text
2 < 2
```

is false,

there is no overlap.

Update:

```text
end = 3
```

---

Compare:

```text
[3,4]
```

Since

```text
3 < 3
```

is false,

there is no overlap.

Update:

```text
end = 4
```

Final answer:

```text
1
```

---

# Why Does This Work?

Whenever two intervals overlap,

keeping the interval with the **smaller ending value** gives the best chance of fitting future intervals.

This greedy decision is always optimal because an interval that ends earlier can overlap with fewer future intervals.

Therefore, making the locally optimal choice at every overlap leads to the minimum number of removals.

---

# Time Complexity

Sorting:

```text
O(n log n)
```

Traversal:

```text
O(n)
```

Overall:

```text
O(n log n)
```

---

# Space Complexity

Ignoring the space used internally by sorting:

```text
O(1)
```

---

# Concepts Used

- Greedy
- Sorting
- Intervals
- Arrays

---

# Python Features Used

### Sort

```python
intervals.sort()
```

---

### Minimum

```python
end1 = min(end1, end2)
```

---

# Key Takeaways

- Sort intervals by their starting values.
- Touching intervals are **not** overlapping.
- The overlap condition is:

```python
start2 < end1
```

- When two intervals overlap, keep the one with the **smaller ending value**.
- This greedy choice minimizes future overlaps.
- The solution runs in **O(n log n)** time and is optimal.

---

## Author

**Ramit Sarker**
