# 56. Merge Intervals

## Problem

Given an array of intervals where:

```text
intervals[i] = [start, end]
```

merge all overlapping intervals and return the resulting list of **non-overlapping intervals**.

---

## Examples

### Example 1

**Input**

```text
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

**Output**

```text
[[1,6],[8,10],[15,18]]
```

**Explanation**

The intervals

```text
[1,3]

[2,6]
```

overlap, so they are merged into

```text
[1,6]
```

---

### Example 2

**Input**

```text
intervals = [[1,4],[4,5]]
```

**Output**

```text
[[1,5]]
```

**Explanation**

The intervals touch at `4`, so they are considered overlapping.

---

### Example 3

**Input**

```text
intervals = [[4,7],[1,4]]
```

**Output**

```text
[[1,7]]
```

---

# Intuition

If the intervals are not sorted, it is difficult to know which intervals overlap.

For example:

```text
[8,10]

[1,3]

[2,6]
```

Here, `[1,3]` and `[2,6]` should be merged, but they are separated.

So, the first step is to **sort the intervals by their starting value**.

After sorting:

```text
[1,3]

[2,6]

[8,10]
```

Now overlapping intervals become adjacent, allowing us to merge them in a single traversal.

---

# Key Observation

Suppose our current merged interval is:

```text
[1,6]
```

The next interval is:

```text
[4,8]
```

Since

```text
6 >= 4
```

the intervals overlap.

The merged interval becomes:

```text
[1,max(6,8)]

=

[1,8]
```

If instead the next interval is:

```text
[9,12]
```

Since

```text
6 < 9
```

there is no overlap.

The current interval is complete, so add it to the answer and start a new interval.

---

# Approach

1. Sort the intervals.
2. Take the first interval as the current interval.
3. Traverse the remaining intervals.
4. If the intervals overlap, merge them.
5. Otherwise, store the current interval and start a new one.
6. Add the final merged interval to the answer.

---

# Algorithm

### Step 1

Sort the intervals.

```python
intervals.sort()
```

---

### Step 2

Initialize the first interval.

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

If they overlap,

```python
if end1 >= start2:
```

extend the current interval.

```python
end1 = max(end1, end2)
```

---

### Step 5

Otherwise,

store the current interval.

```python
res.append([start1, end1])
```

Start a new interval.

```python
start1 = start2
end1 = end2
```

---

### Step 6

After the loop finishes,

the final interval has not yet been stored.

Append it.

```python
res.append([start1, end1])
```

---

# Code

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for start2, end2 in intervals[1:]:

            if end1 >= start2:
                end1 = max(end1, end2)

            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2

        res.append([start1, end1])

        return res
```

---

# Dry Run

### Example

```text
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

After sorting:

```text
[1,3]

[2,6]

[8,10]

[15,18]
```

Current interval:

```text
[1,3]
```

| Current | Next | Overlap? | Result |
|---------|------|:--------:|--------|
| [1,3] | [2,6] | ✅ | Merge → [1,6] |
| [1,6] | [8,10] | ❌ | Store [1,6] |
| [8,10] | [15,18] | ❌ | Store [8,10] |

After the loop:

```text
Store [15,18]
```

Final Answer:

```text
[[1,6],[8,10],[15,18]]
```

---

# Why Does This Work?

Sorting ensures that intervals are processed in increasing order of their starting values.

If two intervals overlap,

```text
Current End >= Next Start
```

they are merged into one interval.

Otherwise,

the current interval is complete and can safely be added to the answer.

---

# Time Complexity

Sorting:

```text
O(n log n)
```

Traversing the intervals:

```text
O(n)
```

Overall:

```text
O(n log n)
```

Sorting dominates the running time.

---

# Space Complexity

Ignoring the output list:

```text
O(1)
```

Including the output list:

```text
O(n)
```

in the worst case when no intervals overlap.

---

# Concepts Used

- Sorting
- Greedy Algorithm
- Arrays

---

# Python Features Used

### Sort a List

```python
intervals.sort()
```

---

### List Unpacking

```python
for start2, end2 in intervals[1:]:
```

---

### Maximum Value

```python
end1 = max(end1, end2)
```

---

### Append a List

```python
res.append([start1, end1])
```

---

# Key Takeaways

- Sort intervals by their starting value.
- Keep one **current merged interval**.
- If two intervals overlap, extend the current interval.
- Otherwise, save the current interval and begin a new one.
- Don't forget to append the **last merged interval** after the loop.
- Overall complexity is **O(n log n)**, which is the optimal solution for unsorted intervals.

---

## Author

**Ramit Sarker**
