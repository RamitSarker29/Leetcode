# 57. Insert Interval

## Problem

You are given a list of **non-overlapping intervals** sorted in ascending order by their starting values.

You are also given a new interval.

Insert the new interval into the list such that:

- The intervals remain sorted.
- Any overlapping intervals are merged.

Return the updated list.

---

## Examples

### Example 1

**Input**

```text
intervals = [[1,3],[6,9]]

newInterval = [2,5]
```

**Output**

```text
[[1,5],[6,9]]
```

**Explanation**

`[2,5]` overlaps with `[1,3]`, so they merge into:

```text
[1,5]
```

---

### Example 2

**Input**

```text
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

newInterval = [4,8]
```

**Output**

```text
[[1,2],[3,10],[12,16]]
```

**Explanation**

`[4,8]` overlaps with:

```text
[3,5]

[6,7]

[8,10]
```

After merging, they become:

```text
[3,10]
```

---

# Intuition

The intervals are already:

- Sorted
- Non-overlapping

So sorting again is unnecessary.

Instead, traverse the array only once.

Each interval will belong to one of three cases:

1. Completely before `newInterval`
2. Overlapping `newInterval`
3. Completely after `newInterval`

---

# Approach

### Case 1: Interval is before `newInterval`

If the current interval ends before `newInterval` starts,

they cannot overlap.

```python
intervals[i][1] < newInterval[0]
```

Simply add the interval to the answer.

```python
res.append(intervals[i])
```

---

### Case 2: Interval overlaps `newInterval`

If the current interval starts before or at the end of `newInterval`,

they overlap.

```python
intervals[i][0] <= newInterval[1]
```

Merge them by expanding `newInterval`.

Start:

```python
newInterval[0] = min(newInterval[0], intervals[i][0])
```

End:

```python
newInterval[1] = max(newInterval[1], intervals[i][1])
```

Continue merging until there are no more overlapping intervals.

---

### Case 3: Interval is after `newInterval`

Once all overlapping intervals are merged,

append the merged interval.

```python
res.append(newInterval)
```

Then append the remaining intervals.

---

# Algorithm

1. Add all intervals completely before `newInterval`.
2. Merge every overlapping interval into `newInterval`.
3. Append the merged interval.
4. Append the remaining intervals.
5. Return the answer.

---

# Code

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add merged interval
        res.append(newInterval)

        # Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```

---

# Dry Run

### Example

```text
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

newInterval = [4,8]
```

### Step 1

Current:

```text
[1,2]
```

Since

```text
2 < 4
```

it is completely before `newInterval`.

Answer:

```text
[[1,2]]
```

---

### Step 2

Current:

```text
[3,5]
```

It overlaps.

Merge:

```text
newInterval

[3,8]
```

---

Current:

```text
[6,7]
```

Merge again:

```text
[3,8]
```

(No change.)

---

Current:

```text
[8,10]
```

Merge:

```text
[3,10]
```

---

### Step 3

Append the merged interval.

```text
[[1,2],[3,10]]
```

---

### Step 4

Append the remaining interval.

```text
[[1,2],[3,10],[12,16]]
```

---

# Why Does This Work?

Since the intervals are already sorted,

all intervals before `newInterval` appear first,

all overlapping intervals appear together,

and all remaining intervals appear afterwards.

Therefore, a single traversal is sufficient.

---

# Time Complexity

Each interval is processed exactly once.

```text
O(n)
```

---

# Space Complexity

The output list stores the answer.

```text
O(n)
```

---

# Concepts Used

- Arrays
- Greedy
- Interval Merging

---

# Python Features Used

### Minimum

```python
min(a, b)
```

---

### Maximum

```python
max(a, b)
```

---

### Append

```python
res.append(interval)
```

---

# Key Takeaways

- The input intervals are already sorted.
- No sorting is required.
- Traverse the array only once.
- Handle three cases:
  - Before `newInterval`
  - Overlapping `newInterval`
  - After `newInterval`
- Merge by expanding `newInterval`.
- The solution runs in **O(n)** time, which is the optimal complexity.

---

## Author

**Ramit Sarker**
