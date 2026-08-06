# Overlapping Intervals

## Problem

You are given a list of intervals where each interval is represented as:

```text
[start, end]
```

Determine whether **any two intervals overlap**.

Two intervals overlap if they share **at least one common value**.

```text
[a, b] and [c, d] overlap if

a <= d
and
c <= b
```

Return:

- `True` if any overlap exists.
- `False` otherwise.

---

## Examples

### Example 1

**Input**

```text
[[1,3],[5,7],[2,4],[6,8]]
```

**Output**

```text
True
```

**Explanation**

After sorting:

```text
[[1,3],[2,4],[5,7],[6,8]]
```

The intervals

```text
[1,3]

[2,4]
```

overlap.

---

### Example 2

**Input**

```text
[[1,3],[7,9],[4,6],[10,13]]
```

**Output**

```text
False
```

**Explanation**

After sorting:

```text
[[1,3],[4,6],[7,9],[10,13]]
```

No consecutive intervals overlap.

---

# Intuition

After sorting by starting point,

any interval can only overlap with the interval immediately after it.

Therefore, we only need to compare consecutive intervals.

If any overlap is found, return `True`.

Otherwise, return `False`.

---

# Approach

### Step 1

Sort the intervals according to their starting values.

```python
intervals.sort()
```

---

### Step 2

Store the first interval.

```python
start1 = intervals[0][0]
end1 = intervals[0][1]
```

---

### Step 3

Traverse the remaining intervals.

```python
for start2, end2 in intervals[1:]:
```

---

### Step 4

Check whether the current interval overlaps.

```python
if start2 <= end1:
```

If true,

return:

```python
True
```

---

### Step 5

Otherwise,

update the current interval.

```python
start1 = start2
end1 = end2
```

---

### Step 6

If the loop finishes,

no overlap exists.

Return:

```python
False
```

---

# Algorithm

1. Sort all intervals.
2. Store the first interval.
3. Compare every interval with the current interval.
4. If an overlap exists, return `True`.
5. Otherwise, update the current interval.
6. If no overlap is found, return `False`.

---

# Code

```python
class Solution:
    def isIntersect(self, intervals):
        intervals.sort()

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for start2, end2 in intervals[1:]:
            if start2 <= end1:
                return True

            start1 = start2
            end1 = end2

        return False
```

---

# Dry Run

### Example

```text
intervals = [[1,3],[5,7],[2,4],[6,8]]
```

After sorting:

```text
[[1,3],[2,4],[5,7],[6,8]]
```

Current interval:

```text
[1,3]
```

Next interval:

```text
[2,4]
```

Check:

```text
2 <= 3
```

True.

Return:

```text
True
```

---

### Example

```text
intervals = [[1,3],[4,6],[7,9]]
```

Current:

```text
[1,3]
```

Next:

```text
[4,6]
```

Check:

```text
4 <= 3
```

False.

Update current interval:

```text
[4,6]
```

Next:

```text
[7,9]
```

Check:

```text
7 <= 6
```

False.

No overlap found.

Return:

```text
False
```

---

# Why Does This Work?

Sorting places intervals in increasing order of their starting values.

If an interval overlaps with any future interval,

it must overlap with the very next interval after sorting.

Therefore, checking consecutive intervals is sufficient.

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

Ignoring the space used by sorting:

```text
O(1)
```

---

# Concepts Used

- Sorting
- Greedy
- Intervals
- Arrays

---

# Python Features Used

### Sort

```python
intervals.sort()
```

---

### List Unpacking

```python
for start2, end2 in intervals[1:]:
```

---

# Key Takeaways

- Sort intervals by their starting values.
- Only consecutive intervals need to be compared.
- Two intervals overlap if:

```python
start2 <= end1
```

- Return `True` immediately when an overlap is found.
- Otherwise, continue checking until all intervals are processed.
- The optimal time complexity is **O(n log n)** due to sorting.

---

## Author

**Ramit Sarker**
