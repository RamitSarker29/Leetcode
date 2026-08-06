# 986. Interval List Intersections

## Problem

You are given two lists of **closed intervals**:

- `firstList`
- `secondList`

Both lists are:

- Sorted in ascending order.
- Pairwise non-overlapping.

Return all intersections between the two lists.

---

## Example 1

![Example 1](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)

**Input**

```text
firstList = [[0,2],[5,10],[13,23],[24,25]]

secondList = [[1,5],[8,12],[15,24],[25,26]]
```

**Output**

```text
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

---

## Example 2

**Input**

```text
firstList = [[1,3],[5,9]]

secondList = []
```

**Output**

```text
[]
```

---

# Intuition

Since both interval lists are already **sorted** and **non-overlapping**, we can process them using **two pointers**.

At every step:

- Compare one interval from each list.
- Find their intersection.
- Move the pointer whose interval ends first.

Since an interval that ends first can never intersect any future interval from the other list, it is safe to discard it.

---

# Approach

### Step 1

Initialize two pointers.

```python
i = 0
j = 0
```

They point to the current interval in each list.

---

### Step 2

Continue while both lists still have intervals.

```python
while i < n1 and j < n2:
```

---

### Step 3

Find the possible intersection.

The intersection starts from the larger starting point.

```python
start = max(firstList[i][0], secondList[j][0])
```

The intersection ends at the smaller ending point.

```python
end = min(firstList[i][1], secondList[j][1])
```

---

### Step 4

An intersection exists only when

```python
start <= end
```

If true,

append it to the answer.

```python
res.append([start, end])
```

---

### Step 5

Move the pointer whose interval ends first.

If the first interval ends earlier,

```python
i += 1
```

If the second interval ends earlier,

```python
j += 1
```

If both end together,

move both pointers.

---

# Algorithm

1. Initialize two pointers.
2. Compare the current intervals.
3. Compute the possible intersection.
4. If it exists, store it.
5. Move the pointer whose interval ends first.
6. Continue until either list is exhausted.

---

# Code

```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []

        n1 = len(firstList)
        n2 = len(secondList)

        while i < n1 and j < n2:
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                res.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                j += 1

        return res
```

---

# Dry Run

### Input

```text
firstList = [[0,2],[5,10],[13,23],[24,25]]

secondList = [[1,5],[8,12],[15,24],[25,26]]
```

---

### Compare

```text
[0,2]

[1,5]
```

Intersection:

```text
start = max(0,1) = 1

end = min(2,5) = 2
```

Append:

```text
[1,2]
```

Since `2 < 5`, move `i`.

---

### Compare

```text
[5,10]

[1,5]
```

Intersection:

```text
[5,5]
```

Since `10 > 5`, move `j`.

---

### Compare

```text
[5,10]

[8,12]
```

Intersection:

```text
[8,10]
```

Since `10 < 12`, move `i`.

---

### Compare

```text
[13,23]

[15,24]
```

Intersection:

```text
[15,23]
```

Since `23 < 24`, move `i`.

---

### Compare

```text
[24,25]

[15,24]
```

Intersection:

```text
[24,24]
```

Since `25 > 24`, move `j`.

---

### Compare

```text
[24,25]

[25,26]
```

Intersection:

```text
[25,25]
```

Since both intervals end at `25`, move both pointers.

Answer:

```text
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

---

# Why Does This Work?

The intervals are already sorted.

At each step, the interval that finishes first cannot intersect any future interval from the other list.

Therefore, it is safe to move its pointer forward.

Since every interval is visited at most once, the algorithm efficiently finds every intersection.

---

# Time Complexity

Let:

- `n = len(firstList)`
- `m = len(secondList)`

Each pointer moves only forward.

Each interval is processed at most once.

```text
O(n + m)
```

---

# Space Complexity

Ignoring the output array:

```text
O(1)
```

Including the output array:

```text
O(k)
```

where `k` is the number of intersections.

---

# Concepts Used

- Two Pointers
- Interval Problems
- Greedy
- Arrays

---

# Python Features Used

### Maximum

```python
max(a, b)
```

Finds the larger starting point.

---

### Minimum

```python
min(a, b)
```

Finds the smaller ending point.

---

### Append

```python
res.append([start, end])
```

Stores the intersection.

---

# Key Takeaways

- Since both lists are sorted, two pointers are sufficient.
- The intersection starts at the larger start and ends at the smaller end.
- An intersection exists only if:

```python
start <= end
```

- Move the pointer whose interval ends first.
- If both intervals end together, move both pointers.
- Every interval is processed at most once, giving an optimal **O(n + m)** solution.

---

## Author

**Ramit Sarker**
