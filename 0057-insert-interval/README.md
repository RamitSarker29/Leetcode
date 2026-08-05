# 57. Insert Interval

## Problem

You are given a list of **non-overlapping intervals** sorted in ascending order of their starting points.

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

All of them merge into:

```text
[3,10]
```

---

# Intuition

One way to solve this problem is:

1. Insert the new interval into the list.
2. Sort all intervals.
3. Reuse the **Merge Intervals** algorithm to merge any overlapping intervals.

Although the original intervals are already sorted, this approach is simple because it builds directly on the solution to **LeetCode 56 - Merge Intervals**.

---

# Approach

### Step 1

Create a new list.

Traverse every interval.

When the correct position is found, insert `newInterval`.

```python
res.append(newInterval)
```

---

### Step 2

If the new interval was never inserted (it belongs at the end),

append it after the loop.

```python
if not inserted:
    res.append(newInterval)
```

---

### Step 3

Sort all intervals.

```python
res.sort()
```

Now the intervals are ordered by their starting values.

---

### Step 4

Use the Merge Intervals algorithm.

Keep one current interval.

```python
start1, end1 = res[0]
```

Traverse the remaining intervals.

---

### Step 5

If two intervals overlap,

```python
if end1 >= start2:
```

extend the current interval.

```python
end1 = max(end1, end2)
```

---

### Step 6

Otherwise,

store the completed interval.

```python
ans.append([start1, end1])
```

Start a new current interval.

```python
start1 = start2
end1 = end2
```

---

### Step 7

After finishing the loop,

append the final merged interval.

```python
ans.append([start1, end1])
```

---

# Algorithm

1. Handle the empty array.
2. Insert the new interval into a new list.
3. If necessary, append the new interval at the end.
4. Sort the list.
5. Merge overlapping intervals.
6. Return the merged intervals.

---

# Code

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        ans = []
        inserted = False

        for start, end in intervals:
            if not inserted and newInterval[0] <= start:
                res.append(newInterval)
                inserted = True
            res.append([start, end])

        if not inserted:
            res.append(newInterval)

        res.sort()

        start1, end1 = res[0]

        for start2, end2 in res[1:]:
            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                ans.append([start1, end1])
                start1, end1 = start2, end2

        ans.append([start1, end1])

        return ans
```

---

# Dry Run

### Example

```text
intervals = [[1,3],[6,9]]

newInterval = [2,5]
```

### After inserting

```text
[[1,3],[2,5],[6,9]]
```

### After sorting

```text
[[1,3],[2,5],[6,9]]
```

### Merge

Current:

```text
[1,3]
```

Next:

```text
[2,5]
```

Overlap:

```text
3 >= 2
```

Merged interval:

```text
[1,5]
```

Next interval:

```text
[6,9]
```

No overlap.

Store:

```text
[1,5]
```

Append remaining interval:

```text
[6,9]
```

Final Answer:

```text
[[1,5],[6,9]]
```

---

# Why Does This Work?

After inserting and sorting,

any overlapping intervals become adjacent.

The Merge Intervals algorithm then combines every overlapping pair into a single interval.

Since every interval is processed once after sorting,

all overlapping intervals are merged correctly.

---

# Time Complexity

Insertion:

```text
O(n)
```

Sorting:

```text
O(n log n)
```

Merging:

```text
O(n)
```

Overall:

```text
O(n log n)
```

---

# Space Complexity

```text
O(n)
```

Extra space is used for the result lists.

---

# Concepts Used

- Arrays
- Sorting
- Greedy
- Interval Merging

---

# Python Features Used

### Sort

```python
res.sort()
```

---

### List Unpacking

```python
start1, end1 = res[0]
```

---

### Maximum

```python
end1 = max(end1, end2)
```

---

### Append

```python
res.append(newInterval)
```

---

# Key Takeaways

- Insert the new interval into the list.
- Sort the intervals.
- Reuse the Merge Intervals algorithm.
- Merge overlapping intervals by extending the current interval.
- Append completed intervals to the answer.
- Overall complexity is **O(n log n)** because of sorting.

> **Note:** The optimal solution for this problem runs in **O(n)** because the input intervals are already sorted. This solution intentionally reuses the Merge Intervals approach, making it simpler to understand and implement while remaining correct.

---

## Author

**Ramit Sarker**
